#pragma once
#include "../common/tables.h"

class CBattlePass : public singleton<CBattlePass>
{
	public:
		CBattlePass();
		~CBattlePass() override;

        void BootBattlePassMap();
		const TBattlePassParser* GetBattlePassMap(uint32_t id);

		std::tuple<uint16_t, uint16_t> GetBattlePassRange(uint16_t id) const;

		const auto& GetRewardMap() const { return rewardMap; };

	private:
	    std::map<DWORD, TBattlePassParser> battlepassMap;
		std::map<uint16_t, std::vector<TRewardTableBP>> rewardMap;
};
