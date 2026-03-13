#pragma once

class CBiolog : public singleton<CBiolog>
{
	public:
		CBiolog();
		virtual ~CBiolog();

		void BiologMission(LPCHARACTER ch, int index);
		void BiologMissionActive(LPCHARACTER ch, int index);
		void ObjectDrop(LPCHARACTER pkChar, LPCHARACTER pkVictim, DWORD pkVictimVnum, int index);
		int GetReqItem(int iValue, int iCollect, int option);
		int GetReqLevel(int iValue);
		int GetRewardPoint(int iValue, int index);
		int GetRewardItem(int iValue);
};
