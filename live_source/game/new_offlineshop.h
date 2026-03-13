#ifndef __INCLUDE_NEW_OFFLINESHOP_HEADER__
#define __INCLUDE_NEW_OFFLINESHOP_HEADER__
#ifdef __ENABLE_NEW_OFFLINESHOP__

#include "item.h"

#define ENABLE_SHOP_GUESTLIST_FIX
#ifdef ENABLE_SHOP_GUESTLIST_FIX
#define GUEST_PTR(id)  (CHARACTER_MANAGER::instance().FindByPID(id))
#define GUEST_FROM_CHARACTER(id) (id->GetPlayerID())
#else
#define GUEST_PTR(i)  (i)
#define GUEST_FROM_CHARACTER(i) (i)
#endif

template <class T>
void ZeroObject(T& obj)
{
	memset(&obj, 0 , sizeof(obj));
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

template <class T, size_t size>
void CopyArray(T (&objDest)[size] , const T (&objSrc)[size])
{
	if(size==0)
		return;
	memcpy(&objDest[0] , &objSrc[0], sizeof(T)*size);
}

template <class T>
void DeletePointersContainer(T& obj)
{
	typename T::iterator it = obj.begin();
	for(; it != obj.end(); it++)
		M2_DELETE(*it);
}

namespace offlineshop
{
	inline offlineshop::ExpirationType GetItemExpiration(LPITEM item) {
		auto proto = item->GetProto();
		for (const auto limit : proto->aLimits) {
			if (limit.bType == LIMIT_REAL_TIME)
				return offlineshop::ExpirationType::EXPIRE_REAL_TIME;
			else if (limit.bType == LIMIT_REAL_TIME_START_FIRST_USE && item->GetSocket(1) != 0)
				return offlineshop::ExpirationType::EXPIRE_REAL_TIME_FIRST_USE;
		} return offlineshop::ExpirationType::EXPIRE_NONE;
	}

#pragma pack(1)
	class CShopItem
	{
	public:
		CShopItem(DWORD dwID);
		CShopItem(const CShopItem& rCopy);
		CShopItem(LPITEM pItem, const TPriceInfo& sPrice, BYTE byWindowType, DWORD dwID=0);

		~CShopItem();

		bool			GetTable(TItemTable** ppTable) const;
		TPriceInfo*		GetPrice() const;
		LPITEM			CreateItem() const;
		TItemInfoEx*	GetInfo() const;
		void			SetInfo(LPITEM pItem);
		void			SetInfo(const TItemInfoEx& info);
		void			SetPrice(const TPriceInfo& sPrice);
		void			SetWindow(BYTE byWin);
		BYTE			GetWindow() const;
		DWORD			GetID() const ;
		void			SetOwnerID(DWORD dwOwnerID);
		bool			CanBuy(LPCHARACTER ch) const;
		void operator = (const CShopItem& rItem);

	protected:
		TItemInfoEx		m_itemInfo;
		TPriceInfo		m_priceInfo;
		BYTE			m_byWindow;
		DWORD			m_dwID;
		DWORD			m_dwOwnerID;
	};

#pragma pack()
	class CShop
	{
	public:
		typedef std::vector<CShopItem>  VECSHOPITEM;
		typedef std::vector<TOfferInfo>	VECSHOPOFFER;
#ifdef ENABLE_SHOP_GUESTLIST_FIX
		typedef std::list<DWORD>		LISTGUEST;
#else
		typedef std::list<LPCHARACTER>	LISTGUEST;
#endif

	public:
		CShop();
		CShop(const CShop& rCopy);
		~CShop();

		VECSHOPITEM*		GetItems() const;
		VECSHOPITEM*		GetItemsSold() const;
		VECSHOPOFFER*		GetOffers() const;
		LISTGUEST*			GetGuests() const;

		void				SetDuration(DWORD dwDuration);
		DWORD				DecreaseDuration();

		DWORD				GetDuration() const;

		void				SetOwnerPID(DWORD dwOwnerPID);
		DWORD				GetOwnerPID() const;

		bool				AddGuest(LPCHARACTER ch);
		bool				RemoveGuest(LPCHARACTER ch);

		void				SetItems(const VECSHOPITEM* pVec);
		bool				AddItem(CShopItem& rItem);
		bool				AddItemSold(CShopItem& rItem);
		bool				RemoveItem(DWORD dwItemID);
		bool				ModifyItem(DWORD dwItemID, const CShopItem& rItem);
		bool				BuyItem(DWORD dwItem);
		bool				GetItem(DWORD dwItem, CShopItem** ppItem);
		bool				GetItemSold(DWORD dwItem, CShopItem** ppItem);

		bool				AddOffer(const TOfferInfo* pOfferInfo);
		bool				AcceptOffer(const TOfferInfo* pOfferInfo);

		void				NotifyOffers(LPCHARACTER ch);
		void				NotifyAcceptedOffers(LPCHARACTER ch);
		LPCHARACTER			FindOwnerCharacter() const;
		void				Clear();

		const char*			GetName() const;
		void				SetName(const char* pcszName);

		void				RefreshToOwner() const;

#ifdef __NEW_OFFLINESHOP_SPAWN__
		void				SetPosInfo(const TShopPosition& pos);
#endif

		void SetChangeNamePulse(time_t pulse) { m_changeNamePulse = pulse; }
		time_t GetChangeNamePulse() const { return m_changeNamePulse; }

		void SetEditItemPricePulse(time_t pulse) { m_editItemPricePulse = pulse; }
		time_t GetEditItemPricePulse() const { return m_editItemPricePulse; }

	private:
		void				__RefreshItems(LPCHARACTER ch=NULL);
		void				__SendOfferNotify(LPCHARACTER ch, TOfferInfo* pOffer);

	private:
		VECSHOPITEM			m_vecItems;
		VECSHOPITEM			m_vecItemSold;
		VECSHOPOFFER		m_vecOffers;
		LISTGUEST			m_listGuests;

		DWORD				m_dwPID;
		DWORD				m_dwDuration;
		std::string			m_stName;
#ifdef __NEW_OFFLINESHOP_SPAWN__
		TShopPosition		m_posInfo;
#endif
		time_t m_changeNamePulse;
		time_t m_editItemPricePulse;
	};

	class CShopSafebox
	{
	public:
		typedef std::vector<CShopItem> VECITEM;

	public:
#pragma pack(1)
		struct SValuteAmount
		{
			long long illYang;
#ifdef __ENABLE_CHEQUE_SYSTEM__
			int iCheque;
#endif

			SValuteAmount() : illYang(0)
			{
			}

			SValuteAmount(const TValutesInfo& rCopy)
			{
				illYang = rCopy.illYang;
#ifdef __ENABLE_CHEQUE_SYSTEM__
				iCheque = rCopy.iCheque;
#endif
			}

			SValuteAmount(const TPriceInfo& rCopy)
			{
				illYang = rCopy.illYang;
#ifdef __ENABLE_CHEQUE_SYSTEM__
				iCheque = rCopy.iCheque;
#endif
			}

			long long GetTotalYangAmount() const
			{
				long long total = illYang;
#ifdef __ENABLE_CHEQUE_SYSTEM__
				total += YANG_PER_CHEQUE*iCheque;
#endif
				return total;
			}

			bool operator < (const SValuteAmount& rVal)
			{
				return GetTotalYangAmount() < rVal.GetTotalYangAmount();
			}

			void operator -= (const SValuteAmount& rVal)
			{
				illYang -= rVal.illYang;
#ifdef __ENABLE_CHEQUE_SYSTEM__
				iCheque += rVal.iCheque;
#endif
			}

			void operator += (const SValuteAmount& rVal)
			{
				illYang += rVal.illYang;
#ifdef __ENABLE_CHEQUE_SYSTEM__
				iCheque += rVal.iCheque;
#endif
			}
		};
#pragma pack()

	public:
		CShopSafebox(LPCHARACTER chOwner);
		CShopSafebox();
		CShopSafebox(const CShopSafebox& rCopy);
		~CShopSafebox();

		void			SetOwner(LPCHARACTER ch);
		void			SetItems(VECITEM* pVec);
		void			SetValutesAmount(SValuteAmount val);

		bool			AddItem(CShopItem* pItem);
		bool			RemoveItem(DWORD dwItemID);

		void			AddValutes(SValuteAmount val);
		bool			RemoveValutes(SValuteAmount val);

		VECITEM*		GetItems();
		SValuteAmount	GetValutes();

		bool			GetItem(DWORD dwItemID, CShopItem** ppItem);
		LPCHARACTER		GetOwner() const;

		bool			RefreshToOwner(LPCHARACTER ch= nullptr) const;

	private:
		VECITEM			m_vecItems;
		LPCHARACTER		m_pkOwner;
		SValuteAmount	m_valutes;
	};

	class CAuction
	{
	public:
		typedef std::vector<TAuctionOfferInfo> AUCTION_OFFERVEC;
#ifdef ENABLE_SHOP_GUESTLIST_FIX
		typedef std::list<DWORD>		GUESTLIST;
#else
		typedef std::list<LPCHARACTER>	GUESTLIST;
#endif

	public:
		CAuction();
		~CAuction();

		void SetInfo(const TAuctionInfo& auction);
		void SetOffers(const std::vector<TAuctionOfferInfo>& vec);

		bool AddOffer(const TAuctionOfferInfo& offer);
		bool AddGuest(LPCHARACTER ch);
		bool RemoveGuest(LPCHARACTER ch);
		void DecreaseDuration();
		void IncreaseDuration();

		CShop::LISTGUEST&			GetGuests();
		DWORD GetBestBuyer() const;
		const TAuctionInfo&			GetInfo() const;
		const AUCTION_OFFERVEC&		GetOffers() const;
		const TPriceInfo&			GetBestOffer() const;

	private:
		void __RefreshToGuests();
		bool __SetBestOffer();

	private:
		TAuctionInfo		m_info;
		AUCTION_OFFERVEC	m_offersVec;
		TPriceInfo			m_bestOffer;
		DWORD				m_dwBestBuyer;
		GUESTLIST			m_guestsList;

	};

#ifdef __ENABLE_NEW_SHOP_IN_CITIES__
	class ShopEntity : public CEntity
	{
	public:
		ShopEntity();
		~ShopEntity() { Destroy(); }

		void	EncodeInsertPacket(LPENTITY entity) override;
		void	EncodeRemovePacket(LPENTITY entity) override;

		const char*			GetShopName() const;
		void				SetShopName(const char* name);

		int					GetShopType() const;
		void				SetShopType(int iType);
		void				SetShop(offlineshop::CShop* pOfflineShop);

		offlineshop::CShop* GetShop() {return m_pkShop;}

		static DWORD		AllocID()
		{
			static DWORD dwID=1;
			return dwID++;
		}

		DWORD GetVID() { return m_dwVID; }
		void  Destroy() { CEntity::Destroy(); }

	private:
		char					m_szName[OFFLINE_SHOP_NAME_MAX_LEN];
		int						m_iType;
		DWORD					m_dwVID;
		offlineshop::CShop*		m_pkShop;
	};
#endif
}
#endif
#endif
