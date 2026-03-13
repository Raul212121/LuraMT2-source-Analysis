#pragma once
#define EVENT_MAP_INDEX 159
typedef struct SEventFind
{

	uint16_t mapIndex, x, y;
	std::string hint;

} TEventFind;

#ifdef ENABLE_EVENT_FIND_NPC
class EventManagerAddons : public singleton<EventManagerAddons>
{
	public:
		EventManagerAddons();
		~EventManagerAddons() override;

		//Initializer
		void BootNPCMap();

		//NPC
		void OnTriggerEvent();
		void OnTriggerNPC(LPCHARACTER pkNpc, LPCHARACTER pkChr);

		void HandleSpawning();
		void ClearEvent();

		auto GetEventNpc() const { return m_pkNPC; }
		auto GetEventStatus() const { return isEventEnabled; }

		//BOSS
		void ClearEventBoss();

		void OnTriggerBossEvent(bool status = false);
		void OnEnterMap(LPCHARACTER pkChar) const;

		auto GetEventStatusBoss() const { return isEventEnabledBoss; }

		auto GetEventMapIndex() const { return EVENT_MAP_INDEX; }

	private:
		std::vector<TEventFind> npcFinderMap;
		std::vector<TEventFind> npcFinderTriggerMap;

		bool isEventEnabled{};
		bool isEventEnabledBoss{};
		int8_t spawnStage{};

		LPCHARACTER m_pkNPC{};
};
#endif
