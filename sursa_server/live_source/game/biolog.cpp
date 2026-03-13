#include "stdafx.h"
#include "char.h"
#include "utils.h"
#include "packet.h"
#include "questmanager.h"
#include "desc_client.h"
#include "desc_manager.h"
#include "../common/CommonDefines.h"
#include "biolog.h"

int iConfigBioTimeWait[] = // Valori; minute*secunde
{
	10*60,		/*Misiune nivel 30*/
	10*60, 		/*Misiune nivel 40*/
	10*60, 		/*Misiune nivel 50*/
	10*60, 		/*Misiune nivel 60*/
	10*60, 	    /*Misiune nivel 70*/
	10*60, 	    /*Misiune nivel 80*/
	30*60, 	/*Misiune nivel 85*/
	30*60, 	/*Misiune nivel 90*/
	30*60, 	/*Misiune nivel 92*/
	30*60, 	/*Misiune nivel 94*/
};

int iConfigPointBio[MISSION_MAX_BIOLOG][8] =
{
	{ APPLY_MOV_SPEED, 10}, // 30
	{ APPLY_ATT_SPEED, 5}, // 40
	{ APPLY_DEF_GRADE_BONUS, 60}, // 50
	{ APPLY_ATT_GRADE_BONUS, 50}, // 60
	{ APPLY_MOV_SPEED, 10, APPLY_DEF_GRADE_BONUS, 10}, // 70
	{ APPLY_ATT_SPEED, 6, APPLY_MALL_ATTBONUS, 10, APPLY_RESIST_MONSTER,10}, // 80
	{ APPLY_RESIST_WARRIOR, 10, APPLY_RESIST_ASSASSIN, 10, APPLY_RESIST_SURA, 10, APPLY_RESIST_SHAMAN, 10}, // 85
	{ APPLY_ATTBONUS_WARRIOR, 8, APPLY_ATTBONUS_ASSASSIN, 8, APPLY_ATTBONUS_SURA, 8, APPLY_ATTBONUS_SHAMAN, 8}, // 90
	{ APPLY_MAX_HP, 1500},
	{ APPLY_ATT_GRADE_BONUS, 60},
};

int iConfigRewardBIO[] = {50109, 50110, 50111, 50112, 50113, 50114, 50115, 80007, 80007, 80007};
int iConfigNeedItemBIO[MISSION_MAX_BIOLOG][2] =
{
	{30006, 10},   /*Misiune nivel 30*/
	{30047, 15},   /*Misiune nivel 40*/
	{30015, 15},   /*Misiune nivel 50*/
	{30050, 20},   /*Misiune nivel 60*/
	{30165, 25},   /*Misiune nivel 70*/
	{30166, 30},   /*Misiune nivel 80*/
	{30167, 40},   /*Misiune nivel 85*/
	{30168, 50},   /*Misiune nivel 90*/
	{30251, 10},   /*Misiune nivel 92*/
	{30252, 20},   /*Misiune nivel 94*/
};

static const int eConfigSansa[2] = {
    60, // sansa fara elixir [0]
    20 // sansa cu elixir [1]
};

int iConfigBioNeedLevel[] = {30, 40, 50, 60, 70, 80, 85, 90, 92, 94};

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
	AFF_BIO_10
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


