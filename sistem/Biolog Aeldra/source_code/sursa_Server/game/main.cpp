# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
    #include "BiologSystemManager.cpp"
#endif

#ifdef __NEW_EVENT_HANDLER__
	#include "EventFunctionHandler.hpp"
#endif

# AFTER

while (idle());

# ADD

#ifdef __NEW_EVENT_HANDLER__
    CEventFunctionHandler EventFunctionHandler;
#endif

# AFTER

	sys_log(0, "<shutdown> Destroying quest::CQuestManager...");
	quest::CQuestManager::instance().Destroy();
	sys_log(0, "<shutdown> Destroying building::CManager...");
	building::CManager::instance().Destroy();

# ADD

#ifdef __NEW_EVENT_HANDLER__
	sys_log(0, "<shutdown> Destroying CEventFunctionHandler...");
	CEventFunctionHandler::instance().Destroy();
#endif


#before

	return 1;
}

int io_loop(LPFDWATCH fdw)


# ADD

#ifdef __NEW_EVENT_HANDLER__
	CEventFunctionHandler::instance().Process();
#endif


#before

	if (!start(argc, argv)) {
		CleanUpForEarlyExit();
		return 0;
	}

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	CBiologSystemManager biologSystem;
#endif
