#include "stdafx.h"
#include "char.h"
#include "utils.h"
#include "packet.h"
#include "questmanager.h"
#include "Bio_olog.h"
#include "desc_client.h"
#include "desc_manager.h"
#include "../../common/service.h"

int iConfigBioTimeWait[] = // Valori; minute*secunde
{
	1*60,		/*Mission I*/ 
	1*60, 		/*Mission II*/ 	
	1*60, 		/*Mission III*/ 
	1*60, 		/*Mission IV*/ 	
	1*60, 		/*Mission V*/ 	
	1*60, 		/*Mission VI*/ 	
	1*60, 		/*Mission VII*/ 
	1*60, 		/*Mission VIII*/
	1*60, 		/*Mission IX*/
	1*60, 		/*Mission X*/
	1*60, 		/*Mission XI*/
	
}; 

int iConfigPointBio[MISSION_MAX_BIOLOG][6] =
{
	{ APPLY_ATTBONUS_MONSTER, 10}, 
	{ APPLY_ATTBONUS_MONSTER, 5},
	{ APPLY_ATTBONUS_MONSTER, 5},
	{ APPLY_MAX_HP, 1000},
	{ APPLY_ATT_GRADE_BONUS, 100},
	{ APPLY_EXP_DOUBLE_BONUS, 20},
	{ APPLY_CRITICAL_PCT, 5},
	{ APPLY_PENETRATE_PCT, 5},
	{ APPLY_ATTBONUS_HUMAN, 10},
	{ APPLY_MELEE_MAGIC_ATTBONUS_PER, 5},
};

int iConfigRewardBIO[] = {71124, 71125, 0, 0, 0, 0, 0, 0, 0, 0, 71124};
int iConfigNeedItemBIO[MISSION_MAX_BIOLOG][2] = 
{
	{30006, 10},   /*Mission I*/ 
	{30006, 10},   /*Mission II*/ 	
	{30006, 10},   /*Mission III*/ 
	{30006, 10},   /*Mission IV*/ 	
	{30006, 10},   /*Mission V*/ 	
	{30006, 15},   /*Mission VI*/ 	
	{30006, 15},   /*Mission VII*/ 
	{30006, 20},   /*Mission VIII*/
	{30006, 1},    /*Mission IX*/
	{30006, 1},    /*Mission X*/
	{30006, 1},    /*Mission XI*/
	};
	
int iConfigBioSansaDeEsuare[] = {40, 40, 40, 40, 40, 40, 40, 40, 25, 25, 25};
int iConfigBioNeedLevel[] = {30, 40, 50, 60, 70, 80, 85, 90, 95, 100, 105};

int iAffectBiolog[] = 
{
	AFF_BIO_1, 
	AFF_BIO_2, 
	AFF_BIO_3, 
	AFF_BIO_4, 
	AFF_BIO_5, 
	AFF_BIO_6, 
	AFF_BIO_7,
	AFF_BIO_8, 
	AFF_BIO_9, 
	AFF_BIO_10,
	AFF_BIO_11
};

CBiolog::CBiolog()
{
}

CBiolog::~CBiolog()
{
}

int CBiolog::GetReqItem(int iValue, int iCollect, int option)
{
	if (option == 0)
		return iConfigNeedItemBIO[iValue][0];
	else if (option == 1)
		return iConfigNeedItemBIO[iValue][1] - iCollect;
	else if (option == 2)
		return iConfigNeedItemBIO[iValue][1];
	
	return 0;
}

int CBiolog::GetReqLevel(int iValue)
{
	return iConfigBioNeedLevel[iValue];
}

int CBiolog::GetRewardPoint(int iValue, int index)
{
	return iConfigPointBio[iValue][index];
}

int CBiolog::GetRewardItem(int iValue)
{
	return iConfigRewardBIO[iValue];
}

