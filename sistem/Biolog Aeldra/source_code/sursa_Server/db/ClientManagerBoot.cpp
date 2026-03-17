# BEFORE
using namespace std;

# ADD

#define DIRECT_QUERY(query) CDBManager::instance().DirectQuery((query))

# IN FUNCTION

bool CClientManager::InitializeTables()
{

    ...

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	if (!InitializeBiologMissions())
	{
		sys_err("InitializeBiologMissions FAILED");
		return false;
	}

	if (!InitializeBiologRewards())
	{
		sys_err("InitializeBiologRewards FAILED");
		return false;
	}

	if (!InitializeBiologMonsters())
	{
		sys_err("InitializeBiologMonsters FAILED");
		return false;
	}
#endif

# BEFORE 

	return true;
}

# AT THE BOTTOM FILE ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
bool CClientManager::InitializeBiologMissions()
{
	MYSQL_ROW data;
	const char szQuery[] = "SELECT `mission`, `required_lvl`, `required_item`, `required_item_count`, `cooldown`, `chance` FROM `player`.biolog_missions ORDER BY mission;";
	std::unique_ptr<SQLMsg> pMsg(DIRECT_QUERY(szQuery));

	if (pMsg->uiSQLErrno != 0)
	{
		sys_err("CANNOT LOAD biolog_missions TABLE , errorcode %d ", pMsg->uiSQLErrno);
		return false;
	}

	if (!m_vec_BiologMissions.empty())
	{
		sys_log(0, "RELOAD: biolog_missions upgrade");
		m_vec_BiologMissions.clear();
	}

	if (pMsg->Get())
	{
		sys_log(0, "BIOLOG_MISSIONS: Table size is %u", pMsg->Get()->uiNumRows);

		while ((data = mysql_fetch_row(pMsg->Get()->pSQLResult)))
		{
			TBiologMissionsProto b;
			memset(&b, 0, sizeof(TBiologMissionsProto));

			int col = 0;

			str_to_number(b.bMission, data[col++]);
			str_to_number(b.bRequiredLevel, data[col++]);
			str_to_number(b.iRequiredItem, data[col++]);
			str_to_number(b.wRequiredItemCount, data[col++]);
			str_to_number(b.iCooldown, data[col++]);
			str_to_number(b.bChance, data[col++]);

			sys_log(0, "BIOLOG_MISSIONS: Added to vector: mission %u required_level: %u required_item: %u required_count: %u chance: %u",
				b.bMission, b.bRequiredLevel, b.iRequiredItem, b.wRequiredItemCount, b.bChance);

			m_vec_BiologMissions.push_back(b);
		}
	}
	return true;
}

bool CClientManager::InitializeBiologRewards()
{
	MYSQL_ROW data;
	const char szQuery[] = "SELECT mission, apply_type+0, apply_value FROM `player`.biolog_rewards ORDER by mission;";
	std::unique_ptr<SQLMsg> pMsg(DIRECT_QUERY(szQuery));

	if (pMsg->uiSQLErrno != 0)
	{
		sys_err("CANNOT LOAD biolog_rewards TABLE , errorcode %d ", pMsg->uiSQLErrno);
		return false;
	}

	if (!m_vec_BiologRewards.empty())
	{
		sys_log(0, "RELOAD: biolog_missions upgrade");
		m_vec_BiologRewards.clear();
	}

	if (pMsg->Get())
	{
		sys_log(0, "BIOLOG_REWARDS: Table size is %u", pMsg->Get()->uiNumRows);

		while ((data = mysql_fetch_row(pMsg->Get()->pSQLResult)))
		{
			TBiologRewardsProto b;
			memset(&b, 0, sizeof(TBiologRewardsProto));

			int col = 0;

			str_to_number(b.bMission, data[col++]);
			str_to_number(b.bApplyType, data[col++]);
			str_to_number(b.lApplyValue, data[col++]);

			sys_log(0, "BIOLOG_REWARDS: Added to vector: mission %u apply_type: %u aply_value: %u",
				b.bMission, b.bApplyType, b.lApplyValue);

			m_vec_BiologRewards.push_back(b);
		}
	}
	return true;
}

bool CClientManager::InitializeBiologMonsters()
{
	MYSQL_ROW data;
	const char szQuery[] = "SELECT `mission`, `mob_vnum`, `chance` FROM `player`.biolog_monsters ORDER by mission;";
	std::unique_ptr<SQLMsg> pMsg(DIRECT_QUERY(szQuery));

	if (pMsg->uiSQLErrno != 0)
	{
		sys_err("CANNOT LOAD biolog_monsters TABLE , errorcode %d ", pMsg->uiSQLErrno);
		return false;
	}

	if (!m_vec_BiologMonsters.empty())
	{
		sys_log(0, "RELOAD: biolog_monsters upgrade");
		m_vec_BiologMonsters.clear();
	}

	if (pMsg->Get())
	{
		sys_log(0, "BIOLOG_MONSTERS: Table size is %u", pMsg->Get()->uiNumRows);

		while ((data = mysql_fetch_row(pMsg->Get()->pSQLResult)))
		{
			TBiologMonstersProto b;
			memset(&b, 0, sizeof(TBiologMonstersProto));

			int col = 0;

			str_to_number(b.bMission, data[col++]);
			str_to_number(b.dwMonsterVnum, data[col++]);
			str_to_number(b.bChance, data[col++]);

			sys_log(0, "BIOLOG_MONSTERS: Added to vector: mission: %u monster_vnum: %u chance: %u ",
				b.bMission, b.dwMonsterVnum, b.bChance);

			m_vec_BiologMonsters.push_back(b);
		}
	}
	return true;
}
#endif
