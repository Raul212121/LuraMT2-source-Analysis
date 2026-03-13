#include "stdafx.h"

#ifdef ENABLE_EVENT_FIND_NPC
#include "char.h"
#include "db.h"
#include "config.h"
#include "locale_service.h"
#include "sectree_manager.h"
#include "char_manager.h"
#include "NpcFinderManager.h"

#ifdef min
#undef min
#endif

#ifdef max
#undef max
#endif

#include <rapidjson/document.h>
#include <rapidjson/istreamwrapper.h>
#include <rapidjson/error/en.h>
#include <fmt/format.h>
#include <fstream>
#include <random>

EventManagerAddons::EventManagerAddons()
{
	ClearEvent();
	ClearEventBoss();
}

EventManagerAddons::~EventManagerAddons()
{
	m_pkNPC = nullptr;

	isEventEnabled = false;
	isEventEnabledBoss = false;

	spawnStage = 0;

	npcFinderMap.clear();
	npcFinderTriggerMap.clear();
}


void EventManagerAddons::BootNPCMap()
{
	if (g_bAuthServer)
		return;

	npcFinderMap.clear();

	char filename[PATH_MAX] = {};
	snprintf(filename, sizeof(filename), "%s/npcEvent.json", LocaleService_GetBasePath().c_str());
	std::ifstream ifs(filename, std::ios::in);

	if (ifs.fail())
		return;

	rapidjson::Document document;
	rapidjson::IStreamWrapper isw(ifs);
	document.ParseStream(isw);

	if (document.HasParseError())
	{
		sys_err("%s parse failed! Error: %s offset: %u", filename, GetParseError_En(document.GetParseError()), document.GetErrorOffset());
		return;
	}

	if (!document.IsArray())
	{
		sys_err("%s: the document isn't an array", filename);
		return;
	}

	for (size_t i = 0; i < document.Size(); ++i)
	{
		TEventFind data = {};

		const auto& v = document[i];
		if (!v.IsObject())
		{
			sys_err("%s: the document(%u) isn't an object", filename, i);
			return;
		}

		const auto& mapIndex = v["mapIndex"];
		if (!mapIndex.IsUint())
		{
			sys_err("%s: document(%u) the `mapIndex` isn't an integer", filename, i);
			return;
		}

		data.mapIndex = mapIndex.GetUint();

		const auto& coords = v["coords"];
		if (!coords.IsArray())
		{
			sys_err("%s: document(%u) the `coords` isn't an array", filename, i);
			return;
		}

		data.x = coords[0].IsUint() ? coords[0].GetUint() : 0;
		data.y = coords[1].IsUint() ? coords[1].GetUint() : 0;

		const auto& hints = v["hints"];
		if (!hints.IsArray())
		{
			sys_err("%s: document(%u) the `hints` isn't an array", filename, i);
			return;
		}

		data.hint = hints[0].GetString();

		npcFinderMap.emplace_back(data);
	}
}

void EventManagerAddons::OnTriggerEvent()
{
	if (isEventEnabled)
		return;

	if (npcFinderMap.empty())
	{
		sys_err("Failed to initialize finder map");
		return;
	}

	std::vector<TEventFind> tempVector;

	// Assign Temporary Vector elements from all finder map
	tempVector.assign(npcFinderMap.begin(), npcFinderMap.end());

	// Randomize Temporary Vector
	auto rd = std::random_device{};
	auto randomizer = std::default_random_engine {rd ()};
	std::shuffle(std::begin(tempVector), std::end(tempVector), randomizer);

	// Assign 10 values from Temporary Vector to Vector Map
	npcFinderTriggerMap.clear();

	for (uint8_t i = 0; i < 10; i++)
		npcFinderTriggerMap.emplace_back(tempVector[i]);

	isEventEnabled = true;

	HandleSpawning();
}

