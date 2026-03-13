#include "StdAfx.h"
#include "PythonApplication.h"
#include "ProcessScanner.h"
#include "resource.h"


#ifdef _DEBUG
#include <crtdbg.h>
#endif

#ifdef ENABLE_HWID_BAN_SYSTEM
#include "HWIDManager.h"
#endif

#include "../EterFSLib/FileSystemIncl.hpp"
#include "../eterLib/Util.h"
#include "../CWebBrowser/CWebBrowser.h"
#include "../eterBase/CPostIt.h"

#include "CheckLatestFiles.h"
#ifdef ENABLE_CRASH_RPT
#include <CrashRpt.h>
#endif

#include <tbb/parallel_for.h>

#if defined(CHECK_WEB_URL)
#include "check_url.h"
#endif

#ifdef max
#undef max
#endif

#ifdef min
#undef min
#endif

#include <rapidjson/document.h>
#include <rapidjson/error/en.h>

#ifdef DISTRIBUTE
#include <xorstr.hpp>
#endif

extern "C" {
extern int _fltused;
volatile int _AVOID_FLOATING_POINT_LIBRARY_BUG = _fltused;
__declspec(dllexport) DWORD NvOptimusEnablement = 0x00000001;
__declspec(dllexport) int AmdPowerXpressRequestHighPerformance = 1;
};

#pragma comment(linker, "/NODEFAULTLIB:libci.lib")

#ifdef __USE_CYTHON__
extern "C" {
	void initrootlib();
	void initsystem();
}
#pragma comment( lib, "rootlib.lib" )
#endif

#pragma comment( lib, "version.lib" )
#pragma comment(lib, "cryptopp-static.lib")

#if GrannyProductMinorVersion==4
#pragma comment( lib, "granny2.4.0.10.lib" )
#elif GrannyProductMinorVersion==7
#pragma comment( lib, "granny2.7.0.30.lib" )
#elif GrannyProductMinorVersion==8
#pragma comment( lib, "granny2.8.49.0.lib" )
#elif GrannyProductMinorVersion==9
#pragma comment( lib, "granny2.9.12.0.lib" )
#elif GrannyProductMinorVersion==11
#pragma comment( lib, "granny2.11.8.0.lib" )
#else
#error "unknown granny version"
#endif

#ifdef _DEBUG
#pragma comment( lib, "python27_d.lib" )
#pragma comment( lib, "jpegd.lib" )
#pragma comment( lib, "lz4d.lib")
#pragma comment( lib, "xxhashd.lib")
#else
#pragma comment( lib, "python27.lib" )
#pragma comment( lib, "jpeg.lib" )
#pragma comment( lib, "lz4.lib")
#pragma comment( lib, "xxhash.lib")
#endif
#pragma comment( lib, "imagehlp.lib" )
#pragma comment( lib, "devil.lib" )

#pragma comment( lib, "mss32.lib" )
#pragma comment( lib, "winmm.lib" )
#pragma comment( lib, "imm32.lib" )
#pragma comment( lib, "oldnames.lib" )
#pragma comment( lib, "SpeedTreeRT.lib" )
#pragma comment( lib, "dinput8.lib" )
#pragma comment( lib, "dxguid.lib" )
#pragma comment( lib, "ws2_32.lib" )
#pragma comment( lib, "strmiids.lib" )
#pragma comment( lib, "ddraw.lib" )
#pragma comment( lib, "dmoguids.lib" )
#ifdef __ENABLE_NEW_OFFLINESHOP__
#pragma comment( lib, "shlwapi.lib" )
#pragma comment( lib, "libconfig.lib" )
#pragma comment( lib, "libconfig++.lib" )
#endif

#pragma comment( lib, "libcurl.lib" )

#include <cstdlib>
bool __IS_TEST_SERVER_MODE__=false;

extern bool SetDefaultCodePage(DWORD codePage);


int Setup(LPSTR lpCmdLine); // Internal function forward

static bool PackInitialize(CFile& file, FileSystemManager* file_system)
{
	rapidjson::Document document;
	document.Parse(reinterpret_cast<const char*>(file.GetData()));

	if (document.HasParseError())
	{
		TraceError("%ls parse failed! Error: %s offset: %u", file.GetFileName().c_str(), GetParseError_En(document.GetParseError()), document.GetErrorOffset());
		return false;
	}

	if (!document.HasMember("pack_dir"))
	{
		TraceError("%ls has no member `pack_dir`", file.GetFileName().c_str());
		return false;
	}

	if (!document.HasMember("files"))
	{
		TraceError("%ls has no member `files`", file.GetFileName().c_str());
		return false;
	}

	if (!document["pack_dir"].IsString())
	{
		TraceError("%ls type member `pack_dir` is not string", file.GetFileName().c_str());
		return false;
	}

	if (!document["files"].IsArray())
	{
		TraceError("%ls type member `files` is not array", file.GetFileName().c_str());
		return false;
	}

	const std::string pack_dir = document["pack_dir"].GetString();
	const auto& files = document["files"];

	parallel_for(tbb::blocked_range<int32_t>(0, files.Size()),
		[&](const tbb::blocked_range<int32_t> r)
		{
			for (auto i = r.begin(); i < r.end(); ++i)
			{
				if (!files[i].IsString())
					continue;

				const auto& name = pack_dir + files[i].GetString() + ".pak";
				const auto& key = file_system->GetArchiveKey(name);
				if (!file_system->AddArchive(name, key)) {
					abort();
				}
			}
			return true;
		}
	);
	return true;
}

