# AFTER

	bool		InitializeObjectTable();
	bool		InitializeMonarch();

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	bool		InitializeBiologMissions();
	bool		InitializeBiologRewards();
	bool		InitializeBiologMonsters();
#endif

# AFTER

	std::vector<building::TLand>		m_vec_kLandTable;
	std::vector<building::TObjectProto>	m_vec_kObjectProto;
	std::map<DWORD, building::TObject *>	m_map_pkObjectTable;

	std::queue<TPacketGDVCard>		m_queue_vcard;

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	std::vector<TBiologMissionsProto>	m_vec_BiologMissions;
	std::vector<TBiologRewardsProto>	m_vec_BiologRewards;
	std::vector<TBiologMonstersProto>	m_vec_BiologMonsters;
#endif
