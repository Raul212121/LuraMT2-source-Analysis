#pragma once
#include "../GameLib/ItemData.h"
#include <array>
struct SAffects
{
	enum
	{
		AFFECT_MAX_NUM = 32,
	};

	SAffects() : dwAffects(0) {}
	SAffects(const DWORD & c_rAffects)
	{
		__SetAffects(c_rAffects);
	}
	int operator = (const DWORD & c_rAffects)
	{
		__SetAffects(c_rAffects);
	}

	BOOL IsAffect(BYTE byIndex)
	{
		return dwAffects & (1 << byIndex);
	}

	void __SetAffects(const DWORD & c_rAffects)
	{
		dwAffects = c_rAffects;
	}

	DWORD dwAffects;
};

extern std::string g_strGuildSymbolPathName;

const DWORD c_Name_Max_Length = 64;
const DWORD c_FileName_Max_Length = 128;
const DWORD c_Short_Name_Max_Length = 32;

const DWORD c_Inventory_Page_Size = 5*9; // x*y
const DWORD c_Inventory_Page_Count = 4;
#ifdef ENABLE_SPECIAL_INVENTORY_SYSTEM
const DWORD c_Special_Inventory_Page_Size = 5 * 9;
const DWORD c_Special_Inventory_Page_Count = 3;
const DWORD c_Special_ItemSlot_Count = c_Special_Inventory_Page_Size * c_Special_Inventory_Page_Count;
#endif
const DWORD c_ItemSlot_Count = c_Inventory_Page_Size * c_Inventory_Page_Count;
const DWORD c_Equipment_Count = 12;

const DWORD c_Equipment_Start = c_ItemSlot_Count;

const DWORD c_Equipment_Body	= c_Equipment_Start + 0;
const DWORD c_Equipment_Head	= c_Equipment_Start + 1;
const DWORD c_Equipment_Shoes	= c_Equipment_Start + 2;
const DWORD c_Equipment_Wrist	= c_Equipment_Start + 3;
const DWORD c_Equipment_Weapon	= c_Equipment_Start + 4;
const DWORD c_Equipment_Neck	= c_Equipment_Start + 5;
const DWORD c_Equipment_Ear		= c_Equipment_Start + 6;
const DWORD c_Equipment_Unique1	= c_Equipment_Start + 7;
const DWORD c_Equipment_Unique2	= c_Equipment_Start + 8;
const DWORD c_Equipment_Arrow	= c_Equipment_Start + 9;
const DWORD c_Equipment_Shield	= c_Equipment_Start + 10;

// 새로 추가된 신규 반지 & 벨트
// 장착형 아이템에 할당할 수 있는 위치가 기존 장비, 채기랍 퀘스트 보상, 코스튬 시스템 등으로 인해서 공간이 잘려있다.
// 이게 다 채기랍 보상 버프를 장착아이템처럼 구현한 ㅅㄲ 때문에 난리났따... ㅆㅂ
//
// 정리하면, 기존 장비창들은 서버DB상 아이템 포지션이 90 ~ 102 이고,
// 2013년 초에 새로 추가되는 슬롯들은 111 ~ 부터 시작한다. 착용 장비에서 최대로 사용할 수 있는 값은 121 까지이고, 122부터는 용혼석에서 사용한다.
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	const DWORD c_New_Equipment_Start = c_Equipment_Start + 23;
	const DWORD c_New_Equipment_Count = 3;
	const DWORD c_Equipment_Ring1 = c_New_Equipment_Start + 0;
	const DWORD c_Equipment_Ring2 = c_New_Equipment_Start + 1;
	const DWORD c_Equipment_Belt  = c_New_Equipment_Start + 2;;
#endif

enum EDragonSoulDeckType
{
	DS_DECK_1,
	DS_DECK_2,
	DS_DECK_MAX_NUM = 2,
};

enum EDragonSoulGradeTypes
{
	DRAGON_SOUL_GRADE_NORMAL,
	DRAGON_SOUL_GRADE_BRILLIANT,
	DRAGON_SOUL_GRADE_RARE,
	DRAGON_SOUL_GRADE_ANCIENT,
	DRAGON_SOUL_GRADE_LEGENDARY,
	DRAGON_SOUL_GRADE_MAX,

};

