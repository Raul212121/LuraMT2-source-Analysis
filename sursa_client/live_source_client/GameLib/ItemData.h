#pragma once

// NOTE : Item의 통합 관리 클래스다.
//        Icon, Model (droped on ground), Game Data

#include "../eterLib/GrpSubImage.h"
#include "../eterGrnLib/Thing.h"
#include "GameLibDefines.h"
#include "../UserInterface/Locale_inc.h"
#ifdef INGAME_WIKI
	#include "InGameWiki.h"
#endif

// #define ENABLE_NEW_ITEM_PROTO_STRUCT_20160129

class CItemData
{
	public:
		enum 
		{
			ITEM_NAME_MAX_LEN = 24,
			ITEM_LIMIT_MAX_NUM = 2,
			ITEM_VALUES_MAX_NUM = 6,
			ITEM_SMALL_DESCR_MAX_LEN = 256,
			ITEM_APPLY_MAX_NUM = 3,
			ITEM_SOCKET_MAX_NUM = 3,
            ITEM_SHINE_MAX_NUM = 3,
		};

		enum EItemType
		{
			ITEM_TYPE_NONE,					//0
			ITEM_TYPE_WEAPON,				//1//무기
			ITEM_TYPE_ARMOR,				//2//갑옷
			ITEM_TYPE_USE,					//3//아이템 사용
			ITEM_TYPE_AUTOUSE,				//4
			ITEM_TYPE_MATERIAL,				//5
			ITEM_TYPE_SPECIAL,				//6 //스페셜 아이템
			ITEM_TYPE_TOOL,					//7
			ITEM_TYPE_LOTTERY,				//8//복권
			ITEM_TYPE_ELK,					//9//돈
			ITEM_TYPE_METIN,				//10
			ITEM_TYPE_CONTAINER,			//11
			ITEM_TYPE_FISH,					//12//낚시
			ITEM_TYPE_ROD,					//13
			ITEM_TYPE_RESOURCE,				//14
			ITEM_TYPE_CAMPFIRE,				//15
			ITEM_TYPE_UNIQUE,				//16
			ITEM_TYPE_SKILLBOOK,			//17
			ITEM_TYPE_QUEST,				//18
			ITEM_TYPE_POLYMORPH,			//19
			ITEM_TYPE_TREASURE_BOX,			//20//보물상자
			ITEM_TYPE_TREASURE_KEY,			//21//보물상자 열쇠
			ITEM_TYPE_SKILLFORGET,			//22
			ITEM_TYPE_GIFTBOX,				//23
			ITEM_TYPE_PICK,					//24
			ITEM_TYPE_HAIR,					//25//머리
			ITEM_TYPE_TOTEM,				//26//토템
			ITEM_TYPE_BLEND,				//27//생성될때 랜덤하게 속성이 붙는 약물
			ITEM_TYPE_COSTUME,				//28//코스츔 아이템 (2011년 8월 추가된 코스츔 시스템용 아이템)
			ITEM_TYPE_DS,					//29 //용혼석
			ITEM_TYPE_SPECIAL_DS,			//30 // 특수한 용혼석 (DS_SLOT에 착용하는 UNIQUE 아이템이라 생각하면 됨)
			ITEM_TYPE_EXTRACT,					//31 추출도구.
			ITEM_TYPE_SECONDARY_COIN,			//32 명도전.
			ITEM_TYPE_RING,						//33 반지 (유니크 슬롯이 아닌 순수 반지 슬롯)
			ITEM_TYPE_BELT,						//34 벨트

			ITEM_TYPE_MAX_NUM,
		};

		enum EWeaponSubTypes
		{
			WEAPON_SWORD = 0,
			WEAPON_DAGGER = 1,	//이도류
			WEAPON_BOW = 2,
			WEAPON_TWO_HANDED = 3,
			WEAPON_BELL = 4,
			WEAPON_FAN = 5,
			WEAPON_ARROW = 6,
			WEAPON_MOUNT_SPEAR = 7,
			WEAPON_QUIVER = 8,
			WEAPON_NUM_TYPES,

