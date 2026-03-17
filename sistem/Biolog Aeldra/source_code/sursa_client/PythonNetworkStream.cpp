# BEFORE THIS!


		}
};

int g_iLastPacket[2] = { 0, 0 };

# ADD

#ifdef ENABLE_BIOLOG_SYSTEM
			Set(HEADER_GC_BIOLOG_MANAGER, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCBiologManager), DYNAMIC_SIZE_PACKET));
#endif