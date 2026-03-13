#include "FileSystem.hpp"
#include "FileSystemManager.hpp"
#include "LogHelper.hpp"
#include "Constants.hpp"
#include "FileNameHelper.hpp"
#include "DataBuffer.hpp"
#include "Utils.hpp"

#include <lz4.h>
#include <lz4hc.h>
#include <lzo/lzo2a.h>
#include <zlib.h>
#include <xxhash.h>
#include <filesystem>

#include <cryptopp/modes.h>
#include <cryptopp/aes.h>
#include <cryptopp/twofish.h>
#include <cryptopp/rc5.h>
#include <cryptopp/tea.h>
#include <cryptopp/blowfish.h>

namespace FileSystem
{
	// Read & Process
	bool CArchive::Create(const CFileName& filename, const std::array<uint8_t, ARCHIVE_KEY_LENGTH>& key,
	                      FSFileDict& dict)
	{
		std::lock_guard<std::recursive_mutex> lock(m_archiveMutex);

		if (!m_file.Create(filename, FILEMODE_READ, false))
			return false;

		FSArchiveHeader hdr{};
		if (!m_file.Read(&hdr, sizeof(hdr)))
			return false;

		if (hdr.magic != ARCHIVE_MAGIC)
			return false;

		if (hdr.version != ARCHIVE_VERSION)
			return false;

		m_file.SetPosition(hdr.fileInfoOffset);

		for (uint32_t i = 0; i != hdr.fileCount; ++i)
		{
			FSFileInformation e{};
			if (!m_file.Read(&e, sizeof(e)))
				return false;

			dict.insert(std::make_pair(e.filenameHash, std::make_pair(this, e)));
		}

		m_key.resize(ARCHIVE_KEY_LENGTH);
		memcpy(&m_key[0], key.data(), ARCHIVE_KEY_LENGTH);
		return true;
	}

