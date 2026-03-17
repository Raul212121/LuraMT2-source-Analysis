# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
#include "BiologSystemManager.hpp"
#endif

# AT THE BOTTOM ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	protected:
		BYTE	m_BiologActualMission;
		WORD	m_BiologCollectedItems;
		BYTE	m_BiologCooldownReminder;
		long	m_BiologCooldown;

	public:
		CBiologSystem* GetBiologManager() const { return m_pkBiologManager; }

		BYTE	GetBiologMissions() const { return m_BiologActualMission; }
		WORD	GetBiologCollectedItems() const { return m_BiologCollectedItems; }
		BYTE	GetBiologCooldownReminder() const { return m_BiologCooldownReminder; }
		long	GetBiologCooldown() const { return m_BiologCooldown; }

		void	SetBiologMissions(BYTE value) { m_BiologActualMission = value; }
		void	SetBiologCollectedItems(WORD value) { m_BiologCollectedItems = value; }
		void	SetBiologCooldownReminder(BYTE value) { m_BiologCooldownReminder = value; }
		void	SetBiologCooldown(long value) { m_BiologCooldown = value; }

	private:
		CBiologSystem* m_pkBiologManager;
#endif

# BEFORE
};