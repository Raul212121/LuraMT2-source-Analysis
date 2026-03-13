#include "StdAfx.h"

#ifdef ENABLE_BATTLE_PASS
#include "PythonNetworkStream.h"
#include "../EterFSLib/FileSystemManager.hpp"
#include "PythonBattlePass.h"

#ifdef max
#undef max
#endif

#ifdef min
#undef min
#endif

#include <rapidjson/document.h>
#include <rapidjson/istreamwrapper.h>
#include <rapidjson/error/en.h>

CPythonBattlePass::CPythonBattlePass()
{
	battlepassMap.clear();
	rewardMap.clear();
}

CPythonBattlePass::~CPythonBattlePass()
{
	battlepassMap.clear();
	rewardMap.clear();
}

bool CPythonBattlePass::Initialize(const char* filename)
{
	if (!battlepassMap.empty())
		battlepassMap.clear();

	auto file = PackGet(filename);
	if (!file)
		return false;

	rapidjson::Document document;
	document.Parse(reinterpret_cast<const char*>(file->get_data()), file->get_size());

	rewardMap.clear();
	uint8_t positionMap = 0;

	if (document.HasParseError())
	{
		TraceError("%s parse failed! Error: %s offset: %u", filename, GetParseError_En(document.GetParseError()), document.GetErrorOffset());
		return false;
	}

	if (!document.IsArray())
	{
		TraceError("%s: the document isn't an array", filename);
		return false;
	}

	std::set<uint8_t> finalMissions = { MISSION_FREE_END };

	for (size_t i = 0; i < document.Size(); ++i)
	{
		TBattlePassParser data = {};
		const auto& v = document[i];
		if (!v.IsObject())
		{
			TraceError("%s: the document(%u) isn't an object", filename, i);
			return false;
		}

		const auto& missionID = v["missionID"];
		if (!missionID.IsUint())
		{
			TraceError("%s: document(%u) the `missionID` isn't an integer", filename, i);
			return false;
		}

		data.missionVnum = missionID.GetUint();


		if (finalMissions.count(static_cast<uint8_t>(missionID.GetUint())))
		{

			const auto& rewardItem = v["rewardItem"];
			if (!rewardItem.IsArray())
			{
				TraceError("%s: document(%u) the `rewardItem` isn't an array", filename, i);
				return false;
			}

			const auto& rewardCount = v["rewardCount"];
			if (!rewardCount.IsArray())
			{
				TraceError("%s: document(%u) the `rewardCount` isn't an array", filename, i);
				return false;
			}

			std::vector<TRewardTableBP> rewardVector = {};
			rewardVector.clear();

			for (auto n = 0; n < rewardCount.GetArray().Size(); ++n)
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

			const auto& missionName = v["missionName"];
			if (!missionName.IsString())
			{
				TraceError("%s: document(%u) the `missionName` isn't an string", filename, i);
				return false;
			}

			data.missionName = missionName.GetString();

			const auto& maxProgress = v["maxProgress"];
			if (!maxProgress.IsUint())
			{
				TraceError("%s: document(%u) the `maxProgress` isn't an integer", filename, i);
				return false;
			}

			data.maxProgress = maxProgress.GetUint();

			const auto& itemArray = v["itemArray"];
			if (!itemArray.IsArray())
			{
				TraceError("%s: document(%u) the `itemArray` isn't an array", filename, i);
				return false;
			}

			const auto& rewardArray = v["rewardArray"];
			if (!rewardArray.IsArray())
			{
				TraceError("%s: document(%u) the `rewardArray` isn't an array", filename, i);
				return false;
			}

			for (auto n = 0; n < BATTLEPASS_REWARD_COUNT; ++n)
			{
				assert(itemArray[n].IsUint64());
				assert(rewardArray[n].IsUint64());

				data.rewards[n].vnum = itemArray[n].GetUint64();
				data.rewards[n].count = rewardArray[n].GetUint64();
			}

			const auto& missionDescArray = v["missionDescArray"];
			if (!missionDescArray.IsArray())
			{
				TraceError("%s: document(%u) the `missionDescArray` isn't an array", filename, i);
				return false;
			}

			for (size_t desc = 0; desc < BATTLEPASS_MAX_DESC_LINES; ++desc)
				data.descArray[desc] = missionDescArray[desc].GetString();


			const auto& isFormat = v["isFormat"];
			if (!isFormat.IsBool())
			{
				TraceError("%s: document(%u) the `isFormat` isn't an bool", filename, i);
				return false;
			}

			data.isFormat = isFormat.GetBool();

			data.progress = 0;
			battlepassMap.insert(std::make_pair(i, data));
		}

	}
	return true;
	
}

void CPythonBattlePass::Destroy()
{
	battlepassMap.clear(); //Clear map
}

const TBattlePassParser* CPythonBattlePass::GetBattlePassMap(uint32_t vnum)
{
	auto it = battlepassMap.find(vnum);
	if (it == battlepassMap.end())
		return NULL;

	return &it->second;
}

