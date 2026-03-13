#ifndef __INCLUDE_HEADER_PYTHON_OFFLINESHO__
#define __INCLUDE_HEADER_PYTHON_OFFLINESHO__

#ifdef __ENABLE_NEW_OFFLINESHOP__
#include "PythonBackground.h"

namespace offlineshop
{
	template <class T>
	void ZeroObject(T& obj)
	{
		memset(&obj, 0, sizeof(obj));
	}

	template <class T>
	void CopyObject(T& objDest, const T& objSrc)
	{
		memcpy(&objDest, &objSrc, sizeof(objDest));
	}

	template <class T>
	void CopyContainer(T& objDest, const T& objSrc)
	{
		objDest = objSrc;
	}

	template <class T>
	void DeletePointersContainer(T& obj)
	{
		typename T::iterator it = obj.begin();
		for (; it != obj.end(); it++)
			delete(*it);
	}

	template <class T ,template <class> class S, typename S<T>::iterator >
	void ForEach(S<T>& container, std::function<void(T&)> func)
	{
		S<T>::iterator it=container.begin(), iter;

		while((iter = it++) != container.end())
			func(*iter);
	}

	template <class T , class K, template <class,class> class S, typename S<K,T>::iterator >
	void ForEach(S<K,T>& container, std::function<void(T&)> func)
	{
		S<K,T>::iterator it=container.begin(), iter;

		while((iter = it++) != container.end())
			func(iter->second);
	}
}

namespace offlineshop
{
	enum eConstOfflineshop {
		OFFLINESHOP_DURATION_MAX_DAYS	= 8,
		OFFLINESHOP_DURATION_MAX_HOURS	= 23,
		OFFLINESHOP_DURATION_MAX_MINUTES= OFFLINESHOP_DURATION_MAX_DAYS * 24 * 60,
		OFFLINESHOP_MAX_FILTER_HISTORY_SIZE = 50,
		OFFLINESHOP_MAX_ITEM_NUM = 80,
	};
}

#ifdef __ENABLE_NEW_SHOP_IN_CITIES__
namespace offlineshop
{
	class ShopInstance
	{
	public:
		ShopInstance()
		{
			m_dwVID = 0;
			m_iType = 0;
			m_stSign.clear();
		}

		~ShopInstance()
		{
			m_dwVID = 0;
			m_iType = 0;
			m_stSign.clear();
		}

		void SetVID(DWORD dwVID)
		{
			m_dwVID = dwVID;
		}

		void SetShopType(int iType)
		{
			m_iType = iType;
		}

		void SetSign(const char* cpszSign)
		{
			m_stSign = cpszSign;
		}

		void Show(float x, float y, float z)
		{
			
			m_thingInstance.Clear();
			m_thingInstance.ReserveModelThing(1);
			m_thingInstance.ReserveModelInstance(1);
			m_thingInstance.RegisterModelThing(0, (CGraphicThing *)CResourceManager::Instance().GetResourcePointer("offlineshop/shop.gr2"));
			m_thingInstance.SetModelInstance(0, 0, 0);
			m_thingInstance.SetPosition(x, -y, z);
			m_thingInstance.Show();
			m_thingInstance.Update();
			m_thingInstance.Transform();
			m_thingInstance.Deform();
		}

		DWORD GetVID() const
		{
			return m_dwVID;
		}

		std::string GetSign() const
		{
			return m_stSign;
		}

		int GetType() const
		{
			return m_iType;
		}

		CGraphicThingInstance* GetThingInstancePtr()
		{
			return &m_thingInstance;
		}

		void Clear()
		{
			m_thingInstance.Clear();
			m_dwVID = 0;
			m_iType = 0;
			m_stSign.clear();
		}

		void Render()
		{
			m_thingInstance.Render();
		}

		void BlendRender()
		{
			m_thingInstance.BlendRender();
		}

		void Update()
		{
			m_thingInstance.Update();
		}
#ifdef ENABLE_NEW_GAME_OPTIONS
		void Hide()
		{
			m_thingInstance.Hide();
		}

		bool IsShow()
		{
			return m_thingInstance.isShow();
		}

		void ShowShop()
		{
			return m_thingInstance.Show();
		}
#endif
	private:
		CGraphicThingInstance	m_thingInstance;
		DWORD					m_dwVID;
		int						m_iType;
		std::string				m_stSign;
	};
}
#endif

class CPythonOfflineshop : public CSingleton<CPythonOfflineshop>
{
public:
	typedef struct SDatetime
	{
		BYTE bMinutes;
		BYTE bHour;
		BYTE bDay;
		BYTE bMonth;
		int iYear;
	} TDatetime;