enum EDragonSoulStepTypes
{
	DRAGON_SOUL_STEP_LOWEST,
	DRAGON_SOUL_STEP_LOW,
	DRAGON_SOUL_STEP_MID,
	DRAGON_SOUL_STEP_HIGH,
	DRAGON_SOUL_STEP_HIGHEST,
	DRAGON_SOUL_STEP_MAX,
};

#ifdef ENABLE_COSTUME_SYSTEM
	const DWORD c_Costume_Slot_Start	= c_Equipment_Start + 19;	// [주의] 숫자(19) 하드코딩 주의. 현재 서버에서 코스츔 슬롯은 19부터임. 서버 common/length.h 파일의 EWearPositions 열거형 참고.
	const DWORD	c_Costume_Slot_Body		= c_Costume_Slot_Start + CItemData::COSTUME_BODY;
	const DWORD	c_Costume_Slot_Hair		= c_Costume_Slot_Start + CItemData::COSTUME_HAIR;
	const DWORD c_Costume_Slot_Mount	= c_Costume_Slot_Start + CItemData::COSTUME_MOUNT;
    const DWORD c_Costume_Slot_Weapon	= c_Costume_Slot_Start + CItemData::COSTUME_WEAPON;
#ifdef ENABLE_PET_COSTUME_SYSTEM
	const DWORD	c_Costume_Slot_Pet		= c_Costume_Slot_Start + 7;
#endif
	const DWORD c_Costume_Slot_Count	= 8;

	const DWORD c_Costume_Slot_End		= c_Costume_Slot_Start + c_Costume_Slot_Count;

#endif


// [주의] 숫자(32) 하드코딩 주의. 현재 서버에서 용혼석 슬롯은 32부터임.
// 서버 common/length.h 파일의 EWearPositions 열거형이 32까지 확장될 것을 염두하고(32 이상은 확장 하기 힘들게 되어있음.),
// 그 이후부터를 용혼석 장착 슬롯으로 사용.
const DWORD c_Wear_Max = 32;
const DWORD c_DragonSoul_Equip_Start = c_ItemSlot_Count + c_Wear_Max;
const DWORD c_DragonSoul_Equip_Slot_Max = 6;
const DWORD c_DragonSoul_Equip_End = c_DragonSoul_Equip_Start + c_DragonSoul_Equip_Slot_Max * DS_DECK_MAX_NUM;

// NOTE: 2013년 2월 5일 현재... 용혼석 데크는 2개가 존재하는데, 향후 확장 가능성이 있어서 3개 데크 여유분을 할당 해 둠. 그 뒤 공간은 벨트 인벤토리로 사용
const DWORD c_DragonSoul_Equip_Reserved_Count = c_DragonSoul_Equip_Slot_Max * 3;

#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	const DWORD c_Belt_Inventory_Slot_Start = c_DragonSoul_Equip_End + c_DragonSoul_Equip_Reserved_Count;
	const DWORD c_Belt_Inventory_Width = 4;
	const DWORD c_Belt_Inventory_Height= 4;
	const DWORD c_Belt_Inventory_Slot_Count = c_Belt_Inventory_Width * c_Belt_Inventory_Height;
	const DWORD c_Belt_Inventory_Slot_End = c_Belt_Inventory_Slot_Start + c_Belt_Inventory_Slot_Count;

	const DWORD c_Inventory_Count = c_Belt_Inventory_Slot_End;
#else
	const DWORD c_Inventory_Count = c_DragonSoul_Equip_End;
#endif

// 용혼석 전용 인벤토리
const DWORD c_DragonSoul_Inventory_Start = 0;
const DWORD c_DragonSoul_Inventory_Box_Size = 32;
const DWORD c_DragonSoul_Inventory_Count = CItemData::DS_SLOT_NUM_TYPES * DRAGON_SOUL_GRADE_MAX * c_DragonSoul_Inventory_Box_Size;
const DWORD c_DragonSoul_Inventory_End = c_DragonSoul_Inventory_Start + c_DragonSoul_Inventory_Count;

