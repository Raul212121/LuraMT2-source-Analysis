#include "stdafx.h"
#include "constants.h"
#include "gm.h"
#include "buffer_manager.h"
#include "desc_client.h"
#include "log.h"
#include "config.h"
#include "p2p.h"
#include "crc32.h"
#include "char.h"
#include "char_manager.h"
#include "questmanager.h"
#include "packet.h"
#include "messenger_manager.h"

MessengerManager::MessengerManager()
{
}

MessengerManager::~MessengerManager()
{
}

void MessengerManager::Initialize()
{
}

void MessengerManager::Destroy()
{
#ifdef ENABLE_MESSENGER_TEAM
	m_vecTeamList.clear();
#endif // ENABLE_MESSENGER_TEAM
}

void MessengerManager::P2PLogin(MessengerManager::keyA account)
{
	Login(account);
}

void MessengerManager::P2PLogout(MessengerManager::keyA account)
{
	Logout(account);
}

void MessengerManager::Login(MessengerManager::keyA account)
{
	if (m_set_loginAccount.find(account) != m_set_loginAccount.end())
		return;

	 char _account[CHARACTER_NAME_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(_account, sizeof(_account), account.c_str(), account.size());
	if (account.compare(_account))
		return;

	DBManager::instance().FuncQuery([this](SQLMsg* msg) { LoadList(msg); },
			"SELECT account, companion FROM messenger_list%s WHERE account='%s'", get_table_postfix(), _account);

#if defined(ENABLE_MESSENGER_BLOCK)
	DBManager::instance().FuncQuery([this](SQLMsg* msg) { LoadBlockList(msg); },
		"SELECT `account`, `companion` FROM messenger_block_list%s WHERE `account` = '%s'", get_table_postfix(), _account);
#endif

	m_set_loginAccount.insert(_account);
#ifdef ENABLE_MESSENGER_TEAM
	SendTeamList(_account, false);
#endif // ENABLE_MESSENGER_TEAM
}

void MessengerManager::LoadList(SQLMsg * msg)
{
	if (nullptr == msg)
		return;

	if (nullptr == msg->Get())
		return;

	if (msg->Get()->uiNumRows == 0)
		return;

	std::string account;

	sys_log(1, "Messenger::LoadList");

	for (uint32_t i = 0; i < msg->Get()->uiNumRows; ++i)
	{
		MYSQL_ROW row = mysql_fetch_row(msg->Get()->pSQLResult);

		if (row[0] && row[1])
		{
			if (account.length() == 0)
				account = row[0];

			m_Relation[row[0]].insert(row[1]);
			m_InverseRelation[row[1]].insert(row[0]);
		}
	}

	SendList(account);

	for (const auto& companion : m_InverseRelation[account])
		SendLogin(companion, account);
}

void MessengerManager::Logout(MessengerManager::keyA account)
{
	if (m_set_loginAccount.find(account) == m_set_loginAccount.end())
		return;

	m_set_loginAccount.erase(account);

	for (const auto& it : m_InverseRelation[account])
		SendLogout(it, account);
	m_Relation.erase(account);

#ifdef ENABLE_MESSENGER_TEAM
	UpdateTeam(account);
#endif // ENABLE_MESSENGER_TEAM

#ifdef ENABLE_MESSENGER_BLOCK
	for (const auto& it : m_InverseBlockRelation[account])
		SendBlockLogout(it, account);
	m_BlockRelation.erase(account);
#endif
}

bool MessengerManager::IsInFriendList(const std::string& account, const std::string& companion)
{
	if (m_Relation.find(account) == m_Relation.end())
		return false;

	if (m_Relation[account].empty())
		return false;

	return m_Relation[account].find(companion) != m_Relation[account].end();
}

void MessengerManager::RequestToAdd(LPCHARACTER ch, LPCHARACTER target)
{
	if (!ch->IsPC() || !target->IsPC())
		return;

	if (quest::CQuestManager::instance().GetPCForce(ch->GetPlayerID())->IsRunning() == true)
	{
	    ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상대방이 친구 추가를 받을 수 없는 상태입니다."));
	    return;
	}

	if (quest::CQuestManager::instance().GetPCForce(target->GetPlayerID())->IsRunning() == true)
		return;

	DWORD dw1 = GetCRC32(ch->GetName(), strlen(ch->GetName()));
	DWORD dw2 = GetCRC32(target->GetName(), strlen(target->GetName()));

	char buf[64];
	snprintf(buf, sizeof(buf), "%u:%u", dw1, dw2);
	DWORD dwComplex = GetCRC32(buf, strlen(buf));

	m_set_requestToAdd.insert(dwComplex);

	target->ChatPacket(CHAT_TYPE_COMMAND, "messenger_auth %s", ch->GetName());
}

// @fixme130 void -> bool
bool MessengerManager::AuthToAdd(MessengerManager::keyA account, MessengerManager::keyA companion, bool bDeny)
{
	DWORD dw1 = GetCRC32(companion.c_str(), companion.length());
	DWORD dw2 = GetCRC32(account.c_str(), account.length());

	char buf[64];
	snprintf(buf, sizeof(buf), "%u:%u", dw1, dw2);
	DWORD dwComplex = GetCRC32(buf, strlen(buf));

	if (m_set_requestToAdd.find(dwComplex) == m_set_requestToAdd.end())
		return false;

	m_set_requestToAdd.erase(dwComplex);

	if (!bDeny)
	{
		AddToList(companion, account);
		AddToList(account, companion);
	}
	return true;
}

void MessengerManager::__AddToList(MessengerManager::keyA account, MessengerManager::keyA companion)
{
	m_Relation[account].insert(companion);
	m_InverseRelation[companion].insert(account);

	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : nullptr;

	if (d)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<메신져> %s 님을 친구로 추가하였습니다."), companion.c_str());
	}

	LPCHARACTER tch = CHARACTER_MANAGER::instance().FindPC(companion.c_str());

	if (tch)
		SendLogin(account, companion);
	else
		SendLogout(account, companion);
}

