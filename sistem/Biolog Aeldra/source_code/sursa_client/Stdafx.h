# BEFORE


extern const std::string& ApplicationStringTable_GetString(DWORD dwID);

# ADD

#ifdef ENABLE_BIOLOG_SYSTEM
void initBiologManager();
#endif