bool RunMainScript(CPythonLauncher& pyLauncher, const char* lpCmdLine)
{
	initServerStateChecker();
	initpack();
	initdbg();
	initime();
	initgrp();
	initgrpImage();
	initgrpText();
	initwndMgr();
	initudp();
	initapp();
	initsystemSetting();
#ifdef INGAME_WIKI
	initWiki();
#endif
	initchr();
	initchrmgr();
	initPlayer();
	initItem();
	initNonPlayer();
	initTrade();
	initChat();
	initTextTail();
	initnet();
	initMiniMap();
	initProfiler();
	initEvent();
	initeffect();
	initfly();
	initsnd();
	initshop();
	initskill();
	initquest();
	initBackground();
	initMessenger();
	initsafebox();
	initguild();
#ifdef ENABLE_SWITCHBOT
	initSwitchbot();
#endif

#ifdef __ENABLE_NEW_OFFLINESHOP__
	initofflineshop();
#endif
#ifdef ENABLE_BATTLE_PASS
	initBattlePass();
#endif
    PyObject * builtins = PyImport_ImportModule("__builtin__");

#ifdef _DEBUG
	PyModule_AddIntConstant(builtins, "__DEBUG__", 1);
#else
	PyModule_AddIntConstant(builtins, "__DEBUG__", 0);
#endif

#ifdef __USE_CYTHON__
	PyModule_AddIntConstant(builtins, "__USE_CYTHON__", 1);
#else
	PyModule_AddIntConstant(builtins, "__USE_CYTHON__", 0);
#endif

#ifdef __USE_CYTHON__
	initrootlib();
	initsystem();
	PyErr_Print();
#else
	PyModule_AddStringConstant(builtins, "__COMMAND_LINE__", lpCmdLine);
	const char* filename = "root/system.py";
	if (!pyLauncher.RunFile(filename))
	{
		TraceError("Failed to run file %s", filename);
		std::system("PAUSE");
		return false;
	}
#endif

	return true;
}

bool Main(HINSTANCE hInstance, LPSTR lpCmdLine)
{
#if defined(CHECK_WEB_URL)
	if (!URL_CheckWebResponse())
		return false;
#endif

	DWORD dwRandSeed=time(nullptr)+DWORD(GetCurrentProcess());
	srandom(dwRandSeed);
	srand(random());

	SetLogLevel(1);

#ifndef __VTUNE__
	ilInit();
#endif
	if (!Setup(lpCmdLine))
		return false;

#ifdef _DEBUG
	OpenConsoleWindow();
	OpenLogFile(true); // true == uses syserr.txt and log.txt
#else
	OpenLogFile(false); // false == uses syserr.txt only
#endif

	static CLZO				lzo;
	FileSystemManager file_system;

#ifdef ENABLE_HWID_BAN_SYSTEM
	static HWIDMANAGER		hwidManager;
#endif

	CTextFileLoader::SetCacheMode();
	CSoundData::SetPackMode();

	if (!file_system.InitializeFSManager(
#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		FILE_FLAG_XTEA
#endif
	))
	{
		LogBox("FileSystem Initialization failed");
		return false;
	}

#ifdef DISTRIBUTE
	file_system.AddToDiskBlacklist(xorstr_("py"));
	file_system.AddToDiskBlacklist(xorstr_("pyc"));
#endif

	CFile file;
	const std::string pack_file = "packs.json";
	if (!file_system.OpenFile(pack_file, file))
	{
		TraceError("Failed to open %s", pack_file.c_str());
		file.Close();
		return false;
	}

	if (!PackInitialize(file, &file_system))
	{
		LogBox("Pack Initialization failed.");
		file.Close();
		return false;
	}

	if(LocaleService_LoadGlobal(hInstance))
		SetDefaultCodePage(LocaleService_GetCodePage());

	CPythonApplication * app = new CPythonApplication;

	app->Initialize(hInstance);

	bool ret=false;
	{
		CPythonLauncher pyLauncher;
		if (pyLauncher.Create())
		{
			ret=RunMainScript(pyLauncher, lpCmdLine);
		}

		app->Clear();

		timeEndPeriod(1);
		CPythonLauncher::Clear();
	}

	app->Destroy();
	delete app;

	return ret;
}

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	CreateDirectoryA("logs", nullptr);

#ifdef ENABLE_CRASH_RPT
	crash_rpt::CrashRpt g_crashRpt(
		"9e3f5dec-41e0-4eca-b201-1939b30eb6b6",
		L"Sinner2 Crash Reporter",
		L""
	);
	g_crashRpt.AddFileToReport(L"syserr.txt", nullptr);
	//g_crashRpt.AddFileToReport(L"logs/fs_log.txt", nullptr);
#endif

#ifdef _DEBUG
	_CrtSetDbgFlag( _CRTDBG_ALLOC_MEM_DF | _CRTDBG_CHECK_CRT_DF | _CRTDBG_LEAK_CHECK_DF );

#endif

	LocaleService_LoadConfig("locale.cfg");
	SetDefaultCodePage(LocaleService_GetCodePage());

	WebBrowser_Startup(hInstance);

	Main(hInstance, lpCmdLine);

	WebBrowser_Cleanup();

	::CoUninitialize();

	return 0;
}


int Setup(LPSTR lpCmdLine)
{
	TIMECAPS tc;
	UINT wTimerRes;

	if (timeGetDevCaps(&tc, sizeof(TIMECAPS)) != TIMERR_NOERROR)
		return 0;

	wTimerRes = MINMAX(tc.wPeriodMin, 1, tc.wPeriodMax);
	timeBeginPeriod(wTimerRes);

	return 1;
}