void MessengerManager::AddToList(MessengerManager::keyA account, MessengerManager::keyA companion)
{
	if (companion.empty() || account.empty())
		return;

	if (m_Relation[account].find(companion) != m_Relation[account].end())
		return;

	char _account[CHARACTER_NAME_MAX_LEN * 2 + 1];
	char _companion[CHARACTER_NAME_MAX_LEN * 2 + 1];

	DBManager::instance().EscapeString(_account, sizeof(_account), account.c_str(), account.size());
	DBManager::instance().EscapeString(_companion, sizeof(_companion), companion.c_str(), companion.size());
	if (account.compare(_account) || companion.compare(_companion))
		return;


	sys_log(1, "Messenger Add %s %s", account.c_str(), companion.c_str());
	DBManager::instance().Query("INSERT INTO messenger_list%s (account, companion, time) VALUES ('%s', '%s', NOW())",
			get_table_postfix(), _account, _companion);

	__AddToList(account, companion);

	TPacketGGMessenger p2ppck;

	p2ppck.bHeader = HEADER_GG_MESSENGER_ADD;
	strlcpy(p2ppck.szAccount, account.c_str(), sizeof(p2ppck.szAccount));
	strlcpy(p2ppck.szCompanion, companion.c_str(), sizeof(p2ppck.szCompanion));
	P2P_MANAGER::instance().Send(&p2ppck, sizeof(TPacketGGMessenger));
}

void MessengerManager::__RemoveFromList(MessengerManager::keyA account, MessengerManager::keyA companion)
{
	m_Relation[account].erase(companion);
	m_InverseRelation[companion].erase(account);

	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : nullptr;

	if (d)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<메신져> %s 님을 메신저에서 삭제하였습니다."), companion.c_str());

		BYTE bLen = companion.size();

		TPacketGCMessenger pack{};

		pack.header = HEADER_GC_MESSENGER;
		pack.subheader = MESSENGER_SUBHEADER_GC_REMOVE_FRIEND;
		pack.size = sizeof(TPacketGCMessenger) + sizeof(BYTE) + bLen;

		d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
		d->BufferedPacket(&bLen, sizeof(BYTE));
		d->Packet(companion.c_str(), companion.size());
	}
}

