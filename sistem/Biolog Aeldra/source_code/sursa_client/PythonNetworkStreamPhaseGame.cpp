# BEFORE

			default:
				ret = RecvDefaultPacket(header);
				break;


# ADD

#ifdef ENABLE_BIOLOG_SYSTEM
			case HEADER_GC_BIOLOG_MANAGER:
				ret = RecvBiologManager();
				break;
#endif


# ADD AT THE BOTTOM OF FILE

#ifdef ENABLE_BIOLOG_SYSTEM
bool CPythonNetworkStream::SendBiologManagerAction(BYTE bSubHeader)
{
	if (!__CanActMainInstance())
		return true;

	TPacketCGBiologManagerAction packet;
	packet.bHeader = HEADER_CG_BIOLOG_MANAGER;
	packet.bSubHeader = bSubHeader;

	if (!Send(sizeof(TPacketCGBiologManagerAction), &packet))
	{
		Tracef("SendBiologManagerAction Send Packet Error\n");
		return false;
	}

	return SendSequence();
}

bool CPythonNetworkStream::RecvBiologManager()
{
	TPacketGCBiologManager packet;
	if (!Recv(sizeof(packet), &packet)) {
		TraceError("RecvBiologManager Error");
		return false;
	}

	switch (packet.bSubHeader)
	{
	case GC_BIOLOG_MANAGER_OPEN:
	{
		TPacketGCBiologManagerInfo kInfo;
		if (!Recv(sizeof(kInfo), &kInfo))
			return false;

		CPythonBiologManager::Instance()._LoadBiologInformation(&kInfo);
		if (kInfo.bUpdate)
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_BiologManagerUpdate", Py_BuildValue("()"));
		else
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_BiologManagerOpen", Py_BuildValue("()"));
	}
	break;
	case GC_BIOLOG_MANAGER_ALERT:
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_BiologManagerAlert", Py_BuildValue("()"));
	}
	break;
	case GC_BIOLOG_MANAGER_CLOSE:
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_BiologManagerClose", Py_BuildValue("()"));
	}
	break;
	}
	return true;
}
#endif
