#pragma once
// #define ENABLE_NEW_MOB_PROTO_STRUCT_20141125	// bleeding resistance 2014/11/25
// #define ENABLE_NEW_MOB_PROTO_STRUCT_20151020	// claw resistance 2015/10/20

/*
 *	NPC 데이터 프로토 타잎을 관리 한다.
 */
#ifdef INGAME_WIKI
	#include "../GameLib/InGameWiki.h"
#endif
class CPythonNonPlayer : public CSingleton<CPythonNonPlayer>
{
	public:
		enum  EClickEvent
		{
			ON_CLICK_EVENT_NONE		= 0,
			ON_CLICK_EVENT_BATTLE	= 1,
			ON_CLICK_EVENT_SHOP		= 2,
			ON_CLICK_EVENT_TALK		= 3,
			ON_CLICK_EVENT_VEHICLE	= 4,

			ON_CLICK_EVENT_MAX_NUM,
		};

#ifdef INGAME_WIKI
		enum EMobTypes
		{
			MONSTER,
			NPC,
			STONE,
			WARP,
			DOOR,
			BUILDING,
			PC,
			POLYMORPH_PC,
			HORSE,
			GOTO
		};
#endif

#if defined(WJ_SHOW_MOB_INFO) && defined(ENABLE_SHOW_MOBAIFLAG)
		enum EAIFlags
		{
			AIFLAG_AGGRESSIVE	= (1 << 0),
			AIFLAG_NOMOVE	= (1 << 1),
			AIFLAG_COWARD	= (1 << 2),
			AIFLAG_NOATTACKSHINSU	= (1 << 3),
			AIFLAG_NOATTACKJINNO	= (1 << 4),
			AIFLAG_NOATTACKCHUNJO	= (1 << 5),
			AIFLAG_ATTACKMOB = (1 << 6 ),
			AIFLAG_BERSERK	= (1 << 7),
			AIFLAG_STONESKIN	= (1 << 8),
			AIFLAG_GODSPEED	= (1 << 9),
			AIFLAG_DEATHBLOW	= (1 << 10),
			AIFLAG_REVIVE		= (1 << 11),
		};
#endif

		enum EMobEnchants
		{
			MOB_ENCHANT_CURSE,
			MOB_ENCHANT_SLOW,
			MOB_ENCHANT_POISON,
			MOB_ENCHANT_STUN,
			MOB_ENCHANT_CRITICAL,
			MOB_ENCHANT_PENETRATE,
			MOB_ENCHANTS_MAX_NUM
		};
		enum EMobRank
		{
			MOB_RANK_PAWN,
			MOB_RANK_S_PAWN,
			MOB_RANK_KNIGHT,
			MOB_RANK_S_KNIGHT,
			MOB_RANK_BOSS,
			MOB_RANK_KING,
			MOB_RANK_MAX_NUM
		};
		enum EMobResists
		{
			MOB_RESIST_SWORD,
			MOB_RESIST_TWOHAND,
			MOB_RESIST_DAGGER,
			MOB_RESIST_BELL,
			MOB_RESIST_FAN,
			MOB_RESIST_BOW,
			MOB_RESIST_FIRE,
			MOB_RESIST_ELECT,
			MOB_RESIST_MAGIC,
			MOB_RESIST_WIND,
			MOB_RESIST_POISON,
			MOB_RESISTS_MAX_NUM
		};
#ifdef INGAME_WIKI
		enum ERaceFlags
		{
			RACE_FLAG_ANIMAL = (1 << 0),
			RACE_FLAG_UNDEAD = (1 << 1),
			RACE_FLAG_DEVIL = (1 << 2),
			RACE_FLAG_HUMAN = (1 << 3),
			RACE_FLAG_ORC = (1 << 4),
			RACE_FLAG_MILGYO = (1 << 5),
			RACE_FLAG_INSECT = (1 << 6),
			RACE_FLAG_FIRE = (1 << 7),
			RACE_FLAG_ICE = (1 << 8),
			RACE_FLAG_DESERT = (1 << 9),
			RACE_FLAG_TREE = (1 << 10),
			RACE_FLAG_ATT_ELEC = (1 << 11),
			RACE_FLAG_ATT_FIRE = (1 << 12),
			RACE_FLAG_ATT_ICE = (1 << 13),
			RACE_FLAG_ATT_WIND = (1 << 14),
			RACE_FLAG_ATT_EARTH = (1 << 15),
			RACE_FLAG_ATT_DARK = (1 << 16),

			RACE_FLAG_MAX_NUM = 17,
		};
#endif
		#define MOB_ATTRIBUTE_MAX_NUM	12
		#define MOB_SKILL_MAX_NUM		5

#pragma pack(push)
#pragma pack(1)
		typedef struct SMobSkillLevel
		{
			DWORD       dwVnum;
			BYTE        bLevel;
		} TMobSkillLevel;