void MessengerManager::RemoveFromList(MessengerManager::keyA account, MessengerManager::keyA companion)
{
	if (companion.empty())
		return;

	if (account == companion)
		return;

	if (!IsInFriendList(account, companion))
		return;

	char _account[CHARACTER_NAME_MAX_LEN * 2 + 1];
	char _companion[CHARACTER_NAME_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(_account, sizeof(_account), account.c_str(), account.size());
	DBManager::instance().EscapeString(_companion, sizeof(_companion), companion.c_str(), companion.size());
	if (account.compare(_account) || companion.compare(_companion))
		return;


	sys_log(1, "Messenger Remove %s %s", account.c_str(), companion.c_str());
	DBManager::instance().Query("DELETE FROM messenger_list%s WHERE account='%s' AND companion = '%s'",
			get_table_postfix(), _account, _companion);

	__RemoveFromList(account, companion);

	TPacketGGMessenger p2ppck;

	p2ppck.bHeader = HEADER_GG_MESSENGER_REMOVE;
	strlcpy(p2ppck.szAccount, account.c_str(), sizeof(p2ppck.szAccount));
	strlcpy(p2ppck.szCompanion, companion.c_str(), sizeof(p2ppck.szCompanion));
	P2P_MANAGER::instance().Send(&p2ppck, sizeof(TPacketGGMessenger));
}

void MessengerManager::RemoveAllList(keyA account)
{
	if (m_Relation.find(account) == m_Relation.end())
		return;

	if (m_Relation[account].empty())
		return;

	std::set<keyT> company(m_Relation[account]);
	for (const auto& iter : company)
		RemoveFromList(account, iter);

	company.clear();

	char _account[CHARACTER_NAME_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(_account, sizeof(_account), account.c_str(), account.size());
	if (account.compare(_account))
		return;

	DBManager::instance().Query("DELETE FROM messenger_list%s WHERE account='%s' OR companion='%s'", get_table_postfix(), _account, _account);
}

void MessengerManager::SendList(MessengerManager::keyA account)
{
	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());

	if (!ch)
		return;

	LPDESC d = ch->GetDesc();

	if (!d)
		return;

	if (m_Relation.find(account) == m_Relation.end())
		return;

	if (m_Relation[account].empty())
		return;

	TPacketGCMessenger pack;

	pack.header		= HEADER_GC_MESSENGER;
	pack.subheader	= MESSENGER_SUBHEADER_GC_LIST;
	pack.size		= sizeof(TPacketGCMessenger);

	TPacketGCMessengerListOffline pack_offline;
	TPacketGCMessengerListOnline pack_online;

	TEMP_BUFFER buf(128 * 1024); // 128k

	auto it = m_Relation[account].begin(), eit = m_Relation[account].end();

	while (it != eit)
	{
		if (m_set_loginAccount.find(*it) != m_set_loginAccount.end())
		{
			pack_online.connected = 1;

			// Online
			pack_online.length = it->size();

			buf.write(&pack_online, sizeof(TPacketGCMessengerListOnline));
			buf.write(it->c_str(), it->size());
		}
		else
		{
			pack_offline.connected = 0;

			// Offline
			pack_offline.length = it->size();

			buf.write(&pack_offline, sizeof(TPacketGCMessengerListOffline));
			buf.write(it->c_str(), it->size());
		}

		++it;
	}

	pack.size += buf.size();

	d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
	d->Packet(buf.read_peek(), buf.size());
}

void MessengerManager::SendLogin(MessengerManager::keyA account, MessengerManager::keyA companion)
{
	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : nullptr;

	if (!d)
		return;

	if (!d->GetCharacter())
		return;

	if (ch->GetGMLevel() == GM_PLAYER && gm_get_level(companion.c_str()) != GM_PLAYER)
		return;

	BYTE bLen = companion.size();

	TPacketGCMessenger pack;

	pack.header			= HEADER_GC_MESSENGER;
	pack.subheader		= MESSENGER_SUBHEADER_GC_LOGIN;
	pack.size			= sizeof(TPacketGCMessenger) + sizeof(BYTE) + bLen;

	d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
	d->BufferedPacket(&bLen, sizeof(BYTE));
	d->Packet(companion.c_str(), companion.size());
}

void MessengerManager::SendLogout(MessengerManager::keyA account, MessengerManager::keyA companion)
{
	if (companion.empty())
		return;

	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : NULL;

	if (!d)
		return;

	BYTE bLen = companion.size();

	TPacketGCMessenger pack;

	pack.header		= HEADER_GC_MESSENGER;
	pack.subheader	= MESSENGER_SUBHEADER_GC_LOGOUT;
	pack.size		= sizeof(TPacketGCMessenger) + sizeof(BYTE) + bLen;

	d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
	d->BufferedPacket(&bLen, sizeof(BYTE));
	d->Packet(companion.c_str(), companion.size());
}


#ifdef ENABLE_MESSENGER_TEAM
void MessengerManager::ClearTeamList()
{
	m_vecTeamList.clear();
}

void MessengerManager::UpdateTeamList()
{
	std::for_each(m_set_loginAccount.begin(), m_set_loginAccount.end(), [&](const std::string& name) { SendTeamList(name, true); });
}

void MessengerManager::PushTeamList(const char* c_szName)
{
	if (GetTeamMember(c_szName) != nullptr)
		return;

	TTeamMessenger TeamMessenger = {};
	TeamMessenger.IsConnected = m_set_loginAccount.find(c_szName) != m_set_loginAccount.end();
	strlcpy(TeamMessenger.szName, c_szName, sizeof(TeamMessenger.szName));
	m_vecTeamList.emplace_back(TeamMessenger);
}

void MessengerManager::SendTeamList(keyA account, bool isReload)
{
	if (account.empty() || (!isReload && m_vecTeamList.empty()))
		return;

	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC desc = ch != nullptr ? ch->GetDesc() : nullptr;

	if (desc != nullptr)
	{
		std::for_each(m_vecTeamList.begin(), m_vecTeamList.end(), [&](TTeamMessenger& member) { member.IsConnected = m_set_loginAccount.find(member.szName) != m_set_loginAccount.end(); });

		TPacketGCMessenger pack{};
		pack.header = HEADER_GC_MESSENGER;
		pack.subheader = MESSENGER_SUBHEADER_GC_TEAM;
		pack.size = static_cast<uint16_t>(sizeof(TPacketGCMessenger) + (sizeof(TTeamMessenger) * m_vecTeamList.size()));

		TEMP_BUFFER buf;
		buf.write(&pack, sizeof(pack));
		if (!m_vecTeamList.empty())
			buf.write(&m_vecTeamList[0], static_cast<int>(sizeof(TTeamMessenger) * m_vecTeamList.size()));
		desc->Packet(buf.read_peek(), buf.size());
	}

	if (!isReload)
		UpdateTeam(account);
}

void MessengerManager::UpdateTeam(keyA account)
{
	TTeamMessenger* member = GetTeamMember(account);
	if (!member)
		return;

	member->IsConnected = m_set_loginAccount.find(account) != m_set_loginAccount.end();

	TPacketGCMessenger pack{};
	pack.header = HEADER_GC_MESSENGER;
	pack.subheader = MESSENGER_SUBHEADER_GC_TEAM_UPDATE;
	pack.size = sizeof(TPacketGCMessenger) + sizeof(TTeamMessenger);

	for (const auto & i : m_set_loginAccount)
	{
		if (strcmp(i.c_str(), account.c_str()) == 0)
			continue;

		LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(i.c_str());
		LPDESC desc = ch != nullptr ? ch->GetDesc() : nullptr;
		if (desc != nullptr)
		{
			desc->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
			desc->Packet(member, sizeof(TTeamMessenger));
		}
	}
}

TTeamMessenger* MessengerManager::GetTeamMember(keyA account)
{
	if (account.empty())
		return nullptr;

	auto iterator = m_vecTeamList.begin();
	while (iterator != m_vecTeamList.end())
	{
		auto& t = *iterator++;
		if (strcmp(t.szName, account.c_str()) == 0)
			return &t;
	}
	return nullptr;
}
#endif // ENABLE_MESSENGER_TEAM

#ifdef ENABLE_MESSENGER_BLOCK
void MessengerManager::SendBlockList(const std::string& account)
{
	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());

	if (!ch)
		return;

	LPDESC d = ch->GetDesc();

	if (!d)
		return;

	TPacketGCMessenger pack;

	pack.header = HEADER_GC_MESSENGER;
	pack.subheader = MESSENGER_SUBHEADER_GC_BLOCK_LIST;
	pack.size = sizeof(TPacketGCMessenger);

	TPacketGCMessengerBlockListOnline pack_online;
	TPacketGCMessengerBlockListOffline pack_offline;

	TEMP_BUFFER buf(128 * 1024);

	auto it = m_BlockRelation[account].begin(), eit = m_BlockRelation[account].end();

	while (it != eit)
	{
		if (m_set_loginAccount.find(*it) != m_set_loginAccount.end())
		{
			pack_online.connected = 1;
			pack_online.length = it->size();

			buf.write(&pack_online, sizeof(TPacketGCMessengerBlockListOnline));
			buf.write(it->c_str(), it->size());
		}
		else
		{
			pack_offline.connected = 0;
			pack_offline.length = it->size();

			buf.write(&pack_offline, sizeof(TPacketGCMessengerBlockListOffline));
			buf.write(it->c_str(), it->size());
		}

		++it;
	}

	pack.size += buf.size();

	d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
	d->Packet(buf.read_peek(), buf.size());
}

