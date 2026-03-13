#ifndef __INC_MESSENGER_MANAGER_H
#define __INC_MESSENGER_MANAGER_H

#include "db.h"
#include "packet.h"
class MessengerManager : public singleton<MessengerManager>
{
	public:
		typedef std::string keyT;
		typedef const std::string & keyA;

		MessengerManager();
		virtual ~MessengerManager();

	public:
		void	P2PLogin(keyA account);
		void	P2PLogout(keyA account);

		void	Login(keyA account);
		void	Logout(keyA account);
		bool IsInFriendList(const std::string& account, const std::string& companion);
		void	RequestToAdd(LPCHARACTER ch, LPCHARACTER target);
		bool	AuthToAdd(keyA account, keyA companion, bool bDeny); // @fixme130 void -> bool

		void	__AddToList(keyA account, keyA companion);
		void	AddToList(keyA account, keyA companion);

		void	__RemoveFromList(keyA account, keyA companion);
		void	RemoveFromList(keyA account, keyA companion);

		void	RemoveAllList(keyA account);

		void	Initialize();

	private:
		void	SendList(keyA account);
		void	SendLogin(keyA account, keyA companion);
		void	SendLogout(keyA account, keyA companion);

		void	LoadList(SQLMsg * pmsg);
		void	Destroy();

		std::set<keyT>			m_set_loginAccount;
		std::map<keyT, std::set<keyT> >	m_Relation;
		std::map<keyT, std::set<keyT> >	m_InverseRelation;
		std::set<DWORD>			m_set_requestToAdd;

#ifdef ENABLE_MESSENGER_TEAM
	public:
		void ClearTeamList();
		void PushTeamList(const char* c_szName);
		void UpdateTeamList();
	private:
		void UpdateTeam(keyA account);
		void SendTeamList(keyA account, bool isReload);
		TTeamMessenger* GetTeamMember(keyA account);
		std::vector<TTeamMessenger> m_vecTeamList;
#endif // ENABLE_MESSENGER_TEAM
#ifdef ENABLE_MESSENGER_BLOCK
	public:
		void __AddToBlockList(const std::string& account, const std::string& companion);
		void AddToBlockList(const std::string& account, const std::string& companion);

		void __RemoveFromBlockList(const std::string& account, const std::string& companion);
		bool IsBlocked(const std::string& account, const std::string& companion);
		void RemoveFromBlockList(const std::string& account, const std::string& companion);
		void RemoveAllBlockList(const std::string& account);
	private:
		void SendBlockList(const std::string& account);
		void SendBlockLogin(const std::string& account, const std::string& companion);
		void SendBlockLogout(const std::string& account, const std::string& companion);

		void LoadBlockList(SQLMsg* pmsg);
	private:
		std::map<std::string, std::set<std::string>> m_BlockRelation;
		std::map<std::string, std::set<std::string>> m_InverseBlockRelation;
		std::set<DWORD> m_set_requestToBlockAdd;
#endif
};

#endif
