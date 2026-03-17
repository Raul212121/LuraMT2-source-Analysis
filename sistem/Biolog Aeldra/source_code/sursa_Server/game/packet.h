# Add CG_HEADER take core for enums!!

#ifdef __ENABLE_BIOLOG_SYSTEM__
	HEADER_CG_BIOLOG_MANAGER = 84,
#endif

# ADD GC_HEADER take core for enums!!

#ifdef __ENABLE_BIOLOG_SYSTEM__
	HEADER_GC_BIOLOG_MANAGER,
#endif

# ADD at the bottom before #pragma pack(pop)

#ifdef __ENABLE_BIOLOG_SYSTEM__
typedef struct SPacketCGBiologManagerAction
{
	BYTE bHeader;
	BYTE bSubHeader;
} TPacketCGBiologManagerAction;

typedef struct SPacketGCBiologManager
{
	BYTE	bHeader;
	WORD	wSize;
	BYTE	bSubHeader;
} TPacketGCBiologManager;

typedef struct SPacketGCBiologManagerInfo
{
	bool	bUpdate;
	BYTE	bRequiredLevel;
	DWORD	iRequiredItem;
	WORD	wGivenItems;
	WORD	wRequiredItemCount;
	time_t	iGlobalCooldown;
	time_t	iCooldown;
	bool	iCooldownReminder;
	BYTE	bChance;
	DWORD	bApplyType;
	long	lApplyValue;
} TPacketGCBiologManagerInfo;
#endif
