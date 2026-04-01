class CBiolog : public singleton<CBiolog>
{
	public:
		CBiolog();
		virtual ~CBiolog();

		void BiologMission(LPCHARACTER ch, int index);
		int GetReqItem(int iValue, int iCollect, int option);
		int GetReqLevel(int iValue);
		int GetRewardPoint(int iValue, int index);
		int GetRewardItem(int iValue);
};
