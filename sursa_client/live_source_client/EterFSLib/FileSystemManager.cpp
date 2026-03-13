#include "FileSystemManager.hpp"

#include <cassert>

#include "LogHelper.hpp"
#include "Constants.hpp"
#include "Keys.hpp"
#include "FileSystem.hpp"
#include "File.hpp"
#include "Utils.hpp"

#include <ppl.h>
#include <lzo/lzo2a.h>
#include <filesystem>
#include <utility>

#include <cryptopp/modes.h>
#include <cryptopp/tea.h>
#include <cryptopp/blowfish.h>

namespace FileSystem
{
	static FileSystemManager* gs_pFSInstance = nullptr;

	FileSystemManager* FileSystemManager::InstancePtr()
	{
		return gs_pFSInstance;
	}

	FileSystemManager& FileSystemManager::Instance()
	{
		assert(gs_pFSInstance);
		return *gs_pFSInstance;
	}

	FileSystemManager::FileSystemManager()
	{
		assert(!gs_pFSInstance);

		gs_pFSInstance = this;
		m_lzoWorkMem = nullptr;
#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		m_layer2Type = FILE_FLAG_XTEA;
#endif
	}

	FileSystemManager::~FileSystemManager()
	{
		assert(gs_pFSInstance == this);

		gs_pFSInstance = nullptr;
		if (m_lzoWorkMem)
		{
			free(m_lzoWorkMem);
			m_lzoWorkMem = nullptr;
		}
	}

	bool FileSystemManager::InitializeFSManager(
#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		uint8_t layer2Type
#endif
	)
	{
		std::lock_guard lock(m_fsMutex);

		assert(!gs_pFSLogInstance);

		CreateDirectoryA("logs", nullptr);
		gs_pFSLogInstance = new CLog("FSLogger", CUSTOM_LOG_FILENAME);

		if (!gs_pFSLogInstance)
		{
			Logf(CUSTOM_LOG_ERROR_FILENAME,
			     "FileSystemManager::InitializeFSManager: File system log manager initialization fail!");
			return false;
		}

		if (const auto error = lzo_init(); error != LZO_E_OK)
		{
			FS_LOG(LL_ERR, "LZO can not initialized. Error: %d", error);
			return false;
		}

		m_lzoWorkMem = malloc(LZO2A_999_MEM_COMPRESS);
		if (!m_lzoWorkMem)
		{
			FS_LOG(LL_ERR, "LZO work memory can not allocated");
			return false;
		}

#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		m_layer2Type = layer2Type;
#endif

		DEBUG_LOG(LL_SYS, "Build: %s", __TIMESTAMP__);
		return true;
	}

	void FileSystemManager::FinalizeFSManager() const
	{
		std::lock_guard lock(m_fsMutex);

		if (gs_pFSLogInstance)
		{
			delete gs_pFSLogInstance;
			gs_pFSLogInstance = nullptr;
		}
	}

	void FileSystemManager::CloseArchives()
	{
		std::lock_guard lock(m_fsMutex);

		for (const auto& archive : m_archives)
		{
			archive->GetArchiveFileStream().Close();
		}
	}

	bool FileSystemManager::AddArchive(const CFileName& filename, const std::array<uint8_t, ARCHIVE_KEY_LENGTH>& key)
	{
		std::lock_guard lock(m_fsMutex);

		auto pack = std::make_unique<CArchive>();
		if (!pack->Create(filename, key, m_files))
		{
			FS_LOG(LL_ERR, "Failed to load Archive %ls", filename.GetPathW().c_str());
			return false;
		}

		m_archives.emplace_back(std::move(pack));
		return true;
	}

	CArchive* FileSystemManager::GetArchive(const CFileName& name)
	{
		std::lock_guard lock(m_fsMutex);

		for (const auto& archive : m_archives)
		{
			if (archive && archive->GetArchiveFileStream().GetFileName() == name.GetPathW())
			{
				return archive.get();
			}
		}
		return nullptr;
	}

	TArchiveKey FileSystemManager::GetArchiveKey(const CFileName& name) const
	{
		std::lock_guard lock(m_fsMutex);

		for (const auto& key : gs_vecFileAndKeys)
		{
			if (std::get<KEY_CONTAINER_FILENAME>(key).GetHash() == name.GetHash())
			{
				return std::get<KEY_CONTAINER_KEY>(key);
			}
		}

		//DEBUG_LOG(LL_ERR, "Archive: %s key does not exist!", name.GetPathA().c_str());
		return DEFAULT_ARCHIVE_KEY;
	}

