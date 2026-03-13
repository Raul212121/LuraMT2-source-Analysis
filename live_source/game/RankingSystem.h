#pragma once


class CRankingSystem : public singleton<CRankingSystem> {
public:
    CRankingSystem();
    ~CRankingSystem();

    void UpdateRankingdata(LPCHARACTER pkChar, uint8_t type, uint64_t points);
    void UpdatePlayerInfo(LPCHARACTER pkChar);
    void FlushToDatabase();

private:
    std::multimap<DWORD, TRankingData> m_RankingVector;
};
