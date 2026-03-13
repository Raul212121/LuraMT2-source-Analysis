#pragma once
#include "../eterBase/Singleton.h"

class CPythonLauncher : public CSingleton<CPythonLauncher>
{
	public:
		CPythonLauncher();
		virtual ~CPythonLauncher();

		static void Clear();

		bool Create(const char* c_szProgramName="eter.python");
		bool RunLine(const char* c_szLine) const;

#ifndef __USE_CYTHON__
		bool RunFile(const char* c_szFileName) const;
		bool RunMemoryTextFile(const char* c_szFileName, UINT uFileSize, const VOID* c_pvFileData) const;
#endif

	protected:
		PyObject* m_poModule;
		PyObject* m_poDic;
};
