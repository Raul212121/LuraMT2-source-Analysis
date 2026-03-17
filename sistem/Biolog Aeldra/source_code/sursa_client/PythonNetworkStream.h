# ADD AT THE BOTTOM BEFORE };

#ifdef ENABLE_BIOLOG_SYSTEM
	public:
		bool	SendBiologManagerAction(BYTE bSubHeader);

	protected:
		bool	RecvBiologManager();
#endif