void EventManagerAddons::ClearEventBoss()
{
	isEventEnabledBoss = false;
}
void EventManagerAddons::ClearEvent()
{
	m_pkNPC = nullptr;

	isEventEnabled = false;
	spawnStage = 0;

	npcFinderTriggerMap.clear();
}

void EventManagerAddons::HandleSpawning()
{
	if (!isEventEnabled)
		return;

	if (m_pkNPC)
		return;

	// If event map is empty, stop the event
	if (npcFinderTriggerMap.empty())
	{
		SendNotice("Au fost gasite toate npc-urile, eveniment-ul s-a incheiat!");
		ClearEvent();
		return;
	}

	const auto& npcData = npcFinderTriggerMap.at(0);

	//Checks for spawning
	if (!map_allow_find(npcData.mapIndex))
		return;

	const auto pkSectreeMap = SECTREE_MANAGER::instance().GetMap(npcData.mapIndex);
	if (!pkSectreeMap)
		return;

	//Spawn The Npc
	m_pkNPC = CHARACTER_MANAGER::Instance().SpawnMob(20359, npcData.mapIndex, pkSectreeMap->m_setting.iBaseX + npcData.x * 100, pkSectreeMap->m_setting.iBaseY + npcData.y * 100, 0);
	if (!m_pkNPC)
	{
		ClearEvent();

		sys_err("Failed to create npc instance.");
		return;
	}

	//Announcements
	auto eventBroadCast = fmt::format("[Event Find] Un NPC a fost spawnat, indiciu {}", npcData.hint);
	BroadcastNotice(eventBroadCast.c_str());

	if (test_server)
	{
		eventBroadCast = fmt::format("[Event Find Test] Un NPC a fost spawnat, coordonate {} {} {} {}", m_pkNPC->GetX(), m_pkNPC->GetY(), npcData.x, npcData.y);

		BroadcastNotice(eventBroadCast.c_str());
	}

	//Erase from spawning map

	npcFinderTriggerMap.erase(npcFinderTriggerMap.begin());
}


void EventManagerAddons::OnTriggerNPC(LPCHARACTER pkNpc, LPCHARACTER pkChr)
{
	if (!pkNpc || pkNpc != m_pkNPC)
		return;

	if (!pkChr)
		return;

	const auto notice = fmt::format("[Event Find]: {} a gasit NPC-ul si a castigat 100 MD-uri", pkChr->GetName());
	BroadcastNotice(notice.c_str());
	M2_DESTROY_CHARACTER(pkNpc);
	m_pkNPC = nullptr;

	pkChr->AutoGiveItem(80017);

	HandleSpawning();
}
struct FExitAllToMap
{
	void operator()(LPENTITY ent)
	{
		if (ent->IsType(ENTITY_CHARACTER))
		{
			LPCHARACTER ch = (LPCHARACTER) ent;

			if (ch->IsPC())
				ch->GoHome();
		}
	}
};
void EventManagerAddons::OnTriggerBossEvent(bool status)
{
	if (!map_allow_find(GetEventMapIndex()))
		return;

	if (!status)
	{
		const auto pMap = SECTREE_MANAGER::instance().GetMap(GetEventMapIndex());

		if (!pMap)
		{
			sys_err("cannot find map by index %d", GetEventMapIndex());
			return;
		}

		FExitAllToMap f;
		pMap->for_each(f);
	}
	else
	{

	}

	isEventEnabledBoss = status;
}

void EventManagerAddons::OnEnterMap(const LPCHARACTER pkChar) const
{
	if (!GetEventStatusBoss())
		return;

	if (!pkChar)
		return;

	if (!pkChar->CanWarp())
		return;

	if ((pkChar->GetLevel() >= 45))
		pkChar->WarpSet(50830, 62886, GetEventMapIndex());
	else
		pkChar->ChatPacket(CHAT_TYPE_INFO, "[Info] Te poti teleporta doar de la nivelul 45");
}

#endif