			WEAPON_NONE = WEAPON_NUM_TYPES+1,
		};

		enum EMaterialSubTypes
		{
			MATERIAL_LEATHER,
			MATERIAL_BLOOD,
			MATERIAL_ROOT,
			MATERIAL_NEEDLE,
			MATERIAL_JEWEL,
			MATERIAL_DS_REFINE_NORMAL,
			MATERIAL_DS_REFINE_BLESSED,
			MATERIAL_DS_REFINE_HOLLY,
		};

		enum EArmorSubTypes
		{
			ARMOR_BODY,
			ARMOR_HEAD,
			ARMOR_SHIELD,
			ARMOR_WRIST,
			ARMOR_FOOTS,
		    ARMOR_NECK,
			ARMOR_EAR,
			ARMOR_NUM_TYPES
		};

		enum ECostumeSubTypes
		{
			COSTUME_BODY,				//0	갑옷(main look)
			COSTUME_HAIR,				//1	헤어(탈착가능)
#ifdef ENABLE_MOUNT_COSTUME_SYSTEM
			COSTUME_MOUNT,
#endif
#ifdef ENABLE_WEAPON_COSTUME_SYSTEM
			COSTUME_WEAPON,
#endif
#ifdef ENABLE_PET_COSTUME_SYSTEM
			COSTUME_PET,
#endif
			COSTUME_NUM_TYPES,
		};

		enum EUseSubTypes
		{
			USE_POTION,					// 0
			USE_TALISMAN,
			USE_TUNING,
			USE_MOVE,
			USE_TREASURE_BOX,
			USE_MONEYBAG,
			USE_BAIT,
			USE_ABILITY_UP,
			USE_AFFECT,
			USE_CREATE_STONE,
			USE_SPECIAL,				// 10
			USE_POTION_NODELAY,
			USE_CLEAR,
			USE_INVISIBILITY,
			USE_DETACHMENT,
			USE_BUCKET,
			USE_POTION_CONTINUE,
			USE_CLEAN_SOCKET,
			USE_CHANGE_ATTRIBUTE,
			USE_ADD_ATTRIBUTE,
			USE_ADD_ACCESSORY_SOCKET,	// 20
			USE_PUT_INTO_ACCESSORY_SOCKET,
			USE_ADD_ATTRIBUTE2,
			USE_RECIPE,
			USE_CHANGE_ATTRIBUTE2,
			USE_BIND,
			USE_UNBIND,
			USE_TIME_CHARGE_PER,
			USE_TIME_CHARGE_FIX,	
			USE_PUT_INTO_BELT_SOCKET,
			USE_PUT_INTO_RING_SOCKET,
#ifdef ENABLE_EXTEND_COSTUME_TIME
			USE_EXTEND_TIME,
#endif
		};

#if defined(ENABLE_COSTUME_EXTENDED_RECHARGE)
		enum EDuration
		{
			MIN_INFINITE_DURATION = 100 * 24 * 60 * 60, // 100 zile
			MAX_INFINITE_DURATION = 60 * 365 * 24 * 60 * 60, // 21900 zile
			MAX_SHOW_DURATION = 60 * 365 * 24 * 60,
		};
#endif
		enum EDragonSoulSubType
		{
			DS_SLOT1,
			DS_SLOT2,
			DS_SLOT3,
			DS_SLOT4,
			DS_SLOT5,
			DS_SLOT6,
			DS_SLOT_NUM_TYPES = 6,
		};

		enum EMetinSubTypes
		{
			METIN_NORMAL,
			METIN_GOLD,
		};

		enum ELimitTypes
		{
			LIMIT_NONE,

			LIMIT_LEVEL,
			LIMIT_STR,
			LIMIT_DEX,
			LIMIT_INT,
			LIMIT_CON,
			LIMIT_REAL_TIME,
			LIMIT_REAL_TIME_START_FIRST_USE,
			LIMIT_TIMER_BASED_ON_WEAR,

