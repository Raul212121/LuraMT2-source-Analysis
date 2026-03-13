#pragma once

class CHARACTER;
class CItem;
class CGrid;

class CSafebox
{
public:
	CSafebox(LPCHARACTER pkChrOwner, int iSize, DWORD dwGold);
	~CSafebox();

	bool			Add(DWORD dwPos, LPITEM pkItem);
	LPITEM			Get(DWORD dwPos);
	LPITEM			Remove(DWORD dwPos);
	void			ChangeSize(int iSize);

#ifdef ENABLE_EXTEND_ITEMS_STACK
	bool 			MoveItem(BYTE bCell, BYTE bDestCell, WORD count);
#else
	bool 			MoveItem(BYTE bCell, BYTE bDestCell, BYTE count);
#endif
	LPITEM			GetItem(BYTE bCell);

	void			Save();

	bool			IsEmpty(DWORD dwPos, BYTE bSize);
#if defined(ITEM_CHECKINOUT_UPDATE)
	int				GetEmptySafebox(BYTE size);
#endif
	bool			IsValidPosition(DWORD dwPos);

	void			SetWindowMode(BYTE bWindowMode);
	unsigned int	GetGridTotalSize() const;

protected:
	void		__Destroy();

	LPCHARACTER	m_pkChrOwner;
	LPITEM		m_pkItems[SAFEBOX_MAX_NUM];
	int			m_iSize;
	long		m_lGold;
	BYTE		m_bWindowMode;
	std::vector<std::shared_ptr<CGrid>> v_Grid;
};