	bool FileSystemManager::EnumerateFiles(const CFileName& name, TEnumFiles pfnEnumFiles, LPVOID pvUserContext)
	{
		std::lock_guard lock(m_fsMutex);

		if (!pfnEnumFiles)
			return false;

		for (const auto& [hash, archivectx] : m_files)
		{
			if (archivectx.first && archivectx.first->GetArchiveFileStream().GetFileName() == name.GetPathW())
			{
				if (pfnEnumFiles(archivectx.first->GetArchiveFileStream().GetFileName(), archivectx.second, pvUserContext) == false)
					return false;
			}
		}

		return true;
	}

	bool FileSystemManager::DoesFileExist(const CFileName& path, bool mapped_only) const
	{
		std::lock_guard lock(m_fsMutex);

		if (m_files.find(path.GetHash()) != m_files.end())
			return true;

		if (!mapped_only)
		{
#ifndef _DEBUG
			if (const auto filename = path.GetPathA(); filename.find_first_of(':') != std::string::npos)
				return false;
#endif
			return 0 == _waccess(path.GetPathW().c_str(), 0);
		}

		return false;
	}

	bool FileSystemManager::OpenFile(const CFileName& path, CFile& fp, bool silent_failure) const
	{
		std::lock_guard lock(m_fsMutex);

		if (!path)
			return false;

		if (const auto it = m_files.find(path.GetHash()); it != m_files.end())
		{
			const auto& entry = it->second;
			return entry.first->Get(path, entry.second, fp);
		}

		const auto fileName = path.GetPathA();
		const auto extPos = fileName.find_last_of('.');
		if (extPos != std::string::npos)
		{
			const auto ext = fileName.substr(extPos + 1);
			if (m_diskExtBlacklist.find(ext) != m_diskExtBlacklist.end())
			{
				DEBUG_LOG(LL_ERR, "Loading %ls from disk is forbidden", path.GetPathW().c_str());
				return false;
			}
		}

#ifndef _DEBUG
		if (fileName.find_first_of(':') != std::string::npos)
			return false;
#endif

		if (fp.Create(path.GetPathW(), FILEMODE_READ, true, true))
			return true;

		//if (!silent_failure)
		//{
		//	DEBUG_LOG(LL_ERR, "Failed to load %ls %u", path.GetPathW().c_str(), path.GetHash());
		//}
		return false;
	}

	void FileSystemManager::AddToDiskBlacklist(const std::string& extension)
	{
		std::lock_guard lock(m_fsMutex);

		DEBUG_LOG(LL_SYS, "Blocked extension: %s", extension.c_str());
		m_diskExtBlacklist.emplace(extension);
	}

#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
	std::vector <uint8_t> FileSystemManager::DecryptLayer2Protection(const uint8_t* data, size_t length) const
	{
		std::lock_guard <std::recursive_mutex> lock(m_fsMutex);

		std::vector <uint8_t> out_buffer(length);

		if (m_layer2Type == FILE_FLAG_RAW)
		{
			memcpy(&out_buffer[0], data, length);
		}
		else if (m_layer2Type == FILE_FLAG_BLOWFISH)
		{
			try
			{
				CryptoPP::CTR_Mode<CryptoPP::Blowfish>::Decryption dec(&DEFAULT_LAYER2_KEY[0], 16, &DEFAULT_LAYER2_KEY[16]);
				dec.ProcessData(&out_buffer[0], data, length);
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on layer2 type 1 decryption: %s", exception.what());
				abort();
			}
		}
		else if (m_layer2Type == FILE_FLAG_XTEA)
		{
			try
			{
				CryptoPP::CTR_Mode<CryptoPP::XTEA>::Decryption dec(&DEFAULT_LAYER2_KEY[0], 16, &DEFAULT_LAYER2_KEY[16]);
				dec.ProcessData(&out_buffer[0], data, length);
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on layer2 type 2 decryption: %s", exception.what());
				abort();
			}
		}
		else
		{
			DEBUG_LOG(LL_CRI, "Unknown layer2 encryption type: %u", m_layer2Type);
			abort();
		}
		return out_buffer;
	}
#endif

	std::unique_ptr<DataBuffer> FileSystemManager::Get(const char* c_szFileName) const
	{
		if (c_szFileName)
		{
			if (CFile file; OpenFile(c_szFileName, file, true))
				return std::make_unique<DataBuffer>(file.GetData(), file.GetSize());
		}
		return std::unique_ptr<DataBuffer>();
	}

	void* FileSystemManager::GetLzoWorkMem() const
	{
		std::lock_guard lock(m_fsMutex);

		return m_lzoWorkMem;
	}

	bool FileSystemManager::GetFileInformation(const CFileName& filename, FSFileInformation& fileInfo) const
	{
		std::lock_guard lock(m_fsMutex);

		for (const auto& [k, v] : m_files)
		{
			if (v.first && v.second.filenameHash == filename.GetHash())
			{
				fileInfo = v.second;
				return true;
			}
		}

		FS_LOG(LL_ERR, "File: %ls not found!", filename.GetPathW().c_str());
		return false;
	}
};