			LIMIT_MAX_NUM
		};

		enum EItemAntiFlag
		{
			ITEM_ANTIFLAG_FEMALE        = (1 << 0),		// 여성 사용 불가
			ITEM_ANTIFLAG_MALE          = (1 << 1),		// 남성 사용 불가
			ITEM_ANTIFLAG_WARRIOR       = (1 << 2),		// 무사 사용 불가
			ITEM_ANTIFLAG_ASSASSIN      = (1 << 3),		// 자객 사용 불가
			ITEM_ANTIFLAG_SURA          = (1 << 4),		// 수라 사용 불가
			ITEM_ANTIFLAG_SHAMAN        = (1 << 5),		// 무당 사용 불가
			ITEM_ANTIFLAG_GET           = (1 << 6),		// 집을 수 없음
			ITEM_ANTIFLAG_DROP          = (1 << 7),		// 버릴 수 없음
			ITEM_ANTIFLAG_SELL          = (1 << 8),		// 팔 수 없음
			ITEM_ANTIFLAG_EMPIRE_A      = (1 << 9),		// A 제국 사용 불가
			ITEM_ANTIFLAG_EMPIRE_B      = (1 << 10),	// B 제국 사용 불가
			ITEM_ANTIFLAG_EMPIRE_R      = (1 << 11),	// C 제국 사용 불가
			ITEM_ANTIFLAG_SAVE          = (1 << 12),	// 저장되지 않음
			ITEM_ANTIFLAG_GIVE          = (1 << 13),	// 거래 불가
			ITEM_ANTIFLAG_PKDROP        = (1 << 14),	// PK시 떨어지지 않음
			ITEM_ANTIFLAG_STACK         = (1 << 15),	// 합칠 수 없음
			ITEM_ANTIFLAG_MYSHOP        = (1 << 16),	// 개인 상점에 올릴 수 없음
			ITEM_ANTIFLAG_SAFEBOX		= (1 << 17),
		};

		enum EItemFlag
		{
			ITEM_FLAG_REFINEABLE        = (1 << 0),		// 개량 가능
			ITEM_FLAG_SAVE              = (1 << 1),
			ITEM_FLAG_STACKABLE         = (1 << 2),     // 여러개 합칠 수 있음
			ITEM_FLAG_COUNT_PER_1GOLD   = (1 << 3),		// 가격이 개수 / 가격으로 변함
			ITEM_FLAG_SLOW_QUERY        = (1 << 4),		// 게임 종료시에만 SQL에 쿼리함
			ITEM_FLAG_RARE              = (1 << 5),
			ITEM_FLAG_UNIQUE            = (1 << 6),
			ITEM_FLAG_MAKECOUNT			= (1 << 7),
			ITEM_FLAG_IRREMOVABLE		= (1 << 8),
			ITEM_FLAG_CONFIRM_WHEN_USE	= (1 << 9),
			ITEM_FLAG_QUEST_USE         = (1 << 10),    // 퀘스트 스크립트 돌리는지?
			ITEM_FLAG_QUEST_USE_MULTIPLE= (1 << 11),    // 퀘스트 스크립트 돌리는지?
			ITEM_FLAG_UNUSED03          = (1 << 12),    // UNUSED03
			ITEM_FLAG_LOG               = (1 << 13),    // 사용시 로그를 남기는 아이템인가?
			ITEM_FLAG_APPLICABLE		= (1 << 14),
		};

