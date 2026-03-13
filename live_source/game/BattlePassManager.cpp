#include "stdafx.h"

#ifdef ENABLE_BATTLE_PASS
#include "BattlePassManager.h"
#include "char.h"
#include "db.h"
#include "config.h"
#include "locale_service.h"

#ifdef min
#undef min
#endif

#ifdef max
#undef max
#endif

#include <rapidjson/document.h>
#include <rapidjson/istreamwrapper.h>
#include <rapidjson/error/en.h>
#include <fstream>

CBattlePass::CBattlePass()
{

}

CBattlePass::~CBattlePass()
{
	battlepassMap.clear();
}


void CBattlePass::BootBattlePassMap()
{
	if (g_bAuthServer)
		return;

	battlepassMap.clear();
	rewardMap.clear();

	uint8_t positionMap = 0;

	char filename[PATH_MAX] = {};
	snprintf(filename, sizeof(filename), "%s/battlepass.json", LocaleService_GetBasePath().c_str());
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

	std::set<uint8_t> finalMissions = { MISSION_FREE_END  };

	for (size_t i = 0; i < document.Size(); ++i)
	{
		TBattlePassParser data = {};

		const auto& v = document[i];
		if (!v.IsObject())
		{
			sys_err("%s: the document(%u) isn't an object", filename, i);
			return;
		}

		const auto& missionID = v["missionID"];
		if (!missionID.IsUint())
		{
			sys_err("%s: document(%u) the `missionID` isn't an integer", filename, i);
			return;
		}

		data.missionVnum = missionID.GetUint();

		if (finalMissions.count(static_cast<uint8_t>(missionID.GetUint())))
		{

			const auto& rewardItem = v["rewardItem"];
			if (!rewardItem.IsArray())
			{
				sys_err("%s: document(%u) the `rewardItem` isn't an array", filename, i);
				return;
			}

			const auto& rewardCount = v["rewardCount"];
			if (!rewardCount.IsArray())
			{
				sys_err("%s: document(%u) the `rewardCount` isn't an array", filename, i);
				return;
			}

			std::vector<TRewardTableBP> rewardVector = {};
			rewardVector.clear();

			for (rapidjson::SizeType n = 0; n < rewardCount.GetArray().Size(); ++n)
			{
				TRewardTableBP reward = {};

				assert(rewardItem[n].IsUint());
				assert(rewardCount[n].IsUint());

				reward.vnum = rewardItem[n].GetUint();
				reward.count = rewardCount[n].GetUint();

				rewardVector.emplace_back(reward);
			}

			rewardMap.emplace(positionMap, rewardVector);
			positionMap++;

		}
		else
		{
			const auto& maxProgress = v["maxProgress"];
			if (!maxProgress.IsUint())
			{
				sys_err("%s: document(%u) the `maxProgress` isn't an integer", filename, i);
				return;
			}

			data.maxProgress = maxProgress.GetUint();

			const auto& itemArray = v["itemArray"];
			if (!itemArray.IsArray())
			{
				sys_err("%s: document(%u) the `itemArray` isn't an array", filename, i);
				return;
			}

			const auto& rewardArray = v["rewardArray"];
			if (!rewardArray.IsArray())
			{
				sys_err("%s: document(%u) the `rewardArray` isn't an array", filename, i);
				return;
			}

			for (auto n = 0; n < BATTLEPASS_REWARD_COUNT; ++n)
			{
				assert(itemArray[n].IsUint());
				assert(rewardArray[n].IsUint());

				data.rewards[n].vnum = itemArray[n].GetUint();
				data.rewards[n].count = rewardArray[n].GetUint();
			}

			battlepassMap.emplace(i, data);
		}
	}
}

const TBattlePassParser* CBattlePass::GetBattlePassMap(uint32_t vnum)
{
	auto it = battlepassMap.find(vnum);
	if (it == battlepassMap.end())
		return NULL;

	return &it->second;
}

std::tuple<uint16_t, uint16_t> CBattlePass::GetBattlePassRange(uint16_t id) const
{
	switch (id)
	{
		case BATTLEPASS_FREE:
			return std::make_tuple(MISSION_FREE_START, MISSION_FREE_END);

		default: break;
	}

	return std::make_tuple(MISSION_FREE_START, MISSION_FREE_END);
}

#endif



