#include "FileNameHelper.hpp"
#include "Constants.hpp"
#include "xxhash.h"
#include <cstring>
#include <algorithm>

namespace FileSystem
{
	CFileName::CFileName()
		: m_hash(0)
	{
	}

	CFileName::CFileName(const std::wstring& path)
		: m_hash(0)
	{
		Set(path, path.length());
	}

	CFileName::CFileName(const std::string& path)
		: m_hash(0)
	{
		Set(path, path.length());
	}

	CFileName::CFileName(const wchar_t* path)
		: m_hash(0)
	{
		Set(path, std::wcslen(path));
	}

	CFileName::CFileName(const char* path)
		: m_hash(0)
	{
		Set(path, std::strlen(path));
	}

	CFileName::CFileName(const uint32_t hash)
	{
		m_hash = hash;
		m_pathW.clear();
		m_pathA.clear();
	}

	auto& CFileName::operator=(const std::wstring& path)
	{
		Set(path, path.length());
		return *this;
	}

	auto& CFileName::operator=(const std::string& path)
	{
		Set(path, path.length());
		return *this;
	}

	auto& CFileName::operator=(const wchar_t* path)
	{
		Set(path, std::wcslen(path));
		return *this;
	}

	auto& CFileName::operator=(const char* path)
	{
		Set(path, std::strlen(path));
		return *this;
	}

	auto& CFileName::operator=(const uint32_t hash)
	{
		m_hash = hash;
		m_pathW.clear();
		m_pathA.clear();
		return *this;
	}

	void CFileName::Set(const std::wstring& path, uint32_t length)
	{
		m_pathW.resize(length);

		m_pathW = path;
		for (auto& i : m_pathW)
		{
			if (i == L'\\')
				i = L'/';
		}
		std::transform(m_pathW.begin(), m_pathW.end(), m_pathW.begin(), ::tolower);

		m_hash = XXH32(m_pathW.data(), length * sizeof(wchar_t), static_cast<XXH32_hash_t>(FILE_NAME_MAGIC));
		m_pathA = std::string(m_pathW.begin(), m_pathW.end());
	}

	void CFileName::Set(const std::string& path, uint32_t length)
	{
		m_pathW.resize(length);

		m_pathW = std::wstring(path.begin(), path.end());
		for (auto& i : m_pathW)
		{
			if (i == L'\\')
				i = L'/';
		}
		std::transform(m_pathW.begin(), m_pathW.end(), m_pathW.begin(), ::tolower);

		m_hash = XXH32(m_pathW.data(), length * sizeof(wchar_t), static_cast<XXH32_hash_t>(FILE_NAME_MAGIC));
		m_pathA = std::string(m_pathW.begin(), m_pathW.end());
		// convert again instead of usage coming path argument, cuz it's required as lower
	}

	std::wstring CFileName::GetPathW() const
	{
		return m_pathW;
	}

	std::string CFileName::GetPathA() const
	{
		return m_pathA;
	}
}
