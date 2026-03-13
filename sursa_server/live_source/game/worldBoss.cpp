#include "stdafx.h"

#ifdef ENABLE_WORLD_BOSS
#include "../common/tables.h"
#include "db.h"
#include "char.h"
#include "char_manager.h"
#include "config.h"
#include "utils.h"
#include "worldBoss.h"

CWorldBossManager::CWorldBossManager(): m_pkSpawnEvent(nullptr)
{
	m_spawnData = {{61009, {219, 1241700, 1213400}}, {693, {219, 1266500, 1215600}}};
	m_bossesSpawnClock = {{61009, {false, get_global_time()}}, {693, {false, get_global_time()}}};
}

CWorldBossManager::~CWorldBossManager()
{
	Destroy();
}

EVENTINFO(EventsManagerInfoData)
{
	EventsManagerInfoData() = default;
};

EVENTFUNC(spwan_event_timer)
{
	if (event == nullptr)
		return 0;

	if (event->info == nullptr)
		return 0;

	CWorldBossManager::instance().PrepareChecker();
	return PASSES_PER_SEC(5);
}

void CWorldBossManager::PrepareChecker()
{
	const time_t cur_Time = time(nullptr);
	const tm vKey = *localtime(&cur_Time);

	const auto& day = vKey.tm_wday;
	const auto& hour = vKey.tm_hour;
	const auto& minute = vKey.tm_min;
	const auto& second = vKey.tm_sec;

	HandleBossEvent(day, hour, minute, second);
}

void CWorldBossManager::Initialize()
{
	if (g_bAuthServer)
		return;

	if (m_pkSpawnEvent != nullptr)
	{
		event_cancel(&m_pkSpawnEvent);
		m_pkSpawnEvent = nullptr;
	}

	const time_t cur_Time = time(nullptr);
	const tm vKey = *localtime(&cur_Time);

	const auto& hour = vKey.tm_hour;

	EventsManagerInfoData* info = AllocEventInfo<EventsManagerInfoData>();

	m_pkSpawnEvent = event_create(spwan_event_timer, info, PASSES_PER_SEC(5));
}

void CWorldBossManager::Destroy()
{
	if (m_pkSpawnEvent != nullptr)
	{
		event_cancel(&m_pkSpawnEvent);
		m_pkSpawnEvent = nullptr;
	}
}
void CWorldBossManager::HandleBossEvent(const int day, const int hour, const int minute, const int second)
{
	const std::list<uint8_t> spawningHoursAlastor = {0, 6, 12, 18, 24};
	for (const auto& spawning : spawningHoursAlastor)
		if (spawning == hour && minute == 0)
			SpawnWorldBossCheck(61009);

	const std::list<uint8_t> spawningHoursOrc = { 3, 9, 15, 21, 24 };
	for (const auto& spawning : spawningHoursOrc)
		if (spawning == hour && minute == 0)
			SpawnWorldBossCheck(693);

}
void CWorldBossManager::SpawnWorldBossCheck(DWORD dwBoss)
{
	const auto bossData = m_bossesSpawnClock.find(dwBoss);
	if (bossData != m_bossesSpawnClock.end())
	{
		const int lastSpawn = bossData->second.second - get_global_time();
		if (!bossData->second.first && lastSpawn < 0)
		{
			bossData->second.second = get_global_time() + 600; // 10 Minutes
			const auto bossSpawndata = m_spawnData.find(dwBoss);
			if (bossSpawndata != m_spawnData.end())
			{
				if (!map_allow_find(bossSpawndata->second.map))
					return;
				const auto pkBoss = CHARACTER_MANAGER::instance().SpawnMob(bossSpawndata->first, bossSpawndata->second.map, bossSpawndata->second.x, bossSpawndata->second.y, 0, false, -1, true);
				if (!pkBoss)
				{
					sys_err("Failed spawning the boss, vnum %d", bossSpawndata->first);
					return;
				}

				pkBoss->SetAggressive();

				char szNoticeBoss[100];
				snprintf(szNoticeBoss, sizeof(szNoticeBoss), "%s a fost spawnat!", pkBoss->GetName());

				BroadcastNotice(szNoticeBoss);
			}
			bossData->second.first = true;
		}
	}
}

void CWorldBossManager::OnKillWorldBoss(LPCHARACTER pkBoss)
{
	if (!pkBoss)
		return;

	const auto bossData = m_bossesSpawnClock.find(pkBoss->GetRaceNum());
	if (bossData != m_bossesSpawnClock.end())
	{
		char szNoticeBoss[100];
		snprintf(szNoticeBoss, sizeof(szNoticeBoss), "%s a fost batut!", pkBoss->GetName());

		BroadcastNotice(szNoticeBoss);
		bossData->second.first = false;
	}
}

#endif