void MessengerManager::SendBlockLogin(const std::string& account, const std::string& companion)
{
	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : nullptr;

	if (!d)
		return;

	if (!d->GetCharacter())
		return;

	BYTE bLen = companion.size();

	TPacketGCMessenger pack;

	pack.header = HEADER_GC_MESSENGER;
	pack.subheader = MESSENGER_SUBHEADER_GC_BLOCK_LOGIN;
	pack.size = sizeof(TPacketGCMessenger) + sizeof(BYTE) + bLen;

	d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
	d->BufferedPacket(&bLen, sizeof(BYTE));
	d->Packet(companion.c_str(), companion.size());
}

void MessengerManager::SendBlockLogout(const std::string& account, const std::string& companion)
{
	if (companion.empty())
		return;

	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : nullptr;

	if (!d)
		return;

	BYTE bLen = companion.size();

	TPacketGCMessenger pack;

	pack.header = HEADER_GC_MESSENGER;
	pack.subheader = MESSENGER_SUBHEADER_GC_BLOCK_LOGOUT;
	pack.size = sizeof(TPacketGCMessenger) + sizeof(BYTE) + bLen;

	d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
	d->BufferedPacket(&bLen, sizeof(BYTE));
	d->Packet(companion.c_str(), companion.size());
}

void MessengerManager::LoadBlockList(SQLMsg* msg)
{
	if (nullptr == msg || nullptr == msg->Get() || msg->Get()->uiNumRows == 0)
		return;

	std::string account;

	for (uint32_t i = 0; i < msg->Get()->uiNumRows; ++i)
	{
		MYSQL_ROW row = mysql_fetch_row(msg->Get()->pSQLResult);

		if (row[0] && row[1])
		{
			if (account.empty())
				account = row[0];

			m_BlockRelation[row[0]].insert(row[1]);
			m_InverseBlockRelation[row[1]].insert(row[0]);
		}
	}

	SendBlockList(account);

	for (auto& it : m_InverseBlockRelation[account])
		SendBlockLogin(it, account);
}

