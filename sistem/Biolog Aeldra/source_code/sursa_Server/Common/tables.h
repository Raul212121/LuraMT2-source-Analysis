# ADD BEFORE } TPlayerTable;

#ifdef __ENABLE_BIOLOG_SYSTEM__
	BYTE	m_BiologActualMission;
	WORD	m_BiologCollectedItems;
	BYTE	m_BiologCooldownReminder;
	long	m_BiologCooldown;
#endif


# ADD AT THE BOTTOM OF FILE BEFOOOOORE #pragma pack()

#ifdef __ENABLE_BIOLOG_SYSTEM__
typedef struct SBiologMissions
{
	BYTE	bMission;
	BYTE	bRequiredLevel;
	DWORD	iRequiredItem;
	WORD	wRequiredItemCount;
	time_t	iCooldown;
	BYTE	bChance;
} TBiologMissionsProto;

typedef struct SBiologRewards
{
	BYTE	bMission;
	DWORD	bApplyType;
	long	lApplyValue;
} TBiologRewardsProto;

typedef struct SBiologMonsters
{
	BYTE	bMission;
	DWORD	dwMonsterVnum;
	BYTE	bChance;
} TBiologMonstersProto;
#endif