void CBiolog::ObjectDrop(LPCHARACTER pkChar, LPCHARACTER pkVictim, DWORD pkVictimVnum, int index)
{
	if (!pkChar || !pkVictim)
		return;

	quest::PC * pPC = quest::CQuestManager::instance().GetPC(pkChar->GetPlayerID());

	if (!pPC)
		return;

	int iValue = pPC->GetFlag("biolog.complete");
	if (iValue < 0 && iValue > MISSION_MAX_BIOLOG)
		return;

	const DWORD monsterList[][15] = {
		{601, 636, 656},
		{706, 756},
		{1001, 1002, 1003, 1004},
		{1107, 1105},
		{2302, 2303, 2304},
		{1401, 1601, 1602},
		{2313, 2314, 2315, 2311, 2312},
		{691, 2091, 2191, 794, 1901, 2206, 1304, 1093, 1191, 2492, 2493, 2598, 3090, 3290, 3590},
		{1137, 1135},
		{2414, 2412}
	};

	const int mobDropChance[] = {
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_30"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_40"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_50"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_60"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_70"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_80"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_85"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_90"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_92"),
		quest::CQuestManager::instance().GetEventFlag("biodrop_lv_94")
	};

	for (const auto& vnum : monsterList[iValue])
	{
		if (vnum == 0)
			continue;

		if (pkVictimVnum == vnum)
		{
			if (number(1, 100) <= mobDropChance[iValue])
			{
				pkChar->ChatPacket(CHAT_TYPE_INFO, "Obiectul necesar pentru biolog a fost gasit.");
				pkChar->AutoGiveItem(iConfigNeedItemBIO[index][0], 1);
			}
		}
	}
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
		ch->ChatPacket(CHAT_TYPE_INFO, "Nu ai obiectul necesar pentru misiune!");
		return;
	}

	TPacketGCSendInfoBiolog packet;
	packet.bHeader = HEADER_GC_SEND_BIOLOG_INFO;

	pPC->SetFlag("biolog.wait_time", iConfigBioTimeWait[index] + get_global_time());
	ch->RemoveSpecifyItem(iConfigNeedItemBIO[index][0], 1);

	int iRandom = number(1, 100);
    int iPass_percent = eConfigSansa[0];

    if (ch->FindAffect(AFFECT_RESEARCHER_ELIXIR))
    {
        ch->RemoveAffect(AFFECT_RESEARCHER_ELIXIR);
        iPass_percent = eConfigSansa[1];

        if (iRandom <= iPass_percent)
        {
            packet.iTimeLeft = iConfigBioTimeWait[index] + get_global_time();
            packet.bInfoChecked = false;
            ch->GetDesc()->Packet(&packet, sizeof(TPacketGCSendInfoBiolog));
            ch->ChatPacket(CHAT_TYPE_INFO, "Din pacate a esuat! Incearca mai tarziu.");
            return;
        }
    }

    if (iRandom <= iPass_percent)
    {
        packet.iTimeLeft = iConfigBioTimeWait[index] + get_global_time();
        packet.bInfoChecked = false;
        ch->GetDesc()->Packet(&packet, sizeof(TPacketGCSendInfoBiolog));
        ch->ChatPacket(CHAT_TYPE_INFO, "Din pacate a esuat! Incearca mai tarziu.");
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

		if (iConfigRewardBIO[index] > 9) {
			ch->AutoGiveItem(iConfigRewardBIO[index], 2);
		}
		else {
			ch->AutoGiveItem(iConfigRewardBIO[index], 1);
		}

		ch->AddAffect(iAffectBiolog[index], aApplyInfo[iConfigPointBio[index][0]].bPointType, iConfigPointBio[index][1], 0, 60*60*60*365, 0, false);

		if (iConfigPointBio[index][3] > 0)
			ch->AddAffect(iAffectBiolog[index], aApplyInfo[iConfigPointBio[index][2]].bPointType, iConfigPointBio[index][3], 0, 60*60*60*365, 0, false);

		if (iConfigPointBio[index][5] > 0)
			ch->AddAffect(iAffectBiolog[index], aApplyInfo[iConfigPointBio[index][4]].bPointType, iConfigPointBio[index][5], 0, 60*60*60*365, 0, false);

		if (iConfigPointBio[index][7] > 0)
			ch->AddAffect(iAffectBiolog[index], aApplyInfo[iConfigPointBio[index][6]].bPointType, iConfigPointBio[index][7], 0, 60*60*60*365, 0, false);


		ch->ChatPacket(CHAT_TYPE_NOTICE, "Ai terminat o misiune din biolog!");

	}
	else{
        ch->RemoveAffect(AFFECT_RESEARCHER_ELIXIR);
		ch->ChatPacket(CHAT_TYPE_INFO, "Un obiect a fost adaugat la misiunea de biolog!");
    }

	int iValue = pPC->GetFlag("biolog.complete");

	char szBuf2[30];
	snprintf(szBuf2, sizeof(szBuf2), "biolog_%d.completate", iValue);
	iCollect = pPC->GetFlag(szBuf2);

	if (iValue >= MISSION_MAX_BIOLOG)
	{
		ch->ChatPacket(CHAT_TYPE_NOTICE, "Ai terminat toate misiunile biologului!");
		pPC->SetFlag("biolog.complete.mission", 1);
		return;
	}

	packet.iTimeLeft = iConfigBioTimeWait[iValue] + get_global_time();
	packet.iRewardItem = iConfigRewardBIO[iValue];
	for (int i = 0; i < 8; ++i)
		packet.iRewardPoints[i] = iConfigPointBio[iValue][i];
	packet.iReqItem[0] = iConfigNeedItemBIO[iValue][0];
	packet.iReqItem[1] = iConfigNeedItemBIO[iValue][1];
	packet.iReqItem[2] = iConfigNeedItemBIO[iValue][1] - iCollect;
	packet.iReqLevel = iConfigBioNeedLevel[iValue];
	packet.bInfoChecked = true;

	ch->GetDesc()->Packet(&packet, sizeof(TPacketGCSendInfoBiolog));
}


