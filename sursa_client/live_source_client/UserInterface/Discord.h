#pragma once
#include "StdAfx.h"
#include "PythonCharacterManager.h"
#include "PythonBackground.h"
#include "PythonPlayer.h"
#include "PythonGuild.h"

namespace Discord
{
	const auto DiscordClientID = "1457557713700782313";

	using DCDATA = std::pair<std::string, std::string>;

	/*NAME*/
	DCDATA GetNameData()
	{
		// website info
		auto website = "Site: " + std::string("www.luramt2.ro");
		
		// Name, guild
		auto CHName = "Name: " + std::string(CPythonPlayer::Instance().GetName());
		std::string GuildName;
		if (CPythonGuild::Instance().GetGuildName(CPythonPlayer::Instance().GetGuildID(), &GuildName))
			CHName += ", Guild: " + GuildName;

		return { website, CHName };
	}

	/*RACE*/
	DCDATA GetRaceData()
	{
		auto pInstance = CPythonCharacterManager::Instance().GetMainInstancePtr();
		if (!pInstance)
			return { "","" };

		auto RACENUM = pInstance->GetRace();

		// Image Race
		auto RaceImage = "race_" + std::to_string(RACENUM);

		// Race name
		auto RaceName = "Warrior";
		switch (RACENUM)
		{
		case NRaceData::JOB_ASSASSIN:
		case NRaceData::JOB_ASSASSIN + 4:
			RaceName = "Assassin";
			break;
		case NRaceData::JOB_SURA:
		case NRaceData::JOB_SURA + 4:
			RaceName = "Sura";
			break;
		case NRaceData::JOB_SHAMAN:
		case NRaceData::JOB_SHAMAN + 4:
			RaceName = "Shaman";
			break;
		}
		return { RaceImage , RaceName };
	}

	/*EMPIRE*/
	DCDATA GetEmpireData()
	{
		auto pInstance = CPythonCharacterManager::Instance().GetMainInstancePtr();
		if (!pInstance)
			return { "","" };

		auto EmpireID = pInstance->GetEmpireID();

		// Empire Image
		auto EmpireImage = "empire_" + std::to_string(EmpireID);

		// Empire Name
		auto EmpireName = "Shinsoo";
		switch (EmpireID)
		{
		case 2:
			EmpireName = "Chunjo";
			break;
		case 3:
			EmpireName = "Jinno";
		}
		return { EmpireImage, EmpireName};
	}
}