enum ESlotType
{
	SLOT_TYPE_NONE,
	SLOT_TYPE_INVENTORY,
	SLOT_TYPE_SKILL,
	SLOT_TYPE_EMOTION,
	SLOT_TYPE_SHOP,
	SLOT_TYPE_EXCHANGE_OWNER,
	SLOT_TYPE_EXCHANGE_TARGET,
	SLOT_TYPE_QUICK_SLOT,
	SLOT_TYPE_SAFEBOX,
	SLOT_TYPE_PRIVATE_SHOP,
	SLOT_TYPE_MALL,
	SLOT_TYPE_DRAGON_SOUL_INVENTORY,
#ifdef ENABLE_SPECIAL_INVENTORY_SYSTEM
	SLOT_TYPE_UPGRADE_INVENTORY,
	SLOT_TYPE_POTIONS_INVENTORY,   
	SLOT_TYPE_BONUS_INVENTORY,  
	SLOT_TYPE_CHEST_INVENTORY,  
#endif
#ifdef ENABLE_SWITCHBOT
	SLOT_TYPE_SWITCHBOT,
#endif
	SLOT_TYPE_MAX,
};

enum EWindows
{
	RESERVED_WINDOW,
	INVENTORY,				
	EQUIPMENT,
	SAFEBOX,
	MALL,
	DRAGON_SOUL_INVENTORY,
#ifdef ENABLE_SPECIAL_INVENTORY_SYSTEM
	UPGRADE_INVENTORY,
	POTIONS_INVENTORY,
	BONUS_INVENTORY,
	CHEST_INVENTORY,
#endif
#ifdef ENABLE_SWITCHBOT
	SWITCHBOT,
#endif
	BELT_INVENTORY,		
	GROUND,
	WINDOW_TYPE_MAX,
};

enum EDSInventoryMaxNum
{
	DS_INVENTORY_MAX_NUM = c_DragonSoul_Inventory_Count,
	DS_REFINE_WINDOW_MAX_NUM = 15,
};


#ifdef ENABLE_SWITCHBOT
enum ESwitchbotValues
{
	SWITCHBOT_SLOT_COUNT = 7,
	SWITCHBOT_ALTERNATIVE_COUNT = 2, 
	MAX_NORM_ATTR_NUM = 5,
};

enum EAttributeSet
{
	ATTRIBUTE_SET_WEAPON,
	ATTRIBUTE_SET_BODY,
	ATTRIBUTE_SET_WRIST,
	ATTRIBUTE_SET_FOOTS,
	ATTRIBUTE_SET_NECK,
	ATTRIBUTE_SET_HEAD,
	ATTRIBUTE_SET_SHIELD,
	ATTRIBUTE_SET_EAR,
	
	ATTRIBUTE_SET_MAX_NUM,
};
#endif

#pragma pack (push, 1)
#define WORD_MAX 0xffff


typedef struct SItemPos
{
	BYTE window_type;
	WORD cell;
    SItemPos ()
    {
		window_type =     INVENTORY;
		cell = WORD_MAX;
    }
	SItemPos (BYTE _window_type, WORD _cell)
    {
        window_type = _window_type;
        cell = _cell;
    }

	bool IsValidCell()
	{
		switch (window_type)
		{
		case INVENTORY:
			return cell < c_Inventory_Count;
			break;
		case EQUIPMENT:
			return cell < c_DragonSoul_Equip_End;
			break;
		case DRAGON_SOUL_INVENTORY:
			return cell < (DS_INVENTORY_MAX_NUM);
			break;
#ifdef ENABLE_SWITCHBOT
		case SWITCHBOT:
			return cell < SWITCHBOT_SLOT_COUNT;
			break;
#endif
#ifdef ENABLE_SPECIAL_INVENTORY_SYSTEM
		case UPGRADE_INVENTORY:
			return cell < c_Special_ItemSlot_Count;
			break;
		case POTIONS_INVENTORY:
			return cell < c_Special_ItemSlot_Count;
			break;
		case BONUS_INVENTORY:
			return cell < c_Special_ItemSlot_Count;
			break;
		case CHEST_INVENTORY:
			return cell < c_Special_ItemSlot_Count;
			break;
#endif
		default:
			return false;
		}
	}
	bool IsEquipCell()
	{
		switch (window_type)
		{
		case INVENTORY:
		case EQUIPMENT:
			return (c_Equipment_Start + c_Wear_Max > cell) && (c_Equipment_Start <= cell);
			break;

		case BELT_INVENTORY:
		case DRAGON_SOUL_INVENTORY:
#ifdef ENABLE_SPECIAL_INVENTORY_SYSTEM
		case UPGRADE_INVENTORY:
		case POTIONS_INVENTORY:
		case BONUS_INVENTORY:
		case CHEST_INVENTORY:
#endif
			return false;
			break;

		default:
			return false;
		}
	}

#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	bool IsBeltInventoryCell()
	{
		bool bResult = c_Belt_Inventory_Slot_Start <= cell && c_Belt_Inventory_Slot_End > cell;
		return bResult;
	}
#endif

	bool operator==(const struct SItemPos& rhs) const
	{
		return (window_type == rhs.window_type) && (cell == rhs.cell);
	}

	bool operator<(const struct SItemPos& rhs) const
	{
		return (window_type < rhs.window_type) || ((window_type == rhs.window_type) && (cell < rhs.cell));
	}
} TItemPos;
#pragma pack(pop)