void CPythonBattlePass::UpdateBattlePass(const TBattlePass& info)
{

	auto it = battlepassMap.find(info.missionVnum);
	if (it != battlepassMap.end())
	{
		it->second.progress = info.progress;
		it->second.isActive = info.isActive;
		// Etc
	}
	
}

PyObject* battlepassGetMissionName(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();
	
	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("s", "");
	
	return Py_BuildValue("s", rkInfo->missionName.c_str());
}

PyObject* battlepassGetActive(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", rkInfo->isActive);
}

PyObject* battlepassGetMissionMax(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", rkInfo->maxProgress);
}

PyObject* battlepassGetMissionStatus(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", rkInfo->progress);
}


PyObject* battlepassGetMissionReward(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	uint16_t reward;
	if (!PyTuple_GetInteger(poArgs, 1, &reward))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("ii", 0, 0);

	return Py_BuildValue("ii", rkInfo->rewards[reward].vnum, rkInfo->rewards[reward].count);
}

PyObject* battlepassGetMissionDesc(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	uint16_t desc;
	if (!PyTuple_GetInteger(poArgs, 1, &desc))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("s", "");

	return Py_BuildValue("s", rkInfo->descArray[desc].c_str()); 
}

PyObject* battlepassGetMissionProgress(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("ii", 0, 0);

	return Py_BuildValue("ii", rkInfo->rewards[mission].vnum, rkInfo->rewards[mission].count);
}

PyObject* battlepassGetMissionSize(PyObject* poSelf, PyObject* poArgs)
{
	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	return Py_BuildValue("i", rk.GetBattlePassMapSize());
}

PyObject* battlepassGetSubMissions(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	uint16_t sub;
	if (!PyTuple_GetInteger(poArgs, 1, &sub))
		return Py_BuildException();
	
	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", rkInfo->subMissions[sub]);
}

PyObject* battlepassIsSubMission(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", rkInfo->isSubMission);
}

PyObject* battlepassIsFormat(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetBattlePassMap(mission);
	if (!rkInfo)
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", rkInfo->isFormat);
}

PyObject* battlepassGetRewards(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	uint16_t reward;
	if (!PyTuple_GetInteger(poArgs, 1, &reward))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetRewardMap().find(mission);

	if (rkInfo == rk.GetRewardMap().end())
		return Py_BuildValue("ii", 0, 0);


	return Py_BuildValue("ii", rkInfo->second[reward].vnum, rkInfo->second[reward].count);

}

PyObject* battlepassGetRewardsSize(PyObject* poSelf, PyObject* poArgs)
{
	uint16_t mission;
	if (!PyTuple_GetInteger(poArgs, 0, &mission))
		return Py_BuildException();

	CPythonBattlePass& rk = CPythonBattlePass::Instance();
	const auto& rkInfo = rk.GetRewardMap().find(mission);

	if (rkInfo == rk.GetRewardMap().end())
		return Py_BuildValue("i", 0);

	return Py_BuildValue("i", rkInfo->second.size());

}


void initBattlePass()
{
	static PyMethodDef s_methods[] =
	{
		{ "GetMissionName",				battlepassGetMissionName,					METH_VARARGS },
		{ "GetMissionMax",				battlepassGetMissionMax,					METH_VARARGS },
		{ "GetMissionProgress",			battlepassGetMissionStatus,					METH_VARARGS },
		{ "IsActive",			battlepassGetActive,					METH_VARARGS },
		
		{ "GetMissionReward",			battlepassGetMissionReward,					METH_VARARGS },
		{ "GetMissionRewardFinal",			battlepassGetRewards,					METH_VARARGS },

		{ "GetMissionDesc",				battlepassGetMissionDesc,					METH_VARARGS },
		{ "GetMissionProgressReward",			battlepassGetMissionProgress,					METH_VARARGS },

		{ "GetMissionSize",			battlepassGetMissionSize,					METH_VARARGS },
		{ "GetMissionRewardFinalSize",			battlepassGetRewardsSize,					METH_VARARGS },
		
		{ "GetSubMissions",			battlepassGetSubMissions,					METH_VARARGS },
		
		{ "IsSubMission",			battlepassIsSubMission,					METH_VARARGS },
		{ "IsFormat",			battlepassIsFormat,					METH_VARARGS },
		
		{ NULL, NULL, NULL }, 
	};

	PyObject * poModule = Py_InitModule("battlepass", s_methods);

	PyModule_AddIntConstant(poModule, "BATTLEPASS_REWARD_COUNT", BATTLEPASS_REWARD_COUNT);
	PyModule_AddIntConstant(poModule, "BATTLEPASS_MAX_DESC_LINES", BATTLEPASS_MAX_DESC_LINES);
	PyModule_AddIntConstant(poModule, "MISSION_FREE_END", MISSION_FREE_END);

}
#endif
