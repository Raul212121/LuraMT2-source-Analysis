# IN FUNCTION 

size_t CreatePlayerSaveQuery(char * pszQuery, size_t querySize, TPlayerTable * pkTab)
{
	size_t queryLen;

# AFTER

			"horse_stamina = %d, "
			"horse_skill_point = %d, "

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
			"biolog_mission = %d, "
			"biolog_collected = %d, "
			"biolog_cooldown_reminder = %d, "
			"biolog_cooldown = %ld, "
#endif

# AFTER

		pkTab->horse.sStamina,
		pkTab->horse_skill_point

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
		, pkTab->m_BiologActualMission
		, pkTab->m_BiologCollectedItems
		, pkTab->m_BiologCooldownReminder
		, pkTab->m_BiologCooldown
#endif

# BEFORE


				"FROM player%s WHERE id=%d",
				GetTablePostfix(), packet->player_id);

		ClientHandleInfo * pkInfo = new ClientHandleInfo(dwHandle, packet->player_id);
		pkInfo->account_id = packet->account_id;
		CDBManager::instance().ReturnQuery(queryStr, QID_PLAYER, peer->GetHandle(), pkInfo);

# FIND

				"skill_level,quickslot,skill_group,alignment,mobile,horse_level,horse_riding,horse_hp,horse_hp_droptime,horse_stamina,"
				"UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_skill_point "

# AFTER THIS ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
				", biolog_mission "
				", biolog_collected "
				", biolog_cooldown_reminder "
				", biolog_cooldown "
#endif

# AFTER

	str_to_number(pkTab->horse.sStamina, row[col++]);
	str_to_number(pkTab->logoff_interval, row[col++]);
	str_to_number(pkTab->horse_skill_point, row[col++]);

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	str_to_number(pkTab->m_BiologActualMission, row[col++]);
	str_to_number(pkTab->m_BiologCollectedItems, row[col++]);
	str_to_number(pkTab->m_BiologCooldownReminder, row[col++]);
	str_to_number(pkTab->m_BiologCooldown, row[col++]);
#endif