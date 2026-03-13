#pragma once

#include "ItemData.h"
#include "../UserInterface/Locale_inc.h"

class CItemManager : public CSingleton<CItemManager>
{
	public:
		enum EItemDescCol
		{
			ITEMDESC_COL_VNUM,
			ITEMDESC_COL_NAME,
			ITEMDESC_COL_DESC,
			ITEMDESC_COL_SUMM,
			ITEMDESC_COL_NUM,
		};

	public:
		typedef std::map<DWORD, CItemData*> TItemMap;
		typedef std::map<std::string, CItemData*> TItemNameMap;

#ifdef INGAME_WIKI
	public:
		typedef std::vector<CItemData*> TItemVec;
		typedef std::vector<DWORD> TItemNumVec;
	
	public:
		void WikiAddVnumToBlacklist(DWORD vnum)
		{
			auto it = m_ItemMap.find(vnum);
			if (it != m_ItemMap.end())
				it->second->SetBlacklisted(true);
		};
		
		TItemNumVec* WikiGetLastItems()
		{
			return &m_tempItemVec;
		}
		
		bool							CanIncrSelectedItemRefineLevel();
		bool							CanIncrItemRefineLevel(DWORD itemVnum);
		bool								CanLoadWikiItem(DWORD dwVnum);
		DWORD							GetWikiItemStartRefineVnum(DWORD dwVnum);
		std::string							GetWikiItemBaseRefineName(DWORD dwVnum);
		size_t								WikiLoadClassItems(BYTE classType, DWORD raceFilter);
		std::tuple<const char*, int>	SelectByNamePart(const char * namePart);
	
	protected:
		TItemNumVec m_tempItemVec;
	
	private:
		bool IsFilteredAntiflag(CItemData* itemData, DWORD raceFilter);
#endif
	public:
		CItemManager();
		virtual ~CItemManager();

		void			Destroy();
		BOOL			SelectItemData(DWORD dwIndex);
		CItemData *		GetSelectedItemDataPointer();

		BOOL			GetItemDataPointer(DWORD dwItemID, CItemData ** ppItemData);

		/////
		bool			LoadItemDesc(const char* c_szFileName);
		bool			LoadItemList(const char* c_szFileName);
		bool			LoadItemTable(const char* c_szFileName);
#ifdef ENABLE_SHINING_SYSTEM
		bool			LoadShiningTable(const char* c_szFileName);
#endif
		CItemData *		MakeItemData(DWORD dwIndex);
#ifdef __ENABLE_NEW_OFFLINESHOP__
		void			GetItemsNameMap(std::map<DWORD, std::string>& inMap);
#endif
	protected:
		TItemMap m_ItemMap;
		std::vector<CItemData*>  m_vec_ItemRange;
		CItemData * m_pSelectedItemData;
};