		typedef struct SMobTable
		{
#ifdef INGAME_WIKI
			SMobTable() = default;
			~SMobTable() = default;
#endif

			DWORD       dwVnum;
			char        szName[CHARACTER_NAME_MAX_LEN + 1];
			char        szLocaleName[CHARACTER_NAME_MAX_LEN + 1];

			BYTE        bType;                  // Monster, NPC
			BYTE        bRank;                  // PAWN, KNIGHT, KING
			BYTE        bBattleType;            // MELEE, etc..
			BYTE        bLevel;                 // Level
#ifdef ENABLE_NEW_MOB_PROTO_STRUCT_20151020
			BYTE		bLvlPct;
#endif
			BYTE        bSize;

			DWORD       dwGoldMin;
			DWORD       dwGoldMax;
			DWORD       dwExp;
			DWORD       dwMaxHP;
			BYTE        bRegenCycle;
			BYTE        bRegenPercent;
			WORD        wDef;

			DWORD       dwAIFlag;
			DWORD       dwRaceFlag;
			DWORD       dwImmuneFlag;

			BYTE        bStr, bDex, bCon, bInt;
			DWORD       dwDamageRange[2];

			short       sAttackSpeed;
			short       sMovingSpeed;
			BYTE        bAggresiveHPPct;
			WORD        wAggressiveSight;
			WORD        wAttackRange;

			char        cEnchants[MOB_ENCHANTS_MAX_NUM];
			char        cResists[MOB_RESISTS_MAX_NUM];

			DWORD       dwResurrectionVnum;
			DWORD       dwDropItemVnum;

			BYTE        bMountCapacity;
			BYTE        bOnClickType;

			BYTE        bEmpire;
			char        szFolder[64 + 1];
			float       fDamMultiply;
			DWORD       dwSummonVnum;
			DWORD       dwDrainSP;
			DWORD		dwMonsterColor;
		    DWORD       dwPolymorphItemVnum;

			TMobSkillLevel	Skills[MOB_SKILL_MAX_NUM];

		    BYTE		bBerserkPoint;
			BYTE		bStoneSkinPoint;
			BYTE		bGodSpeedPoint;
			BYTE		bDeathBlowPoint;
			BYTE		bRevivePoint;

#ifdef ENABLE_NEW_MOB_PROTO_STRUCT_20151020
			DWORD		dwHealerPoint;
#endif
		} TMobTable;
#pragma pack(pop)


#ifdef INGAME_WIKI
		typedef struct SWikiInfoTable
		{
			~SWikiInfoTable() = default;
			SWikiInfoTable() {
				isSet = false;
				isFiltered = false;
				
				dropList.clear();
				mobTable = nullptr;
			}
			
			bool isSet;
			bool isFiltered;
			
			std::vector<CommonWikiData::TWikiMobDropInfo> dropList;
			std::unique_ptr<TMobTable> mobTable;
		} TWikiInfoTable;
		
		typedef std::map<DWORD, TWikiInfoTable> TNonPlayerDataMap;
#else
		typedef std::map<DWORD, TMobTable*> TNonPlayerDataMap;
#endif

	public:
		CPythonNonPlayer(void);
		virtual ~CPythonNonPlayer(void);

		void Clear();
		void Destroy();

		bool				LoadNonPlayerData(const char * c_szFileName);

		const TMobTable *	GetTable(DWORD dwVnum);
#ifdef INGAME_WIKI
		TWikiInfoTable*						GetWikiTable(DWORD dwVnum);
		bool								CanRenderMonsterModel(DWORD dwMonsterVnum);
		size_t								WikiLoadClassMobs(BYTE bType, unsigned short fromLvl, unsigned short toLvl);
		void								WikiSetBlacklisted(DWORD vnum);
		void								BuildWikiSearchList();
		std::tuple<const char*, int>	GetMonsterDataByNamePart(const char* namePart);
		std::vector<DWORD>*				WikiGetLastMobs() { return &m_vecTempMob; }
#endif
		bool				GetName(DWORD dwVnum, const char ** c_pszName);
		bool				GetInstanceType(DWORD dwVnum, BYTE* pbType);
		BYTE				GetEventType(DWORD dwVnum);
		BYTE				GetEventTypeByVID(DWORD dwVID);
		DWORD				GetMonsterColor(DWORD dwVnum);
		const char*			GetMonsterName(DWORD dwVnum);
		DWORD				GetMonsterRank(DWORD dwVnum);
#ifdef ENABLE_BOSS_EFFECT
		DWORD GetMonsterType(DWORD dwVnum);
#endif
		// TARGET_INFO
		DWORD				GetMonsterMaxHP(DWORD dwVnum);
		DWORD				GetMonsterRaceFlag(DWORD dwVnum);
		DWORD				GetMonsterLevel(DWORD dwVnum);
		DWORD				GetMonsterDamage1(DWORD dwVnum);
		DWORD				GetMonsterDamage2(DWORD dwVnum);
		DWORD				GetMonsterExp(DWORD dwVnum);
		float				GetMonsterDamageMultiply(DWORD dwVnum);
		DWORD				GetMonsterST(DWORD dwVnum);
		DWORD				GetMonsterDX(DWORD dwVnum);
		bool				IsMonsterStone(DWORD dwVnum);

	protected:
		TNonPlayerDataMap	m_NonPlayerDataMap;
#ifdef INGAME_WIKI
		void								SortMobDataName();
		
		std::vector<DWORD>				m_vecTempMob;
		std::vector<TMobTable*>				m_vecWikiNameSort;
#endif
};
