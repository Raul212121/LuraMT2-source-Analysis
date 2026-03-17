# IN FUNCTION

void CHARACTER::Initialize()
{

# BEFORE

}

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	m_pkBiologManager = NULL;
#endif


# IN FUNCTION


void CHARACTER::CreatePlayerProto(TPlayerTable & tab)
{

    ..

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	tab.m_BiologActualMission = GetBiologMissions();
	tab.m_BiologCollectedItems = GetBiologCollectedItems();
	tab.m_BiologCooldownReminder = GetBiologCooldownReminder();
	tab.m_BiologCooldown = GetBiologCooldown();
#endif
    
    # BEFORE!!!
}

# IN FUNCTION 

void CHARACTER::Disconnect(const char * c_pszReason)
{

    ...

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	if (m_pkBiologManager)
	{
		delete m_pkBiologManager;
		m_pkBiologManager = NULL;
	}
#endif

# BEFFORE
	m_bSkipSave = true;

	quest::CQuestManager::instance().DisconnectPC(this);

# IN FUNCTION

void CHARACTER::SetPlayerProto(const TPlayerTable * t)
{

    ...

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	if (m_pkBiologManager)
	{
		sys_err("Biolog manager already exist for owner %u %s", GetPlayerID(), GetName());
		delete m_pkBiologManager;
	}

	m_pkBiologManager = M2_NEW CBiologSystem(this);

	SetBiologMissions(t->m_BiologActualMission);
	SetBiologCollectedItems(t->m_BiologCollectedItems);
	SetBiologCooldownReminder(t->m_BiologCooldownReminder);
	SetBiologCooldown(t->m_BiologCooldown);
#endif

# BEFORE
}