void MessengerManager::__AddToBlockList(const std::string& account, const std::string& companion)
{
	m_BlockRelation[account].insert(companion);
	m_InverseBlockRelation[companion].insert(account);

	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : nullptr;

	if (d)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%s is now blocked."), companion.c_str());
	}

	LPCHARACTER tch = CHARACTER_MANAGER::instance().FindPC(companion.c_str());

	if (tch)
		SendBlockLogin(account, companion);
	else
		SendBlockLogout(account, companion);
}

void MessengerManager::AddToBlockList(const std::string& account, const std::string& companion)
{
	if (companion.empty())
		return;

	if (m_BlockRelation[account].find(companion) != m_BlockRelation[account].end())
		return;

	DBManager::instance().Query("INSERT INTO messenger_block_list%s (account, companion, time) VALUES ('%s', '%s', NOW())",
		get_table_postfix(), account.c_str(), companion.c_str());

	__AddToBlockList(account, companion);

	TPacketGGMessenger p2ppck;

	p2ppck.bHeader = HEADER_GG_MESSENGER_BLOCK_ADD;
	strlcpy(p2ppck.szAccount, account.c_str(), sizeof(p2ppck.szAccount));
	strlcpy(p2ppck.szCompanion, companion.c_str(), sizeof(p2ppck.szCompanion));
	P2P_MANAGER::instance().Send(&p2ppck, sizeof(TPacketGGMessenger));
}