	bool CArchive::Get(const CFileName& filename, const FSFileInformation& entry, CFile& fp)
	{
		std::lock_guard<std::recursive_mutex> lock(m_archiveMutex);

		// DEBUG_LOG(LL_SYS, "%lu %ls %u", filename.GetHash(), entry.filename, entry.rawSize);

		m_file.SetPosition(entry.offset);

		std::vector<uint8_t> raw_data(entry.cryptedSize);
		auto read_size = m_file.Read(&raw_data[0], entry.cryptedSize);
		if (read_size != entry.cryptedSize)
		{
			FS_LOG(LL_ERR, "File: %ls Read size mismatch: %u-%u", filename.GetPathW().c_str(), read_size,
			       entry.cryptedSize);
			return false;
		}

		DEBUG_LOG(LL_TRACE,
		          "Target file: %ls(%lu) Data: %p(%u) Hash: %lu Flags: %u",
		          filename.GetPathW().c_str(), filename.GetHash(), raw_data.data(), entry.cryptedSize, entry.fileHash,
		          entry.flags
		);

		auto decrypted = DataBuffer(entry.rawSize);
		if (entry.flags & ARCHIVE_FLAG_AES256)
		{
			std::vector<uint8_t> out_buffer(entry.cryptedSize);
			try
			{
				CryptoPP::CTR_Mode<CryptoPP::AES>::Decryption dec(&m_key[0], 32, &m_key[32]);
				dec.ProcessData(&out_buffer[0], reinterpret_cast<const uint8_t*>(raw_data.data()), entry.cryptedSize);
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on decryption: %s", exception.what());
				abort();
			}
			decrypted = DataBuffer(&out_buffer[0], out_buffer.size());
		}
		else if (entry.flags & ARCHIVE_FLAG_TWOFISH)
		{
			std::vector<uint8_t> out_buffer(entry.cryptedSize);
			try
			{
				CryptoPP::CTR_Mode<CryptoPP::Twofish>::Decryption dec(&m_key[0], 32, &m_key[32]);
				dec.ProcessData(&out_buffer[0], reinterpret_cast<const uint8_t*>(raw_data.data()), entry.cryptedSize);
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on decryption: %s", exception.what());
				abort();
			}
			decrypted = DataBuffer(&out_buffer[0], out_buffer.size());
		}
		else if (entry.flags & ARCHIVE_FLAG_RC5)
		{
			std::vector<uint8_t> out_buffer(entry.cryptedSize);
			try
			{
				CryptoPP::CTR_Mode<CryptoPP::RC5>::Decryption dec(&m_key[0], 32, &m_key[32]);
				dec.ProcessData(&out_buffer[0], reinterpret_cast<const uint8_t*>(raw_data.data()), entry.cryptedSize);
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on decryption: %s", exception.what());
				abort();
			}
			decrypted = DataBuffer(&out_buffer[0], out_buffer.size());
		}
		else
		{
			decrypted = DataBuffer(raw_data.data(), entry.cryptedSize);
		}

		auto decompressed = DataBuffer(entry.rawSize);
		if (entry.flags & ARCHIVE_FLAG_LZ4)
		{
			std::vector<uint8_t> decompressed_data(entry.rawSize);

			auto decompressed_size = LZ4_decompress_safe(
				decrypted.get_data(), reinterpret_cast<char*>(&decompressed_data[0]),
				decrypted.get_size(), decompressed_data.size()
			);
			if (decompressed_size != entry.rawSize)
			{
				FS_LOG(LL_ERR, "Decompressed size mismatch: %d-%u", decompressed_size, entry.rawSize);
				return false;
			}
			decompressed = DataBuffer(&decompressed_data[0], entry.rawSize);
		}
		else if (entry.flags & ARCHIVE_FLAG_LZO)
		{
			std::vector<uint8_t> decompressed_data(entry.rawSize);

			lzo_uint decompressed_size = decompressed_data.size();
			auto ret = lzo2a_decompress_safe(
				reinterpret_cast<uint8_t*>(decrypted.get_data()), decrypted.get_size(),
				reinterpret_cast<uint8_t*>(&decompressed_data[0]), &decompressed_size,
				nullptr
			);
			if (LZO_E_OK != ret || decompressed_size != entry.rawSize)
			{
				FS_LOG(LL_ERR, "Decompress failed: ret %d, decompressedSize %u/%u",
				       ret, decompressed_size, entry.compressedSize);
				return false;
			}
			decompressed = DataBuffer(&decompressed_data[0], entry.rawSize);
		}
		else if (entry.flags & ARCHIVE_FLAG_ZLIB)
		{
			std::vector<uint8_t> decompressed_data(entry.rawSize);

			uLongf decompressed_size = decompressed_data.size();
			auto ret = uncompress(
				reinterpret_cast<Bytef*>(&decompressed_data[0]), &decompressed_size,
				reinterpret_cast<const Bytef*>(decrypted.get_data()), decrypted.get_size()
			);

			if (Z_OK != ret || decompressed_size != entry.rawSize)
			{
				FS_LOG(LL_ERR, "Decompress failed: ret %d, decompressedSize %u/%u",
				       ret, decompressed_size, entry.compressedSize);
				return false;
			}
			decompressed = DataBuffer(&decompressed_data[0], entry.rawSize);
		}
		else
		{
			decompressed = decrypted;
		}

#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		if (IsLayer2File(filename))
		{
			auto decryptedBuffer = FileSystemManager::Instance().DecryptLayer2Protection(
				reinterpret_cast<const uint8_t*>(decompressed.get_data()), decompressed.get_size()
			);
			if (decryptedBuffer.empty())
			{
				FS_LOG(LL_ERR, "Layer2 decryption fail");
				return false;
			}
			auto current_hash = XXH32(decryptedBuffer.data(), decryptedBuffer.size(), FILE_HASH_MAGIC);
			if (current_hash != entry.baseHash)
			{
				FS_LOG(LL_ERR, "Layer2 Hash mismatch: %lu-%lu", current_hash, entry.baseHash);
				return false;
			}
		}
		else
#endif
		{
			if (decompressed.get_size() != entry.rawSize)
			{
				FS_LOG(LL_ERR, "Size mismatch: %lu-%lu", decompressed.get_size(), entry.rawSize);
				return false;
			}

			auto current_hash = XXH32(decompressed.get_data(), decompressed.get_size(),
			                          static_cast<XXH32_hash_t>(FILE_HASH_MAGIC));
			if (current_hash != entry.baseHash)
			{
				FS_LOG(LL_ERR, "Hash mismatch: %lu-%lu", current_hash, entry.baseHash);
				return false;
			}
		}

		if (!fp.Assign(filename, decompressed.get_data(), decompressed.get_size(), true))
		{
			FS_LOG(LL_ERR, "File: %lu(%ls) assign failed", entry.baseHash, filename.GetPathW().c_str());
			return false;
		}
		return true;
	}

