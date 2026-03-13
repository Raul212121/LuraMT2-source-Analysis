#pragma once

class CPythonBattlePass : public CSingleton<CPythonBattlePass>
{
public:
	CPythonBattlePass();
	virtual ~CPythonBattlePass();

	bool	Initialize(const char* path);
	void	Destroy();
	
	void UpdateBattlePass(const TBattlePass& info);
	const TBattlePassParser* GetBattlePassMapReward(uint32_t pass) const;
	uint16_t GetBattlePassMapSize() { return battlepassMap.size();  }

	const TBattlePassParser* GetBattlePassMap(uint32_t id);
	const auto& GetRewardMap() const { return rewardMap; };

private:
	std::map<DWORD, TBattlePassParser> battlepassMap = {};
	std::map<uint16_t, std::vector<TRewardTableBP>> rewardMap;

};