		enum EWearPositions
		{
			WEAR_BODY,          // 0
			WEAR_HEAD,          // 1
			WEAR_FOOTS,         // 2
			WEAR_WRIST,         // 3
			WEAR_WEAPON,        // 4
			WEAR_NECK,          // 5
			WEAR_EAR,           // 6
			WEAR_UNIQUE1,       // 7
			WEAR_UNIQUE2,       // 8
			WEAR_ARROW,         // 9
			WEAR_SHIELD,        // 10
			WEAR_ABILITY1,  // 11
			WEAR_ABILITY2,  // 12
			WEAR_ABILITY3,  // 13
			WEAR_ABILITY4,  // 14
			WEAR_ABILITY5,  // 15
			WEAR_ABILITY6,  // 16
			WEAR_ABILITY7,  // 17
			WEAR_ABILITY8,  // 18
			WEAR_COSTUME_BODY,	// 19
			WEAR_COSTUME_HAIR,	// 20
#ifdef ENABLE_MOUNT_COSTUME_SYSTEM
			WEAR_COSTUME_MOUNT, // 24
#endif
#ifdef ENABLE_WEAPON_COSTUME_SYSTEM
			WEAR_COSTUME_WEAPON,// 24
#endif
			WEAR_RING1,			// 21	: 신규 반지슬롯1 (왼쪽)
			WEAR_RING2,			// 22	: 신규 반지슬롯2 (오른쪽)
			WEAR_BELT,			// 23	: 신규 벨트슬롯

#ifdef ENABLE_PET_COSTUME_SYSTEM
			WEAR_COSTUME_PET,
#endif

			WEAR_MAX_NUM = 32,
		};

		enum EItemWearableFlag
		{
			WEARABLE_BODY       = (1 << 0),
			WEARABLE_HEAD       = (1 << 1),
			WEARABLE_FOOTS      = (1 << 2),
			WEARABLE_WRIST      = (1 << 3),
			WEARABLE_WEAPON     = (1 << 4),
			WEARABLE_NECK       = (1 << 5),
			WEARABLE_EAR        = (1 << 6),
			WEARABLE_UNIQUE     = (1 << 7),
			WEARABLE_SHIELD     = (1 << 8),
			WEARABLE_ARROW      = (1 << 9),
			WEARABLE_HAIR		= (1 << 10),
			WEARABLE_ABILITY		= (1 << 11),
			WEARABLE_COSTUME_BODY = (1 << 12),
			WEARABLE_COSTUME_HAIR	= (1 << 13),
#ifdef ENABLE_MOUNT_COSTUME_SYSTEM
			WEARABLE_COSTUME_MOUNT = (1 << 14),
#endif
#ifdef ENABLE_PET_COSTUME_SYSTEM
			WEARABLE_COSTUME_PET = (1 << 15),
#endif
		};

