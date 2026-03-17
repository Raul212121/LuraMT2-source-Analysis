# Add CG_HEADER take core for enums!!

#ifdef ENABLE_BIOLOG_SYSTEM
	HEADER_CG_BIOLOG_MANAGER = 84,
#endif

# ADD GC_HEADER take core for enums!!

#ifdef ENABLE_BIOLOG_SYSTEM
	HEADER_GC_BIOLOG_MANAGER = 84,
#endif


# ADD at the bottom before #pragma pack(pop)

#ifdef ENABLE_BIOLOG_SYSTEM
enum ECGBiologSubHeaders {
	CG_BIOLOG_MANAGER_OPEN,
	CG_BIOLOG_MANAGER_SEND,
	CG_BIOLOG_MANAGER_TIMER,
};

enum EGCBiologSubHeaders {
	GC_BIOLOG_MANAGER_OPEN,
	GC_BIOLOG_MANAGER_ALERT,
	GC_BIOLOG_MANAGER_CLOSE,
};

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