const DWORD c_QuickBar_Line_Count = 3;
const DWORD c_QuickBar_Slot_Count = 12;

const float c_Idle_WaitTime = 5.0f;

const int c_Monster_Race_Start_Number = 6;
const int c_Monster_Model_Start_Number = 20001;

const float c_fAttack_Delay_Time = 0.2f;
const float c_fHit_Delay_Time = 0.1f;
const float c_fCrash_Wave_Time = 0.2f;
const float c_fCrash_Wave_Distance = 3.0f;

const float c_fHeight_Step_Distance = 50.0f;

enum
{
	DISTANCE_TYPE_FOUR_WAY,
	DISTANCE_TYPE_EIGHT_WAY,
	DISTANCE_TYPE_ONE_WAY,
	DISTANCE_TYPE_MAX_NUM,
};

const float c_fMagic_Script_Version = 1.0f;
const float c_fSkill_Script_Version = 1.0f;
const float c_fMagicSoundInformation_Version = 1.0f;
const float c_fBattleCommand_Script_Version = 1.0f;
const float c_fEmotionCommand_Script_Version = 1.0f;
const float c_fActive_Script_Version = 1.0f;
const float c_fPassive_Script_Version = 1.0f;

// Used by PushMove
const float c_fWalkDistance = 175.0f;
const float c_fRunDistance = 310.0f;

#define FILE_MAX_LEN 128

enum
{
	ITEM_SOCKET_SLOT_MAX_NUM = 3,
	// refactored attribute slot begin
	ITEM_ATTRIBUTE_SLOT_NORM_NUM	= 5,
	ITEM_ATTRIBUTE_SLOT_RARE_NUM	= 2,

	ITEM_ATTRIBUTE_SLOT_NORM_START	= 0,
	ITEM_ATTRIBUTE_SLOT_NORM_END	= ITEM_ATTRIBUTE_SLOT_NORM_START + ITEM_ATTRIBUTE_SLOT_NORM_NUM,

	ITEM_ATTRIBUTE_SLOT_RARE_START	= ITEM_ATTRIBUTE_SLOT_NORM_END,
	ITEM_ATTRIBUTE_SLOT_RARE_END	= ITEM_ATTRIBUTE_SLOT_RARE_START + ITEM_ATTRIBUTE_SLOT_RARE_NUM,

	ITEM_ATTRIBUTE_SLOT_MAX_NUM		= ITEM_ATTRIBUTE_SLOT_RARE_END, // 7
	// refactored attribute slot end
};

#pragma pack(push)
#pragma pack(1)

typedef struct SQuickSlot
{
	BYTE Type;
	BYTE Position;
} TQuickSlot;

typedef struct TPlayerItemAttribute
{
    BYTE        bType;
    short       sValue;
} TPlayerItemAttribute;

typedef struct packet_item
{
    DWORD       vnum;
#ifdef ENABLE_EXTEND_ITEMS_STACK
	WORD		count;
#else
	BYTE		count;
#endif
	DWORD		flags;
	DWORD		anti_flags;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
} TItemData;

