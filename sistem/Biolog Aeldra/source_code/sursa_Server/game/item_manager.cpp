# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	#include "BiologSystemManager.hpp"
#endif

# AFTER


	if (GetDropPerKillPct(100, 1000, iDeltaPercent, "lotto_drop") >= number(1, iRandRange))
	{
		DWORD* pdw = M2_NEW DWORD[3];

		pdw[0] = 50001;
		pdw[1] = 1;
		pdw[2] = quest::CQuestManager::instance().GetEventFlag("lotto_round");

		DBManager::instance().ReturnQuery(QID_LOTTO, pkKiller->GetPlayerID(), pdw,
			"INSERT INTO lotto_list VALUES(0, 'server%s', %u, NOW())",
			get_table_postfix(), pkKiller->GetPlayerID());
	}

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	{
		DWORD itemVnum = 0;
		BYTE chance = 0;
		int random = number(1, 100);

		if (pkChr->IsMonster() && pkKiller)
		{
			CBiologSystem* pkBiologManager = pkKiller->GetBiologManager();
			if (pkBiologManager->GetBiologItemByMobVnum(pkKiller, pkChr->GetRaceNum(), itemVnum, chance))
			{
				if (random <= chance)
				{
					if ((item = CreateItem(itemVnum, 1, 0, true)))
						vec_item.push_back(item);
				}
			}
		}
	}
#endif