# BEFORE


};

class CInputDead : public CInputMain

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
		int			BiologManager(LPCHARACTER ch, const char* c_pData, size_t uiBytes);
#endif