typedef struct packet_shop_item
{
    DWORD       vnum;
#ifdef ENABLE_REMOVE_LIMIT_GOLD
    unsigned long long       price;
#else
	DWORD		price;
#endif
#ifdef ENABLE_EXTEND_ITEMS_STACK
	WORD		count;
#else
	BYTE		count;
#endif

	BYTE		display_pos;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
#if defined(ENABLE_RENEWAL_SHOPEX)
	BYTE 	price_type;
	DWORD 	price_vnum;
#endif
} TShopItemData;

#if defined(ENABLE_RENEWAL_SHOPEX)
enum STableExTypes
{
	SHOPEX_GOLD = 1,
	SHOPEX_SECONDARY,
	SHOPEX_ITEM,
	SHOPEX_EXP,
	SHOPEX_MAX,
};
#endif
#ifdef ENABLE_BATTLE_PASS
enum
{
	BATTLEPASS_REWARD_COUNT = 3,
	BATTLEPASS_MAX_DESC_LINES = 7,
	BATTLEPASS_MAX_SUB_MISSIONS = 5,
	BATTLEPASS_MAX_PROGRESS = 2,
};
typedef struct BattlePassReward
{
	uint32_t vnum, count;

} TRewardTableBP;
typedef struct BattlePassParser
{
	std::string missionName;
	uint8_t missionVnum;

	uint32_t progress;
	uint32_t maxProgress;

	TRewardTableBP rewards[BATTLEPASS_REWARD_COUNT];
	std::array<std::string, BATTLEPASS_MAX_DESC_LINES> descArray;
	std::array<int16_t, BATTLEPASS_MAX_SUB_MISSIONS> subMissions;

	bool isSubMission = false;
	bool isFormat = false;


	bool isActive = false;


} TBattlePassParser;
typedef struct BattlePass
{
	uint8_t missionVnum;
	int32_t progress;

	uint8_t isCompleted = 0;
	bool isActive = true;

} TBattlePass;

enum BattlePassTypes { BATTLEPASS_FREE };
enum
{
	MISSION_FREE_BOSS_SLAYER_1,
	MISSION_FREE_BOSS_SLAYER_2,
	MISSION_FREE_BOSS_SLAYER_3,
	MISSION_FREE_BOSS_SLAYER_4,

	MISSION_FREE_ITEM_BREAK_1,
	MISSION_FREE_ITEM_BREAK_2,
	MISSION_FREE_ITEM_BREAK_3,
	MISSION_FREE_ITEM_BREAK_4,

	MISSION_FREE_MASSACRE,

	MISSION_FREE_CHEST_FISHER,
	MISSION_FREE_CHEST_HEXAGON,

	MISSION_FREE_STONE_BREAKER,
	MISSION_FREE_OX,

	MISSION_FREE_MESSAGER,
	MISSION_FREE_LETTER,

	MISSION_FREE_SHOP_BUY,
	MISSION_FREE_ITEM_CRAFT,
	MISSION_FREE_COLLECT_ICE_CREAM,

	MISSION_FREE_DAILY_COMPLETE,
	MISSION_DAMAGE,

	MISSION_FREE_MISSIONS_END,

	MISSION_BP_LAST_NUM,
};

enum
{
	MISSION_FREE_START = MISSION_FREE_BOSS_SLAYER_1,
	MISSION_FREE_END = MISSION_FREE_MISSIONS_END,
};
#endif
#pragma pack(pop)

inline float GetSqrtDistance(int ix1, int iy1, int ix2, int iy2) // By sqrt
{
	float dx, dy;

	dx = float(ix1 - ix2);
	dy = float(iy1 - iy2);

	return sqrtf(dx*dx + dy*dy);
}

// DEFAULT_FONT
void DefaultFont_Startup();
void DefaultFont_Cleanup();
void DefaultFont_SetName(const char * c_szFontName);
CResource* DefaultFont_GetResource();
CResource* DefaultItalicFont_GetResource();
// END_OF_DEFAULT_FONT

void SetGuildSymbolPath(const char * c_szPathName);
const char * GetGuildSymbolFileName(DWORD dwGuildID);
BYTE SlotTypeToInvenType(BYTE bSlotType);
#ifdef ENABLE_DETAILS_UI
BYTE ApplyTypeToPointType(BYTE bApplyType);
#endif