		enum EApplyTypes
		{
			APPLY_NONE,                 // 0
			APPLY_MAX_HP,               // 1
			APPLY_MAX_SP,               // 2
			APPLY_CON,                  // 3
			APPLY_INT,                  // 4
			APPLY_STR,                  // 5
			APPLY_DEX,                  // 6
			APPLY_ATT_SPEED,            // 7
			APPLY_MOV_SPEED,            // 8
			APPLY_CAST_SPEED,           // 9
			APPLY_HP_REGEN,             // 10
			APPLY_SP_REGEN,             // 11
			APPLY_POISON_PCT,           // 12
			APPLY_STUN_PCT,             // 13
			APPLY_SLOW_PCT,             // 14
			APPLY_CRITICAL_PCT,         // 15
			APPLY_PENETRATE_PCT,        // 16
			APPLY_ATTBONUS_HUMAN,       // 17
			APPLY_ATTBONUS_ANIMAL,      // 18
			APPLY_ATTBONUS_ORC,         // 19
			APPLY_ATTBONUS_MILGYO,      // 20
			APPLY_ATTBONUS_UNDEAD,      // 21
			APPLY_ATTBONUS_DEVIL,       // 22
			APPLY_STEAL_HP,             // 23
			APPLY_STEAL_SP,             // 24
			APPLY_MANA_BURN_PCT,        // 25
			APPLY_DAMAGE_SP_RECOVER,    // 26
			APPLY_BLOCK,                // 27
			APPLY_DODGE,                // 28
			APPLY_RESIST_SWORD,         // 29
			APPLY_RESIST_TWOHAND,       // 30
			APPLY_RESIST_DAGGER,        // 31
			APPLY_RESIST_BELL,          // 32
			APPLY_RESIST_FAN,           // 33
			APPLY_RESIST_BOW,           // 34
			APPLY_RESIST_FIRE,          // 35
			APPLY_RESIST_ELEC,          // 36
			APPLY_RESIST_MAGIC,         // 37
			APPLY_RESIST_WIND,          // 38
			APPLY_REFLECT_MELEE,        // 39
			APPLY_REFLECT_CURSE,        // 40
			APPLY_POISON_REDUCE,        // 41
			APPLY_KILL_SP_RECOVER,      // 42
			APPLY_EXP_DOUBLE_BONUS,     // 43
			APPLY_GOLD_DOUBLE_BONUS,    // 44
			APPLY_ITEM_DROP_BONUS,      // 45
			APPLY_POTION_BONUS,         // 46
			APPLY_KILL_HP_RECOVER,      // 47
			APPLY_IMMUNE_STUN,          // 48
			APPLY_IMMUNE_SLOW,          // 49
			APPLY_IMMUNE_FALL,          // 50
			APPLY_SKILL,                // 51
			APPLY_BOW_DISTANCE,         // 52
			APPLY_ATT_GRADE_BONUS,      // 53
			APPLY_DEF_GRADE_BONUS,      // 54
			APPLY_MAGIC_ATT_GRADE,      // 55
			APPLY_MAGIC_DEF_GRADE,      // 56
			APPLY_CURSE_PCT,            // 57
			APPLY_MAX_STAMINA,			// 58
			APPLY_ATT_BONUS_TO_WARRIOR, // 59
			APPLY_ATT_BONUS_TO_ASSASSIN,// 60
			APPLY_ATT_BONUS_TO_SURA,    // 61
			APPLY_ATT_BONUS_TO_SHAMAN,  // 62
			APPLY_ATT_BONUS_TO_MONSTER, // 63
			APPLY_MALL_ATTBONUS,        // 64 
			APPLY_MALL_DEFBONUS,        // 65 
			APPLY_MALL_EXPBONUS,        // 66 
			APPLY_MALL_ITEMBONUS,       // 67 
			APPLY_MALL_GOLDBONUS,       // 68 
			APPLY_MAX_HP_PCT,           // 69 
			APPLY_MAX_SP_PCT,           // 70 
			APPLY_SKILL_DAMAGE_BONUS,   // 71 
			APPLY_NORMAL_HIT_DAMAGE_BONUS,  // 72
			APPLY_SKILL_DEFEND_BONUS,   // 73 
			APPLY_NORMAL_HIT_DEFEND_BONUS,  // 74 
			APPLY_EXTRACT_HP_PCT,		//75
			APPLY_RESIST_WARRIOR,			//76
			APPLY_RESIST_ASSASSIN,			//77
			APPLY_RESIST_SURA,				//78
			APPLY_RESIST_SHAMAN,			//79
			APPLY_ENERGY,					//80
			APPLY_DEF_GRADE,				// 81
			APPLY_COSTUME_ATTR_BONUS,		// 82
			APPLY_MAGIC_ATTBONUS_PER,		// 83
			APPLY_MELEE_MAGIC_ATTBONUS_PER,			// 84

			APPLY_RESIST_ICE,		// 85
			APPLY_RESIST_EARTH,		// 86
			APPLY_RESIST_DARK,		// 87

			APPLY_ANTI_CRITICAL_PCT,	// 88
			APPLY_ANTI_PENETRATE_PCT,	// 89

			APPLY_RESIST_MONSTER,
            APPLY_RESIST_HUMAN,
			MAX_APPLY_NUM,              //
		};

