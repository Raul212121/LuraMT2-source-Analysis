#pragma once

class CWorldBossManager : public singleton<CWorldBossManager>
{
public:
	CWorldBossManager();
	~CWorldBossManager() override;

	void PrepareChecker();

	void Initialize();

	void Destroy();

	void HandleBossEvent(const int day, const int hour, const int minute, const int second);

	void SpawnWorldBossCheck(DWORD dwBoss);
	void OnKillWorldBoss(LPCHARACTER pkBoss);

private:
	LPEVENT m_pkSpawnEvent;
	std::map<DWORD, std::pair<bool, time_t>> m_bossesSpawnClock;
	std::map<DWORD, TBossSpawnData> m_spawnData;
};

