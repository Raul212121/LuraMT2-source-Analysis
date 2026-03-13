#pragma once

class CPythonSystem : public CSingleton<CPythonSystem>
{
	public:
		enum EWindow
		{
			WINDOW_STATUS,
			WINDOW_INVENTORY,
			WINDOW_ABILITY,
			WINDOW_SOCIETY,
			WINDOW_JOURNAL,
			WINDOW_COMMAND,

			WINDOW_QUICK,
			WINDOW_GAUGE,
			WINDOW_MINIMAP,
			WINDOW_CHAT,

			WINDOW_MAX_NUM,
		};

#ifdef ENABLE_PICKUP_FILTER
		enum EPickupModes {
			PICKUP_MODE_ALL,
		};

		enum EPickupIgnores {
			PICKUP_IGNORE_WEAPON,
			PICKUP_IGNORE_ARMOR,
			PICKUP_IGNORE_HEAD,
			PICKUP_IGNORE_SHIELD,
			PICKUP_IGNORE_WRIST,
			PICKUP_IGNORE_FOOTS,
			PICKUP_IGNORE_NECK,
			PICKUP_IGNORE_EAR,
			PICKUP_IGNORE_ETC,
			PICKUP_IGNORE_MAX_NUM,
		};
#endif

		enum
		{
			FREQUENCY_MAX_NUM  = 30,
			RESOLUTION_MAX_NUM = 100
		};

		typedef struct SResolution
		{
			DWORD	width;
			DWORD	height;
			DWORD	bpp;		// bits per pixel (high-color = 16bpp, true-color = 32bpp)

			DWORD	frequency[20];
			BYTE	frequency_count;
		} TResolution;

		typedef struct SWindowStatus
		{
			int		isVisible;
			int		isMinimized;

			int		ixPosition;
			int		iyPosition;
			int		iHeight;
		} TWindowStatus;

		typedef struct SConfig
		{
			DWORD			width;
			DWORD			height;
			DWORD			bpp;
			DWORD			frequency;

			bool			is_software_cursor;
			bool			is_object_culling;
			int				iDistance;
			int				iShadowLevel;
#ifdef ENABLE_FOV_OPTION
			FLOAT            iFOVLevel;
#endif
			FLOAT			music_volume;
			BYTE			voice_volume;

			int				gamma;

			int				isSaveID;
			char			SaveID[20];

			bool			bWindowed;
			bool			bDecompressDDS;
			bool			bNoSoundCard;
			bool			bUseDefaultIME;
			BYTE			bSoftwareTiling;
			bool			bViewChat;
			bool			bAlwaysShowName;
			bool			bShowDamage;
			bool			bShowSalesText;
#ifdef ENABLE_NEW_GAME_OPTIONS
			bool			bChatModeFilter;
			bool			bShowMoneyLog;
			int				iShowOfflineShop;
			int				bShowFrames;
#endif
#ifdef ENABLE_ENVIRONMENT_EFFECT_OPTION
			bool			bShowNightMode;
			bool			bShowSnowMode;
			bool 			bShowFogMode;
#endif
#ifdef ENABLE_HIDE_MOUNT_PET
			bool			bHidePets;
			bool			bHideMounts;
#endif
#ifdef ENABLE_PICKUP_FILTER
			BYTE			bPickupMode;
			bool			b_arPickupIgnore[PICKUP_IGNORE_MAX_NUM];
#endif
		} TConfig;

		CPythonSystem();
		virtual ~CPythonSystem();

		void Clear();
		void SetInterfaceHandler(PyObject * poHandler);
		void DestroyInterfaceHandler();

		// Config
		void							SetDefaultConfig();
		bool							LoadConfig();
		bool							SaveConfig();
		void							ApplyConfig();
		void							SetConfig(TConfig * set_config);
		TConfig *						GetConfig();
		void							ChangeSystem();

		// Interface
		bool							LoadInterfaceStatus();
		void							SaveInterfaceStatus();
		bool							isInterfaceConfig();
		const TWindowStatus &			GetWindowStatusReference(int iIndex);

