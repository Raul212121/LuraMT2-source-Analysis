#include "stdafx.h"
#include "constants.h"
#include "config.h"
#include "input.h"
#include "desc_client.h"
#include "desc_manager.h"
#include "db.h"

// #define ENABLE_ACCOUNT_W_SPECIALCHARS
static bool FN_IS_VALID_LOGIN_STRING(const char *str)
{
	if (!str || !*str)
		return false;

	if (strlen(str) < 2)
		return false;

	for (const char* tmp = str; *tmp; ++tmp)
	{
		if (isdigit(*tmp) || isalpha(*tmp))
			continue;

#ifdef ENABLE_ACCOUNT_W_SPECIALCHARS
		switch (*tmp)
		{
			case ' ':
			case '_':
			case '-':
			case '.':
			case '!':
			case '@':
			case '#':
			case '$':
			case '%':
			case '^':
			case '&':
			case '*':
			case '(':
			case ')':
				continue;
		}
#endif
		return false;
	}

	return true;
}

CInputAuth::CInputAuth()
{
}

void CInputAuth::Login(LPDESC d, const char * c_pData)
{
	TPacketCGLogin3 * pinfo = (TPacketCGLogin3 *) c_pData;

	if (!g_bAuthServer)
	{
		sys_err ("CInputAuth class is not for game server. IP %s might be a hacker.",
			inet_ntoa(d->GetAddr().sin_addr));
		d->DelayedDisconnect(5);
		return;
	}

	char login[LOGIN_MAX_LEN + 1];
	trim_and_lower(pinfo->login, login, sizeof(login));

	char passwd[PASSWD_MAX_LEN + 1];
	strlcpy(passwd, pinfo->passwd, sizeof(passwd));

	sys_log(0, "InputAuth::Login : %s(%d) desc %p",
			login, strlen(login), get_pointer(d));

	// check login string
	if (false == FN_IS_VALID_LOGIN_STRING(login))
	{
		sys_log(0, "InputAuth::Login : IS_NOT_VALID_LOGIN_STRING(%s) desc %p",
				login, get_pointer(d));
		LoginFailure(d, "NOID");
		return;
	}

	if (g_bNoMoreClient)
	{
		LoginFailure(d, "SHUTDOWN");
		return;
	}

	//std::string game_version = pinfo->game_version;
	//if (game_version.empty() && !test_server)
	//{
	//	LoginFailure(d, "VERSION");
	//	return;
	//}

#ifdef ENABLE_HWID_BAN_SYSTEM
	const auto isValidHWID = [&](const char* cpu_id, const char* hdd_serial, const char* mac_addr) {
		/*
		if (!cpu_id || !*cpu_id)
		{
			sys_err("login(%s) cpu_id is null", login);
			return false;
		}

		if (!hdd_serial || !*hdd_serial)
		{
			sys_err("login(%s) hdd_serial is null", login);
			return false;
		}

		if (!mac_addr || !*mac_addr)
		{
			sys_err("login(%s) mac_addr is null", login);
			return false;
		}
		*/
		return true;
	};

	if (!isValidHWID(pinfo->cpu_id, pinfo->hdd_serial, pinfo->mac_addr))
	{
		LoginFailure(d, "BESAMEKEY");
		return;
	}
#endif

#ifdef ENABLE_ANTI_LOGIN_BRUTEFORCE
	if (!DESC_MANAGER::instance().LoginCheckByLogin(login))
	{
		LoginFailure(d, "BESAMEKEY");
		return;
	}

	if (!DESC_MANAGER::instance().LoginCheckByIP(d->GetHostName()))
	{
		LoginFailure(d, "BESAMEKEY");
		return;
	}
#endif

	if (DESC_MANAGER::instance().FindByLoginName(login))
	{
		LoginFailure(d, "ALREADY");
		return;
	}

	DWORD dwKey = DESC_MANAGER::instance().CreateLoginKey(d);
	DWORD dwPanamaKey = dwKey ^ pinfo->adwClientKey[0] ^ pinfo->adwClientKey[1] ^ pinfo->adwClientKey[2] ^ pinfo->adwClientKey[3];
	d->SetPanamaKey(dwPanamaKey);

	sys_log(0, "InputAuth::Login : key %u:0x%x login %s", dwKey, dwPanamaKey, login);

	TPacketCGLogin3 * p = M2_NEW TPacketCGLogin3;
	memcpy(p, pinfo, sizeof(TPacketCGLogin3));

	char szPasswd[PASSWD_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(szPasswd, sizeof(szPasswd), passwd, strlen(passwd));

	char szLogin[LOGIN_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(szLogin, sizeof(szLogin), login, strlen(login));

#ifdef ENABLE_HWID_BAN_SYSTEM
	char cpu_id[CPU_ID_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(cpu_id, sizeof(cpu_id), pinfo->cpu_id, strlen(pinfo->cpu_id));

	char hdd_serial[HDD_SERIAL_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(hdd_serial, sizeof(hdd_serial), pinfo->hdd_serial, strlen(pinfo->hdd_serial));

	char mac_addr[MAC_ADDR_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(mac_addr, sizeof(mac_addr), pinfo->mac_addr, strlen(pinfo->mac_addr));
#endif

	DBManager::instance().ReturnQuery(QID_AUTH_LOGIN, dwKey, p,
		"SELECT PASSWORD('%s'),a.password,a.social_id,a.id,a.status,a.availDt - NOW() > 0, v.version,"

#ifdef ENABLE_HWID_BAN_SYSTEM
		"(SELECT COUNT(*) FROM banned_hwid_list WHERE hwid = '%s') AS hwid_banned,"
		"(SELECT COUNT(*) FROM banned_hdd_list WHERE hdd_serial = '%s') AS hdd_banned,"
		"(SELECT COUNT(*) FROM banned_cpu_list WHERE cpu_id = '%s') AS cpu_banned,"
#endif

		"UNIX_TIMESTAMP(a.silver_expire),"
		"UNIX_TIMESTAMP(a.gold_expire),"
		"UNIX_TIMESTAMP(a.safebox_expire),"
		"UNIX_TIMESTAMP(a.autoloot_expire),"
		"UNIX_TIMESTAMP(a.fish_mind_expire),"
		"UNIX_TIMESTAMP(a.marriage_fast_expire),"
		"UNIX_TIMESTAMP(a.money_drop_rate_expire),"
		"UNIX_TIMESTAMP(a.create_time)"
		" FROM account AS a, game_version AS v WHERE a.login='%s'",
		szPasswd,
#ifdef ENABLE_HWID_BAN_SYSTEM
		mac_addr, hdd_serial, cpu_id,
#endif
		szLogin);
}

int CInputAuth::Analyze(LPDESC d, BYTE bHeader, const char* c_pData)
{
	if (!g_bAuthServer)
	{
		sys_err("CInputAuth class is not for game server. IP %s might be a hacker.",
			inet_ntoa(d->GetAddr().sin_addr));
		d->DelayedDisconnect(5);
		return 0;
	}

	if (test_server)
		sys_log(0, " InputAuth Analyze Header[%d] ", bHeader);

	switch (bHeader)
	{
	case HEADER_CG_PONG:
		Pong(d);
		break;

	case HEADER_CG_LOGIN3:
		Login(d, c_pData);
		break;

	case HEADER_CG_HANDSHAKE:
		break;

	default:
		{
			sys_err("This phase does not handle this header %d (0x%x)(phase: AUTH) (fd %d)", bHeader, bHeader, d->GetSocket());
			d->SetPhase(PHASE_CLOSE);
			return 0;
		}
	}

	return 0;
}