		enum EImmuneFlags
		{
			IMMUNE_PARA         = (1 << 0),
			IMMUNE_CURSE        = (1 << 1),
			IMMUNE_STUN         = (1 << 2),
			IMMUNE_SLEEP        = (1 << 3),
			IMMUNE_SLOW         = (1 << 4),
			IMMUNE_POISON       = (1 << 5),
			IMMUNE_TERROR       = (1 << 6),
#ifdef INGAME_WIKI
			IMMUNE_FLAG_MAX_NUM = 7
#endif
		};

#pragma pack(push)
#pragma pack(1)
		typedef struct SItemLimit
		{
			BYTE        bType;
			long        lValue;
		} TItemLimit;

		typedef struct SItemApply
		{
			BYTE        bType;
			long        lValue;
		} TItemApply;

		typedef struct SItemTable
		{
			DWORD       dwVnum;
			DWORD       dwVnumRange;
			char        szName[ITEM_NAME_MAX_LEN + 1];
			char        szLocaleName[ITEM_NAME_MAX_LEN + 1];
			BYTE        bType;
			BYTE        bSubType;

			BYTE        bWeight;
			BYTE        bSize;

			DWORD       dwAntiFlags;
			DWORD       dwFlags;
			DWORD       dwWearFlags;
			DWORD       dwImmuneFlag;

			DWORD       dwIBuyItemPrice;
			DWORD		dwISellItemPrice;

			TItemLimit  aLimits[ITEM_LIMIT_MAX_NUM];
			TItemApply  aApplies[ITEM_APPLY_MAX_NUM];
			long        alValues[ITEM_VALUES_MAX_NUM];
			long        alSockets[ITEM_SOCKET_MAX_NUM];
			DWORD       dwRefinedVnum;
			WORD		wRefineSet;
			BYTE        bAlterToMagicItemPct;
			BYTE		bSpecular;
			BYTE        bGainSocketPct;
#ifdef ENABLE_NEW_ITEM_PROTO_STRUCT_20160129
			WORD		wWearableFlag;
#endif
		} TItemTable;

#pragma pack(pop)

	public:
		CItemData();
		virtual ~CItemData();

		void Clear();
		void SetSummary(const std::string& c_rstSumm);
		void SetDescription(const std::string& c_rstDesc);

		CGraphicThing * GetModelThing();
		CGraphicThing * GetSubModelThing();
		CGraphicThing * GetDropModelThing();
		CGraphicSubImage * GetIconImage();
#ifdef ENABLE_EASTER_EVENT
		CGraphicSubImage* GetIconImageFileName(const char* c_szFileName);
#endif
		DWORD GetLODModelThingCount();
		BOOL GetLODModelThingPointer(DWORD dwIndex, CGraphicThing ** ppModelThing);

		DWORD GetAttachingDataCount();
		BOOL GetCollisionDataPointer(DWORD dwIndex, const NRaceData::TAttachingData ** c_ppAttachingData);
		BOOL GetAttachingDataPointer(DWORD dwIndex, const NRaceData::TAttachingData ** c_ppAttachingData);

