# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
#include "BiologSystemManager.hpp"
#endif


# AFTER

		case HEADER_CG_DRAGON_SOUL_REFINE:
			{
				TPacketCGDragonSoulRefine* p = reinterpret_cast <TPacketCGDragonSoulRefine*>((void*)c_pData);
				switch(p->bSubType)
				{
				case DS_SUB_HEADER_CLOSE:
					ch->DragonSoul_RefineWindow_Close();
					break;
				case DS_SUB_HEADER_DO_REFINE_GRADE:
					{
						DSManager::instance().DoRefineGrade(ch, p->ItemGrid);
					}
					break;
#ifdef __ENABLE_DS_REFINE_ALL__
				case DS_SUB_HEADER_DO_REFINE_GRADE_ALL:
				{
					DSManager::instance().DoAllRefineGrade(ch, p->ItemGrid[0].cell, p->ItemGrid[1].cell);
				}
				break;
#endif
				case DS_SUB_HEADER_DO_REFINE_STEP:
					{
						DSManager::instance().DoRefineStep(ch, p->ItemGrid);
					}
					break;
				case DS_SUB_HEADER_DO_REFINE_STRENGTH:
					{
						DSManager::instance().DoRefineStrength(ch, p->ItemGrid);
					}
					break;
				}
			}
			break;

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
		case HEADER_CG_BIOLOG_MANAGER:
			if ((iExtraLen = BiologManager(ch, c_pData, m_iBufferLeft)) < 0)
				return -1;
			break;
#endif

# AT THE BOTTOM OF FILE ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
int CInputMain::BiologManager(LPCHARACTER ch, const char* c_pData, size_t uiBytes)
{
	if (!ch)
		return -1;

	TPacketCGBiologManagerAction* p = (TPacketCGBiologManagerAction*)c_pData;
	c_pData += sizeof(TPacketCGBiologManagerAction);

	CBiologSystem* pkBiologManager = ch->GetBiologManager();
	if (!pkBiologManager)
		return -1;

	return pkBiologManager->RecvClientPacket(p->bSubHeader, c_pData, uiBytes);
}
#endif
