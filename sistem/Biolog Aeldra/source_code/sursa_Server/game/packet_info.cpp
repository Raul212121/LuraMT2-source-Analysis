#before

}

CPacketInfoCG::~CPacketInfoCG()
{
	Log("packet_info.txt");
}

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
	Set(HEADER_CG_BIOLOG_MANAGER, sizeof(TPacketCGBiologManagerAction), "BiologManager");
#endif