void MessengerManager::__RemoveFromBlockList(const std::string& account, const std::string& companion)
{
	m_BlockRelation[account].erase(companion);
	m_InverseBlockRelation[companion].erase(account);

	LPCHARACTER ch = CHARACTER_MANAGER::instance().FindPC(account.c_str());
	LPDESC d = ch ? ch->GetDesc() : nullptr;

	if (d)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%s is no longer blocked."), companion.c_str());


		BYTE bLen = companion.size();

		TPacketGCMessenger pack{};

		pack.header = HEADER_GC_MESSENGER;
		pack.subheader = MESSENGER_SUBHEADER_GC_REMOVE_BLOCK;
		pack.size = sizeof(TPacketGCMessenger) + sizeof(BYTE) + bLen;

		d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
		d->BufferedPacket(&bLen, sizeof(BYTE));
		d->Packet(companion.c_str(), companion.size());
	}
}

bool MessengerManager::IsBlocked(const std::string& account, const std::string& companion)
{
	if (m_BlockRelation.empty() || m_BlockRelation.find(account) == m_BlockRelation.end())
		return false;

	for (const auto& it : m_BlockRelation[account])
	{
		if (it == companion)
			return true;
	}

	return false;
}

void MessengerManager::RemoveFromBlockList(const std::string& account, const std::string& companion)
{
	if (companion.empty() || account.empty())
		return;

	if (m_BlockRelation.find(account) == m_BlockRelation.end())
		return;

	std::set<std::string> company(m_BlockRelation[account]);
	if (company.find(companion) == company.end())
		return;

	char szCompanion[CHARACTER_NAME_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(szCompanion, sizeof(szCompanion), companion.c_str(), companion.length());
	DBManager::instance().Query("DELETE FROM messenger_block_list%s WHERE `account` = '%s' AND `companion` = '%s'",
		get_table_postfix(), account.c_str(), szCompanion);

	__RemoveFromBlockList(account, companion);

	TPacketGGMessenger p2ppck;

	p2ppck.bHeader = HEADER_GG_MESSENGER_BLOCK_REMOVE;
	strlcpy(p2ppck.szAccount, account.c_str(), sizeof(p2ppck.szAccount));
	strlcpy(p2ppck.szCompanion, companion.c_str(), sizeof(p2ppck.szCompanion));
	P2P_MANAGER::instance().Send(&p2ppck, sizeof(TPacketGGMessenger));
}

void MessengerManager::RemoveAllBlockList(keyA account)
{
	if (m_BlockRelation.find(account) == m_BlockRelation.end())
		return;

	std::set<std::string> company(m_BlockRelation[account]);
	if (company.empty())
		return;

	for (const auto& iter : company)
		RemoveFromList(account, iter);

	company.clear();

	DBManager::instance().Query("DELETE FROM messenger_block_list%s WHERE `account` = '%s' OR companion = '%s'", get_table_postfix(), account.c_str(), account.c_str());
}
#endif
