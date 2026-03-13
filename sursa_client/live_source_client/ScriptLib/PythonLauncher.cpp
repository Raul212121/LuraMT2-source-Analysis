#include "StdAfx.h"
#include "../EterFSLib/FileSystemIncl.hpp"

#include "PythonLauncher.h"

CPythonLauncher::CPythonLauncher() : m_poModule(nullptr), m_poDic(nullptr)
{
	Py_NoSiteFlag++;
	Py_NoUserSiteDirectory++;
	Py_IgnoreEnvironmentFlag++;
	Py_DontWriteBytecodeFlag++;

#ifdef _DEBUG
	Py_VerboseFlag++;
	//Py_Py3kWarningFlag++;
#endif

#ifndef DISTRIBUTE
	Py_TabcheckFlag++;
	Py_BytesWarningFlag++;
	Py_InteractiveFlag++;
#else
	Py_OptimizeFlag++;
#endif

	Py_Initialize();
}

CPythonLauncher::~CPythonLauncher()
{
	Clear();
}

void CPythonLauncher::Clear()
{
	Py_Finalize();
}

bool CPythonLauncher::Create(const char* c_szProgramName)
{
	Py_SetProgramName(const_cast<char*>(c_szProgramName));

	m_poModule = PyImport_AddModule("__main__");

	if (!m_poModule)
		return false;

	m_poDic = PyModule_GetDict(m_poModule);

    PyObject * builtins = PyImport_ImportModule("__builtin__");
	PyModule_AddIntConstant(builtins, "TRUE", 1);
	PyModule_AddIntConstant(builtins, "FALSE", 0);
    PyDict_SetItemString(m_poDic, "__builtins__", builtins);
	Py_DECREF(builtins);

	if (!RunLine("import __main__"))
		return false;

	if (!RunLine("import sys"))
		return false;

	return true;
}

#ifndef __USE_CYTHON__
bool CPythonLauncher::RunMemoryTextFile(const char* c_szFileName, UINT uFileSize, const VOID* c_pvFileData) const
{
	const auto c_pcFileData = static_cast<const CHAR*>(c_pvFileData);

	std::string stConvFileData;
	stConvFileData.reserve(uFileSize);
	stConvFileData+="exec(compile('''";

	// ConvertPythonTextFormat
	{
		for (UINT i=0; i<uFileSize; ++i)
		{
			if (c_pcFileData[i]!=13)
				stConvFileData+=c_pcFileData[i];
		}
	}

	stConvFileData+= "''', ";
	stConvFileData+= "'";
	stConvFileData+= c_szFileName;
	stConvFileData+= "', ";
	stConvFileData+= "'exec'))";

	const CHAR* c_pcConvFileData=stConvFileData.c_str();
	return RunLine(c_pcConvFileData);
}

bool CPythonLauncher::RunFile(const char* c_szFileName) const
{
	const auto file = PackGet(c_szFileName);
	return file ? RunMemoryTextFile(c_szFileName, file->get_size(), file->get_data()) : false;
}
#endif

bool CPythonLauncher::RunLine(const char* c_szSrc) const
{
	PyObject * v = PyRun_String(c_szSrc, Py_file_input, m_poDic, m_poDic);

	if (!v)
	{
		PyErr_Print();
		return false;
	}

	Py_DECREF(v);
	return true;
}