		DWORD							GetWidth();
		DWORD							GetHeight();
		DWORD							GetBPP();
		DWORD							GetFrequency();
		bool							IsSoftwareCursor();
		bool							IsWindowed();
		bool							IsViewChat();
		bool							IsAlwaysShowName();
		bool							IsShowDamage();
		bool							IsShowSalesText();
		bool							IsUseDefaultIME();
		bool							IsNoSoundCard();
		bool							IsAutoTiling();
		bool							IsSoftwareTiling();
		void							SetSoftwareTiling(bool isEnable);
		void							SetViewChatFlag(int iFlag);
		void							SetAlwaysShowNameFlag(int iFlag);
		void							SetShowDamageFlag(int iFlag);
		void							SetShowSalesTextFlag(int iFlag);
#ifdef ENABLE_NEW_GAME_OPTIONS
		bool							IsShowMoneyLog();
		void 							SetShowMoneyLog(int iFlag);
		bool							IsEnableChatFilterDice();
		void							SetEnableChatFilterDice(int iFlag);
		int								GetShowOfflineShopFlag();
		void							SetShowOfflineShop(int iFlag);
		bool							IsShowFramesOption();
		void							SetShowFramesOption(int iFlag);
#endif
#ifdef ENABLE_PICKUP_FILTER
		BYTE							 GetPickupMode();
		void							 SetPickupMode(BYTE iMode);
		bool							 GetPickupIgnore(int iType);
		void							 SetPickupIgnore(int iType, int iIgnore);
#endif
#if defined(ENABLE_ENVIRONMENT_EFFECT_OPTION)
		void							SetNightModeOption(int iFlag);
		bool							GetNightModeOption();
		void							SetSnowModeOption(int iFlag);
		bool							GetSnowModeOption();
		void 							SetFogModeOption(int iFlag);
		bool 							GetFogModeOption();
#endif
#ifdef ENABLE_HIDE_MOUNT_PET
	    void							SetHidePets(bool iFlag)								{ m_Config.bHidePets = iFlag; }
	    void							SetHideMounts(bool iFlag)							{ m_Config.bHideMounts = iFlag; }
		bool							IsHidePets()										{ return m_Config.bHidePets; }
		bool							IsHideMounts()										{ return m_Config.bHideMounts; }
#endif

		// Window
		void							SaveWindowStatus(int iIndex, int iVisible, int iMinimized, int ix, int iy, int iHeight);

		// SaveID
		int								IsSaveID();
		const char *					GetSaveID();
		void							SetSaveID(int iValue, const char * c_szSaveID);

		/// Display
		void							GetDisplaySettings();

		int								GetResolutionCount();
		int								GetFrequencyCount(int index);
		bool							GetResolution(int index, OUT DWORD *width, OUT DWORD *height, OUT DWORD *bpp);
		bool							GetFrequency(int index, int freq_index, OUT DWORD *frequncy);
		int								GetResolutionIndex(DWORD width, DWORD height, DWORD bpp);
		int								GetFrequencyIndex(int res_index, DWORD frequency);
		bool							isViewCulling();

		// Sound
		float							GetMusicVolume();
		int								GetSoundVolume();
		void							SetMusicVolume(float fVolume);
		void							SetSoundVolumef(float fVolume);

		int								GetDistance();
		int								GetShadowLevel();
		void							SetShadowLevel(unsigned int level);
#ifdef ENABLE_FOV_OPTION
        float                           GetFOVLevel();
        void                            SetFOVLevel(float fFOV);
#endif

	protected:
		TResolution						m_ResolutionList[RESOLUTION_MAX_NUM];
		int								m_ResolutionCount;

		TConfig							m_Config;
		TConfig							m_OldConfig;

		bool							m_isInterfaceConfig;
		PyObject*						m_poInterfaceHandler;
		TWindowStatus					m_WindowStatus[WINDOW_MAX_NUM];
};