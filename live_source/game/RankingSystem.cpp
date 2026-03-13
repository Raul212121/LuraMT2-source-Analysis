#include "stdafx.h"
#include "desc_client.h"
#include "desc_manager.h"
#include "char_manager.h"
#include "char.h"
#include "RankingSystem.h"
#include "guild.h"

CRankingSystem::CRankingSystem()
{
    m_RankingVector.clear();
}
CRankingSystem::~CRankingSystem() {

}

void CRankingSystem::UpdateRankingdata(LPCHARACTER pkChar, uint8_t type, uint64_t points)
{
    if (!pkChar || points == 0)
        return;

    if (pkChar->GetGMLevel() > GM_PLAYER)
        return;

    const auto& it = m_RankingVector.find(pkChar->GetPlayerID());
    if (it == m_RankingVector.end())
	{
        TRankingData data;
        data.empire = pkChar->GetEmpire();
        data.pid = pkChar->GetPlayerID();
        strcpy(data.name, pkChar->GetName());
        if (pkChar->GetGuild())
            strcpy(data.guild, pkChar->GetGuild()->GetName());
        else
            strcpy(data.guild, "-");
        memset(&data.values, 0, sizeof(data.values));
        data.values[type] = points;
        m_RankingVector.insert({data.pid, data});

		return;
    }
	it->second.values[type] += points;
}

void CRankingSystem::UpdatePlayerInfo(LPCHARACTER pkChar)
{
    if (!pkChar)
        return;

    if (pkChar->GetGMLevel() > GM_PLAYER)
        return;

    const auto& it = m_RankingVector.find(pkChar->GetPlayerID());
    if (it == m_RankingVector.end())
	{
        TRankingData data;
        data.empire = pkChar->GetEmpire();
        data.pid = pkChar->GetPlayerID();
        strcpy(data.name, pkChar->GetName());
        if (pkChar->GetGuild())
            strcpy(data.guild, pkChar->GetGuild()->GetName());
        else
            strcpy(data.guild, "-");
        memset(&data.values, 0, sizeof(data.values));
        m_RankingVector.insert({data.pid, data});
    }
	else
	{
        it->second.empire = pkChar->GetEmpire();
        it->second.pid = pkChar->GetPlayerID();
        strcpy(it->second.name, pkChar->GetName());
        if (pkChar->GetGuild())
            strcpy(it->second.guild, pkChar->GetGuild()->GetName());
        else
            strcpy(it->second.guild, "-");
    }
}

void CRankingSystem::FlushToDatabase() {
    BYTE bSubHeader = 1;
    DWORD rankingCount = m_RankingVector.size();

    db_clientdesc->DBPacketHeader(HEADER_GD_RANKING_SYSTEM, 0, sizeof(BYTE) +sizeof(DWORD) + sizeof(TRankingData) * rankingCount);

    db_clientdesc->Packet(&bSubHeader, sizeof(BYTE));
    db_clientdesc->Packet(&rankingCount, sizeof(DWORD));

    for (const auto& rank : m_RankingVector)
        db_clientdesc->Packet(&rank.second, sizeof(TRankingData));
    m_RankingVector.clear();
}