	// Write
	CArchiveMaker::CArchiveMaker()
	{
#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		m_layer2Type = FILE_FLAG_RAW;
#endif
		m_key.resize(ARCHIVE_KEY_LENGTH);
	}

	bool CArchiveMaker::Create(const CFileName& filename, const std::array<uint8_t, ARCHIVE_KEY_LENGTH>& key)
	{
		if (std::filesystem::exists(filename.GetPathW()))
			std::filesystem::remove(filename.GetPathW()); // remove old archive, if already exist

		if (!m_file.Create(filename, FILEMODE_WRITE, false))
			return false;

		m_file.SetPosition(sizeof(FSArchiveHeader));
#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		m_layer2Type = FileSystemManager::Instance().GetLayer2Type();
#endif
		memcpy(&m_key[0], key.data(), ARCHIVE_KEY_LENGTH);
		return true;
	}

	bool CArchiveMaker::Add(const CFileName& archivedPath, const CFileName& diskPath, uint32_t flags)
	{
		CFile src;
		if (!src.Create(diskPath, FILEMODE_READ, true))
			return false;

		auto baseHash = XXH32(src.GetCurrentSeekPoint(), src.GetSize(), static_cast<XXH32_hash_t>(FILE_HASH_MAGIC));
		auto data_buffer = DataBuffer(src.GetCurrentSeekPoint(), src.GetSize());

		auto processed = false;
#ifdef ENABLE_LAYER2_FILE_ENCRYPTION
		if (IsLayer2File(archivedPath))
		{
			DEBUG_LOG(LL_SYS, "Layer2 supported file detected for secure: %ls", archivedPath.GetPathW().c_str());

			if (m_layer2Type == FILE_FLAG_BLOWFISH)
			{
				try
				{
					CryptoPP::CTR_Mode<CryptoPP::Blowfish>::Encryption enc(&DEFAULT_LAYER2_KEY[0], 16, &DEFAULT_LAYER2_KEY[16]);
					enc.ProcessData(
						reinterpret_cast<uint8_t*>(data_buffer.get_data()),
						reinterpret_cast<const uint8_t*>(src.GetCurrentSeekPoint()),
						src.GetSize()
					);
				}
				catch (const CryptoPP::Exception& exception)
				{
					FS_LOG(LL_CRI, "Caught exception on encryption: %s", exception.what());
					abort();
				}

				processed = true;
			}
			else if (m_layer2Type == FILE_FLAG_XTEA)
			{
				try
				{
					CryptoPP::CTR_Mode<CryptoPP::XTEA>::Encryption enc(&DEFAULT_LAYER2_KEY[0], 16, &DEFAULT_LAYER2_KEY[16]);
					enc.ProcessData(
						reinterpret_cast<uint8_t*>(data_buffer.get_data()),
						reinterpret_cast<const uint8_t*>(src.GetCurrentSeekPoint()),
						src.GetSize()
					);
				}
				catch (const CryptoPP::Exception& exception)
				{
					FS_LOG(LL_CRI, "Caught exception on encryption: %s", exception.what());
					abort();
				}

				processed = true;
			}
			else if (m_layer2Type != FILE_FLAG_RAW)
			{
				DEBUG_LOG(LL_CRI, "Unknown layer2 encryption type: %u", m_layer2Type);
				abort();
			}
		}
#endif
		if (!processed)
			data_buffer = DataBuffer(src.GetCurrentSeekPoint(), src.GetSize());

		FSFileInformation entry{};
		entry.filenameHash = archivedPath.GetHash();
		entry.baseHash = baseHash;
		entry.flags = flags;
		entry.offset = m_file.GetPosition();
		entry.rawSize = src.GetSize();
#ifdef SHOW_FILE_NAMES
		wcscpy_s(entry.filename, archivedPath.GetPathW().c_str());
#endif

		DEBUG_LOG(LL_SYS,
		          "Target file: %ls(%lu) Data: %p(%u) Hash: %lu Flags: %u Offset: %llu",
		          archivedPath.GetPathW().c_str(), archivedPath.GetHash(),
		          data_buffer.get_data(), data_buffer.get_size(), entry.baseHash, flags,
		          entry.offset
		);

		const auto bound = LZ4_compressBound(entry.rawSize);
		DataBuffer finalData(bound);

		int32_t compressed_size = 0;
		int32_t encrypted_size = 0;
		if (entry.flags & ARCHIVE_FLAG_LZ4)
		{
			std::vector<uint8_t> compressed(bound);

			compressed_size = LZ4_compress_HC(
				reinterpret_cast<const char*>(data_buffer.get_data()), reinterpret_cast<char*>(&compressed[0]),
				entry.rawSize, bound, LZ4HC_CLEVEL_MAX
			);
			if (compressed_size >= bound || compressed_size == 0)
			{
				FS_LOG(LL_ERR, "Compression fail! File: %ls Raw: %u Compressed: %u Capacity: %u",
				       diskPath.GetPathW().c_str(), entry.rawSize, compressed_size, bound);

				finalData = data_buffer;
				flags &= ~ARCHIVE_FLAG_LZ4;
			}
			else
			{
				finalData = DataBuffer(&compressed[0], compressed_size);
			}
		}
		else if (flags & ARCHIVE_FLAG_LZO)
		{
			auto* lzoWorkMem = FileSystemManager::Instance().GetLzoWorkMem();
			assert(lzoWorkMem);

			std::vector<uint8_t> compressed(finalData.get_size());

			lzo_uint out_len = finalData.get_size();
			auto ret = lzo2a_999_compress(
				reinterpret_cast<const uint8_t*>(data_buffer.get_data()), entry.rawSize,
				reinterpret_cast<uint8_t*>(&compressed[0]), &out_len,
				lzoWorkMem
			);

			if (LZO_E_OK != ret)
			{
				FS_LOG(LL_ERR, "Compression fail! File: %ls Raw: %u Compressed: %u Ret: %d",
				       diskPath.GetPathW().c_str(), entry.rawSize, out_len, ret);

				finalData = data_buffer;
				flags &= ~ARCHIVE_FLAG_LZO;
			}
			else
			{
				compressed_size = out_len;
				finalData = DataBuffer(&compressed[0], compressed_size);
			}
		}
		else if (flags & ARCHIVE_FLAG_ZLIB)
		{
			finalData = DataBuffer(compressBound(entry.rawSize));
			std::vector<uint8_t> compressed(finalData.get_size());

			uLongf out_len = finalData.get_size();
			auto ret = compress(
				reinterpret_cast<Bytef*>(&compressed[0]), &out_len,
				reinterpret_cast<const Bytef*>(data_buffer.get_data()), entry.rawSize
			);

			if (Z_OK != ret)
			{
				FS_LOG(LL_ERR, "Compression fail! File: %ls Raw: %u Compressed: %u Ret: %d",
				       diskPath.GetPathW().c_str(), entry.rawSize, out_len, ret);

				finalData = data_buffer;
				flags &= ~ARCHIVE_FLAG_ZLIB;
			}
			else
			{
				compressed_size = out_len;
				finalData = DataBuffer(&compressed[0], compressed_size);
			}
		}
		if (compressed_size == 0)
		{
			FS_LOG(LL_ERR, "Compression fail! Raw data moved to compressed buffer");

			if (flags & ARCHIVE_FLAG_LZ4)
				flags &= ~ARCHIVE_FLAG_LZ4;
			else if (flags & ARCHIVE_FLAG_LZO)
				flags &= ~ARCHIVE_FLAG_LZO;
			else if (flags & ARCHIVE_FLAG_ZLIB)
				flags &= ~ARCHIVE_FLAG_ZLIB;

			finalData = data_buffer;
		}

		DEBUG_LOG(LL_SYS, "Compression completed! Data: %p Size: %u - %u",
		          finalData.get_data(), finalData.get_size(), compressed_size);
		entry.compressedSize = compressed_size;

		if (flags & ARCHIVE_FLAG_AES256)
		{
			std::vector<uint8_t> out_buffer(finalData.get_size());

			try
			{
				CryptoPP::CTR_Mode<CryptoPP::AES>::Encryption enc(&m_key[0], 32, &m_key[32]);
				enc.ProcessData(&out_buffer[0], reinterpret_cast<const uint8_t*>(finalData.get_data()),
				                finalData.get_size());
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on encryption: %s", exception.what());
				abort();
			}

			finalData = DataBuffer(&out_buffer[0], out_buffer.size());
			encrypted_size = out_buffer.size();
		}
		else if (flags & ARCHIVE_FLAG_TWOFISH)
		{
			std::vector<uint8_t> out_buffer(finalData.get_size());

			try
			{
				CryptoPP::CTR_Mode<CryptoPP::Twofish>::Encryption enc(&m_key[0], 32, &m_key[32]);
				enc.ProcessData(&out_buffer[0], reinterpret_cast<const uint8_t*>(finalData.get_data()),
				                finalData.get_size());
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on encryption: %s", exception.what());
				abort();
			}

			finalData = DataBuffer(&out_buffer[0], out_buffer.size());
			encrypted_size = out_buffer.size();
		}
		else if (flags & ARCHIVE_FLAG_RC5)
		{
			std::vector<uint8_t> out_buffer(finalData.get_size());

			try
			{
				CryptoPP::CTR_Mode<CryptoPP::RC5>::Encryption enc(&m_key[0], 32, &m_key[32]);
				enc.ProcessData(&out_buffer[0], reinterpret_cast<const uint8_t*>(finalData.get_data()),
				                finalData.get_size());
			}
			catch (const CryptoPP::Exception& exception)
			{
				FS_LOG(LL_CRI, "Caught exception on encryption: %s", exception.what());
				abort();
			}

			finalData = DataBuffer(&out_buffer[0], out_buffer.size());
			encrypted_size = out_buffer.size();
		}
		else
		{
			encrypted_size = finalData.get_size(); // copy of compressed size
		}

		entry.cryptedSize = encrypted_size;
		entry.fileHash = XXH32(finalData.get_data(), finalData.get_size(), static_cast<XXH32_hash_t>(FILE_HASH_MAGIC));
		DEBUG_LOG(LL_SYS, "Encryption completed! Data: %p Size: %u - %u Hash: %lu",
		          finalData.get_data(), finalData.get_size(), encrypted_size, entry.fileHash);

		if (!m_file.Write(&finalData[0], finalData.get_size()))
		{
			FS_LOG(LL_ERR, "Target file: %ls can NOT write to archive!", archivedPath.GetPathW().c_str());
			return false;
		}

		m_files.emplace_back(entry);
		return true;
	}

	bool CArchiveMaker::Save()
	{
		FSArchiveHeader hdr = {};
		hdr.magic = ARCHIVE_MAGIC;
		hdr.version = ARCHIVE_VERSION;
		hdr.fileInfoOffset = m_file.GetPosition();
		hdr.fileCount = m_files.size();

		for (const auto& f : m_files)
		{
			if (!m_file.Write(&f, sizeof(f)))
			{
				FS_LOG(LL_ERR, "Target file: %ls can NOT write fileHash %u to archive!", m_file.GetFileName().c_str(),
				       f.fileHash);
				return false;
			}
		}

		m_file.SetPosition(0);
		if (!m_file.Write(&hdr, sizeof(hdr)))
		{
			FS_LOG(LL_ERR, "Target file: %ls can NOT write archive!", m_file.GetFileName().c_str());
			return false;
		}
		m_file.Close();
		return true;
	}
};