void CBiolog::BiologMission(LPCHARACTER ch, int index)
{
	quest::PC * pPC = quest::CQuestManager::instance().GetPC(ch->GetPlayerID());

	if (!pPC)
		return;
	
	if (ch->GetLevel() < iConfigBioNeedLevel[index])
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Nu ai nivelul necesar!");
		return;
	}
	
	if (ch->CountSpecifyItem(iConfigNeedItemBIO[index][0]) < 1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Nu ai obiectul necesar!");
		return;
	}
	
	TPacketGCSendInfoBiolog packet;
	packet.bHeader = HEADER_GC_SEND_BIOLOG_INFO;
	
	int iNorocel = number(1, 100);

	pPC->SetFlag("biolog.wait_time", iConfigBioTimeWait[index] + get_global_time());	
	ch->RemoveSpecifyItem(iConfigNeedItemBIO[index][0], 1);
	
	if (iNorocel < iConfigBioSansaDeEsuare[index])
	{
		packet.iTimeLeft = iConfigBioTimeWait[index] + get_global_time();
		packet.bInfoChecked = false;
		ch->GetDesc()->Packet(&packet, sizeof(TPacketGCSendInfoBiolog));
		
		ch->ChatPacket(CHAT_TYPE_INFO, "Din pacate a esuat s-a dus drq!");
		return;
	}

	char szBuf[30];
	snprintf(szBuf, sizeof(szBuf), "biolog_%d.completate", index);
	int iCollect = pPC->GetFlag(szBuf);
	pPC->SetFlag(szBuf, iCollect + 1);

	++iCollect;

	if (iCollect == iConfigNeedItemBIO[index][1])
	{
		int iVal = pPC->GetFlag("biolog.complete");
		pPC->SetFlag("biolog.complete", iVal + 1);
		
		ch->AutoGiveItem(iConfigRewardBIO[index], 1);
		ch->AddAffect(iAffectBiolog[index], aApplyInfo[iConfigPointBio[index][0]].bPointType, iConfigPointBio[index][1], 0, 60*60*60*365, 0, false);
		
		if (iConfigPointBio[index][3] > 0)
			ch->AddAffect(iAffectBiolog[index], aApplyInfo[iConfigPointBio[index][2]].bPointType, iConfigPointBio[index][3], 0, 60*60*60*365, 0, false);
 
		if (iConfigPointBio[index][5] > 0)
			ch->AddAffect(iAffectBiolog[index], aApplyInfo[iConfigPointBio[index][4]].bPointType, iConfigPointBio[index][5], 0, 60*60*60*365, 0, false);
		
		ch->ChatPacket(CHAT_TYPE_NOTICE, "Ai terminat o misiune din biolog!");

	}
	else		
		ch->ChatPacket(CHAT_TYPE_INFO, "Un Obiect a fost adaugat la biolog!");
	
	int iValue = pPC->GetFlag("biolog.complete");

	char szBuf2[30];
	snprintf(szBuf2, sizeof(szBuf2), "biolog_%d.completate", iValue);
	iCollect = pPC->GetFlag(szBuf2);
	
	if (iValue >= MISSION_MAX_BIOLOG)
	{
		ch->ChatPacket(CHAT_TYPE_NOTICE, "Felicitari, ai terminat toate misiunile!");
		return;
	}

	packet.iTimeLeft = iConfigBioTimeWait[iValue] + get_global_time();
	packet.iRewardItem = iConfigRewardBIO[iValue];
	for (int i = 0; i < 6; ++i)
		packet.iRewardPoints[i] = iConfigPointBio[iValue][i];
	packet.iReqItem[0] = iConfigNeedItemBIO[iValue][0];
	packet.iReqItem[1] = iConfigNeedItemBIO[iValue][1];
	packet.iReqItem[2] = iConfigNeedItemBIO[iValue][1] - iCollect;
	packet.iReqLevel = iConfigBioNeedLevel[iValue];	
	packet.bInfoChecked = true;

	ch->GetDesc()->Packet(&packet, sizeof(TPacketGCSendInfoBiolog));
}