	typedef struct SFilterHistoryElement
	{
		TDatetime					datetime;
		DWORD						dwCountItem;
		offlineshop::TFilterInfo	filter;

		bool operator >(const SFilterHistoryElement& r)
		{
			if(datetime.iYear != r.datetime.iYear)
				return datetime.iYear > r.datetime.iYear;

			if(datetime.bMonth != r.datetime.bMonth)
				return datetime.bMonth > r.datetime.bMonth;

			if(datetime.bDay != r.datetime.bDay)
				return datetime.bDay > r.datetime.bDay;

			if(datetime.bHour != r.datetime.bHour)
				return datetime.bHour > r.datetime.bHour;

			if(datetime.bMinutes != r.datetime.bMinutes)
				return datetime.bMinutes > r.datetime.bMinutes;

			return false;
		}

	} TFilterHistoryElement;

	typedef struct SFilterPatternInfo
	{
		TDatetime	datetime_lastuse;
		std::string stName;
		offlineshop::TFilterInfo filter;
	} TFilterPatternInfo;

	typedef std::vector<TFilterHistoryElement> FILTERHISTORY;
	typedef FILTERHISTORY::iterator FILTERHISTORY_ITER;
	typedef std::map<int, TFilterPatternInfo> FILTERMAP;
	typedef FILTERMAP::iterator FILTERMAP_ITER;

	static void GetNowAsDatetime(TDatetime& datetime)
	{
		SYSTEMTIME time;
		GetLocalTime(&time);
		datetime.bMinutes	= (BYTE) time.wMinute;
		datetime.bHour		= (BYTE) time.wHour;
		datetime.bDay		= (BYTE) time.wDay;
		datetime.bMonth		= (BYTE) time.wMonth;
		datetime.iYear		= (int)	 time.wYear;
	}

	static int AllocPatternID()
	{
		static int id=0;
		return id++;
	}

public:
	CPythonOfflineshop();
	~CPythonOfflineshop();

	void		SetWindowObjectPointer(PyObject* poWindow);
	PyObject*	GetOfflineshopBoard();

	void	ShopListAddItem(const offlineshop::TShopInfo& shop);
	void	ShopListShow();
	void	ShopListClear();
	void	BuyFromSearch(DWORD dwOwnerID, DWORD dwItemID);
	void	OpenShop(const offlineshop::TShopInfo& shop, const std::vector<offlineshop::TItemInfo>& vec);
	void	OpenShopOwner(	const offlineshop::TShopInfo& shop, 
							const std::vector<offlineshop::TItemInfo>& vec , 
							const std::vector<offlineshop::TItemInfo>& solds,
							const std::vector<offlineshop::TOfferInfo>& offers
	);
	void	OpenShopOwnerNoShop();
	void	ShopClose();
	void	ShopFilterResult(const std::vector<offlineshop::TItemInfo>& vec);
	void	OfferListReceived(const std::vector<offlineshop::TOfferInfo>& offers, const std::vector<offlineshop::TMyOfferExtraInfo>& items);
	void	SafeboxRefresh(const offlineshop::TValutesInfo& valute,const std::vector<DWORD>& ids, const std::vector<offlineshop::TItemInfoEx>& item); 
	void	AuctionList(const std::vector<offlineshop::TAuctionListElement>& auctions);
	void	MyAuctionOpen(const offlineshop::TAuctionInfo& auction, const std::vector<offlineshop::TAuctionOfferInfo>& offers);
	void	AuctionOpen(const offlineshop::TAuctionInfo& auction, const std::vector<offlineshop::TAuctionOfferInfo>& offers);
	void	OpenMyAuctionNoAuction();
	void	LoadFilterHistory();
	void	LoadFilterPatterns();
	void	SaveFilterHistory();
	void	SaveFilterPatterns();
	void	AddNewFilterToHistory(TFilterHistoryElement& element);
	void	PopOldestFilterHistoryElement();
	void	AddNewFilterPattern(TFilterPatternInfo& pattern);
	void	UpdateFilterPatternLastUse(int iPatternID);
	void	RefreshFilterHistory();
	void	RefreshFilterPatterns();
	void	RefreshItemNameMap();
	void	EnableGuiRefreshSymbol();
	void	ShopBuilding_AddInventoryItem(int iSlot);
	void	AuctionBuilding_AddInventoryItem(int iSlot);
	void	ShopBuilding_AddItem(int iWin, int iSlot);
	void	AuctionBuilding_AddItem(int iWin, int iSlot);

#ifdef __ENABLE_NEW_SHOP_IN_CITIES__
	void	InsertEntity(DWORD dwVID , int iType, const char* szName, long x, long y, long z);
	void	RemoveEntity(DWORD dwVID);
	void	RenderEntities();
	void	UpdateEntities();
	bool	GetShowNameFlag();
	void	SetShowNameFlag(bool flag);
	void	DeleteEntities();
#ifdef ENABLE_NEW_GAME_OPTIONS
	void HideEntities();
	void ShowEntities();
#endif
#endif

private:
	PyObject* m_poWindow;

	FILTERHISTORY	m_filterHistory;
	FILTERMAP		m_filterPatterns;

#ifdef __ENABLE_NEW_SHOP_IN_CITIES__
	std::vector<offlineshop::ShopInstance*> m_vecShopInstance;
	bool m_bIsShowName;
#endif
};

extern void initofflineshop();
#endif
#endif
