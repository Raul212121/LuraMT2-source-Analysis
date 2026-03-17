# AFTER 

sizeof(WORD) + sizeof(WORD) + sizeof(MonarchCandidacy)* CMonarch::instance().MonarchCandidacySize() +

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
		sizeof(WORD) + sizeof(WORD) + sizeof(TBiologMissionsProto) * m_vec_BiologMissions.size() +
		sizeof(WORD) + sizeof(WORD) + sizeof(TBiologRewardsProto) * m_vec_BiologRewards.size() +
		sizeof(WORD) + sizeof(WORD) + sizeof(TBiologMonstersProto) * m_vec_BiologMonsters.size() +
#endif

# AFTER

sys_log(0, "sizeof(TMonarchInfo) = %d * %d", sizeof(TMonarchInfo));

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	sys_log(0, "sizeof(TBiologMissionsProto) = %d", sizeof(TBiologMissionsProto));
	sys_log(0, "sizeof(TBiologRewardsProto) = %d", sizeof(TBiologRewardsProto));
	sys_log(0, "sizeof(TBiologMonstersProto) = %d", sizeof(TBiologMonstersProto));
#endif

# AFTER

	if (g_test_server)
		sys_log(0, "MONARCHCandidacy Size %d", CMonarch::instance().MonarchCandidacySize());

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	peer->EncodeWORD(sizeof(TBiologMissionsProto));
	peer->EncodeWORD(m_vec_BiologMissions.size());
	peer->Encode(&m_vec_BiologMissions[0], sizeof(TBiologMissionsProto)* m_vec_BiologMissions.size());

	peer->EncodeWORD(sizeof(TBiologRewardsProto));
	peer->EncodeWORD(m_vec_BiologRewards.size());
	peer->Encode(&m_vec_BiologRewards[0], sizeof(TBiologRewardsProto)* m_vec_BiologRewards.size());

	peer->EncodeWORD(sizeof(TBiologMonstersProto));
	peer->EncodeWORD(m_vec_BiologMonsters.size());
	peer->Encode(&m_vec_BiologMonsters[0], sizeof(TBiologMonstersProto)* m_vec_BiologMonsters.size());
#endif
