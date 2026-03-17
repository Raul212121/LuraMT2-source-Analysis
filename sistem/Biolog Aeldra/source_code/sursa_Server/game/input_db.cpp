# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	#include "BiologSystemManager.hpp"
#endif


# AFTER

	sys_log(0, "sizeof(TObject) = %d", sizeof(building::TObject));
	//ADMIN_MANAGER
	sys_log(0, "sizeof(TAdminManager) = %d", sizeof (TAdminInfo) );
	//END_ADMIN_MANAGER

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	sys_log(0, "sizeof(TBiologMissionsProto) = %d", sizeof(TBiologMissionsProto));
	sys_log(0, "sizeof(TBiologRewardsProto) = %d", sizeof(TBiologRewardsProto));
	sys_log(0, "sizeof(TBiologMonstersProto) = %d", sizeof(TBiologMonstersProto));
#endif


# AFTER

	CMonarch::instance().SetMonarchInfo(&p);

	for (int n = 1; n < 4; ++n)
	{
		if (p.name[n] && *p.name[n])
			sys_log(0, "[MONARCH] Empire %d Pid %d Money %d %s", n, p.pid[n], p.money[n], p.name[n]);
	}

	int CandidacySize = decode_2bytes(data);
	data += 2;

	int CandidacyCount = decode_2bytes(data);
	data += 2;

	if (test_server)
		sys_log (0, "[MONARCH] Size %d Count %d", CandidacySize, CandidacyCount);

	data += CandidacySize * CandidacyCount;

	//END_MONARCH

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	if (decode_2bytes(data) != sizeof(TBiologMissionsProto))
	{
		sys_err("TBiologMissionsProto table size error");
		thecore_shutdown();
		return;
	}
	data += 2;

	size = decode_2bytes(data);
	data += 2;


	CBiologSystemManager::instance().InitializeMissions((TBiologMissionsProto*)data, size);
	data += size * sizeof(TBiologMissionsProto);

	if (decode_2bytes(data) != sizeof(TBiologRewardsProto))
	{
		sys_err("TBiologRewardsProto table size error");
		thecore_shutdown();
		return;
	}
	data += 2;

	size = decode_2bytes(data);
	data += 2;

	CBiologSystemManager::instance().InitializeRewards((TBiologRewardsProto*)data, size);
	data += size * sizeof(TBiologRewardsProto);

	if (decode_2bytes(data) != sizeof(TBiologMonstersProto))
	{
		sys_err("TBiologRewardsProto table size error");
		thecore_shutdown();
		return;
	}
	data += 2;

	size = decode_2bytes(data);
	data += 2;

	CBiologSystemManager::instance().InitializeMonsters((TBiologMonstersProto*)data, size);
	data += size * sizeof(TBiologMonstersProto);
#endif
