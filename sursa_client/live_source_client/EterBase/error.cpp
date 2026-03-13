#include "StdAfx.h"

#include <ctime>
#include <winsock.h>
#include <ImageHlp.h>
#include "Utils.h"
#include <iomanip>
#include <sstream>

void make_minidump(EXCEPTION_POINTERS* e)
{
	auto* hDbgHelp = LoadLibraryA("dbghelp");
	if (hDbgHelp == nullptr)
		return;
	auto* pMiniDumpWriteDump = reinterpret_cast<decltype(&MiniDumpWriteDump)>(GetProcAddress(hDbgHelp, "MiniDumpWriteDump"));
	if (pMiniDumpWriteDump == nullptr)
		return;
	// folder name
	std::string folder = "logs";
	CreateDirectoryA(folder.c_str(), nullptr);
	// time format
	auto t = std::time(nullptr);
	std::ostringstream timefmt;
	timefmt << std::put_time(std::localtime(&t), "%Y%m%d_%H%M%S");
	std::string executable_filename;
	GetExcutedFileName(executable_filename);
	std::string filename;
	GetOnlyFileName(executable_filename.c_str(), filename);
	// filename
	const std::string filename_dmp = folder + "\\"s + filename + "_"s + timefmt.str() + ".dmp";

	auto* hFile = CreateFileA(filename_dmp.c_str(), GENERIC_WRITE, FILE_SHARE_READ, nullptr, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, nullptr);
	if (hFile == INVALID_HANDLE_VALUE)
		return;

	MINIDUMP_EXCEPTION_INFORMATION exceptionInfo;
	exceptionInfo.ThreadId = GetCurrentThreadId();
	exceptionInfo.ExceptionPointers = e;
	exceptionInfo.ClientPointers = FALSE;

	auto dumped = pMiniDumpWriteDump(
		GetCurrentProcess(),
		GetCurrentProcessId(),
		hFile,
		MINIDUMP_TYPE(MiniDumpWithIndirectlyReferencedMemory | MiniDumpScanMemory),
		e ? &exceptionInfo : nullptr,
		nullptr,
		nullptr);

	CloseHandle(hFile);
	const auto errMsg = "The application has crashed and will now close.\n"s + filename_dmp;
	MessageBox(nullptr, errMsg.c_str(), filename.c_str(), MB_ICONSTOP);
}

long __stdcall EterExceptionFilter(_EXCEPTION_POINTERS* pExceptionInfo)
{
	make_minidump(pExceptionInfo);
	return EXCEPTION_EXECUTE_HANDLER;
}

void SetEterExceptionHandler()
{
	SetUnhandledExceptionFilter(EterExceptionFilter);
}