		/////
		const TItemTable*	GetTable() const;
		DWORD GetIndex() const;
		const char * GetName() const;
		const char * GetDescription() const;
		const char * GetSummary() const;
		BYTE GetType() const;
		BYTE GetSubType() const;
		UINT GetRefine() const;
		const char* GetUseTypeString() const;
		DWORD GetWeaponType() const;
		BYTE GetSize() const;
		BOOL IsAntiFlag(DWORD dwFlag) const;
		BOOL IsFlag(DWORD dwFlag) const;
		BOOL IsWearableFlag(DWORD dwFlag) const;
		BOOL HasNextGrade() const;
		DWORD GetWearFlags() const;
		DWORD GetIBuyItemPrice() const;
		DWORD GetISellItemPrice() const;
		BOOL GetLimit(BYTE byIndex, TItemLimit * pItemLimit) const;
		BOOL GetApply(BYTE byIndex, TItemApply * pItemApply) const;
		long GetValue(BYTE byIndex) const;
		long GetSocket(BYTE byIndex) const;
		long SetSocket(BYTE byIndex,DWORD value);
		int GetSocketCount() const;
		DWORD GetIconNumber() const;
#ifdef INGAME_WIKI
		DWORD GetRefinedVnum() const { return m_ItemTable.dwRefinedVnum; }
#endif

#ifdef INGAME_WIKI
	public:
		typedef struct SWikiItemInfo
		{
			~SWikiItemInfo() = default;
			SWikiItemInfo() {
				isSet = false;
				hasData = false;
				bIsCommon = false;
				
				dwOrigin = 0;
				maxRefineLevel = CommonWikiData::MAX_REFINE_COUNT;
				
				pRefineData.clear();
				pChestInfo.clear();
				pOriginInfo.clear();
			}
			
			bool isSet;
			bool hasData;
			bool bIsCommon;
			
			DWORD dwOrigin;
			int maxRefineLevel;
			
			std::vector<CommonWikiData::TWikiRefineInfo> pRefineData;
			std::vector<CommonWikiData::TWikiChestInfo> pChestInfo;
			std::vector<CommonWikiData::TWikiItemOriginInfo> pOriginInfo;
		} TWikiItemInfo;
		
		bool IsValidImage() { return m_isValidImage; }
		std::string GetIconFileName() { return m_strIconFileName; }
		TWikiItemInfo* GetWikiTable() { return &m_wikiInfo; }
		bool IsBlacklisted() { return m_isBlacklisted; }
		
		void ValidateImage(bool isValidImage) { m_isValidImage = isValidImage; }
		void SetBlacklisted(bool val) { m_isBlacklisted = val; }
	
	protected:
		bool m_isValidImage;
		bool m_isBlacklisted;
	
	private:
		TWikiItemInfo m_wikiInfo;

	public:
#endif
		UINT	GetSpecularPoweru() const;
		float	GetSpecularPowerf() const;

		/////

		BOOL IsEquipment() const;

		/////

		//BOOL LoadItemData(const char * c_szFileName);
		void SetDefaultItemData(const char * c_szIconFileName, const char * c_szModelFileName  = NULL);
		void SetItemTableData(TItemTable * pItemTable);

#ifdef ENABLE_SHINING_SYSTEM
		typedef struct SItemShiningTable {
			char szShinings[ITEM_SHINE_MAX_NUM][256];
		public:
			//Checking if any shining is set for this item.
			bool Any() const
			{
				for (int i = 0; i < CItemData::ITEM_SHINE_MAX_NUM; i++)
				{
					if (strcmp(szShinings[i], ""))
					{
						return true;
					}
				}
				return false;
			}
		} TItemShiningTable;
		void SetItemShiningTableData(BYTE bIndex, const char* szEffectname);
		CItemData::TItemShiningTable GetItemShiningTable() { return m_ItemShiningTable; }
#endif

	protected:
		void __LoadFiles();
		void __SetIconImage(const char * c_szFileName);

	protected:
		std::string m_strModelFileName;
		std::string m_strSubModelFileName;
		std::string m_strDropModelFileName;
		std::string m_strIconFileName;
		std::string m_strDescription;
		std::string m_strSummary;
		std::vector<std::string> m_strLODModelFileNameVector;

		CGraphicThing * m_pModelThing;
		CGraphicThing * m_pSubModelThing;
		CGraphicThing * m_pDropModelThing;
		CGraphicSubImage * m_pIconImage;
		std::vector<CGraphicThing *> m_pLODModelThingVector;

		NRaceData::TAttachingDataVector m_AttachingDataVector;
		DWORD		m_dwVnum;
		TItemTable m_ItemTable;
#ifdef ENABLE_SHINING_SYSTEM
		TItemShiningTable m_ItemShiningTable;
#endif
	public:
		static void DestroySystem();

		static CItemData* New();
		static void Delete(CItemData* pkItemData);

		static CDynamicPool<CItemData>		ms_kPool;
};
