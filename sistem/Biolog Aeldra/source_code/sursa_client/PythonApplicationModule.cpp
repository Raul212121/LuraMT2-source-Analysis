# Add

#ifdef ENABLE_BIOLOG_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_BIOLOG_SYSTEM", true);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_BIOLOG_SYSTEM", false);
#endif
