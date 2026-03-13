#include "stdafx.h"
#include "constants.h"
#include "utils.h"
#include "config.h"
#include "shop.h"
#include "desc.h"
#include "desc_manager.h"
#include "char.h"
#include "char_manager.h"
#include "item.h"
#include "item_manager.h"
#include "buffer_manager.h"
#include "packet.h"
#include "log.h"
#include "db.h"
#include "questmanager.h"
#include "monarch.h"
#include "mob_manager.h"
#include "locale_service.h"
#include "desc_client.h"
#include "shopEx.h"
#include "group_text_parse_tree.h"

bool CShopEx::Create(DWORD dwVnum, DWORD dwNPCVnum)
{
	m_dwVnum = dwVnum;
	m_dwNPCVnum = dwNPCVnum;
	return true;
}

bool CShopEx::AddShopTable(TShopTableEx& shopTable)
{
	for (auto it = m_vec_shopTabs.begin(); it != m_vec_shopTabs.end(); ++it)
	{
		const TShopTableEx& _shopTable = *it;
		if (0 != _shopTable.dwVnum && _shopTable.dwVnum == shopTable.dwVnum)
			return false;
		if (0 != _shopTable.dwNPCVnum && _shopTable.dwNPCVnum == shopTable.dwVnum)
			return false;
	}
	m_vec_shopTabs.push_back(shopTable);
	return true;
}

bool CShopEx::AddGuest(LPCHARACTER ch,DWORD owner_vid, bool bOtherEmpire)
{
	if (!ch)
		return false;

	if (ch->GetExchange())
		return false;

	if (ch->GetShop())
		return false;

	ch->SetShop(this);

	m_map_guest.insert(GuestMapType::value_type(ch, bOtherEmpire));

	TPacketGCShop pack;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_START_EX;

	TPacketGCShopStartEx pack2;

	memset(&pack2, 0, sizeof(pack2));

	pack2.owner_vid = owner_vid;
	pack2.shop_tab_count = m_vec_shopTabs.size();
#if defined(ENABLE_RENEWAL_SHOPEX)
	char temp[8096 * 2]{};
#else
	char temp[8096]{};
#endif
	char* buf = &temp[0];
	size_t size = 0;
	for (auto it = m_vec_shopTabs.begin(); it != m_vec_shopTabs.end(); it++)
	{
		const TShopTableEx& shop_tab = *it;
		TPacketGCShopStartEx::TSubPacketShopTab pack_tab;
		pack_tab.coin_type = shop_tab.coinType;
		memcpy(pack_tab.name, shop_tab.name.c_str(), SHOP_TAB_NAME_MAX);

		for (BYTE i = 0; i < SHOP_HOST_ITEM_MAX_NUM; i++)
		{
			pack_tab.items[i].vnum = shop_tab.items[i].vnum;
			pack_tab.items[i].count = shop_tab.items[i].count;
#if defined(ENABLE_RENEWAL_SHOPEX)
			pack_tab.items[i].price_type = shop_tab.items[i].price_type;
			pack_tab.items[i].price_vnum = shop_tab.items[i].price_vnum;
			pack_tab.items[i].price = shop_tab.items[i].price;
			memcpy(pack_tab.items[i].aAttr, shop_tab.items[i].aAttr, sizeof(pack_tab.items[i].aAttr));
			memcpy(pack_tab.items[i].alSockets, shop_tab.items[i].alSockets, sizeof(pack_tab.items[i].alSockets));
#else
			switch(shop_tab.coinType)
			{
			case SHOP_COIN_TYPE_GOLD:
#ifdef ENABLE_NEWSTUFF
				if (bOtherEmpire && !g_bEmpireShopPriceTripleDisable) // no empire price penalty for pc shop
#else
				if (bOtherEmpire) // no empire price penalty for pc shop
#endif
					pack_tab.items[i].price = shop_tab.items[i].price * 3;
				else
					pack_tab.items[i].price = shop_tab.items[i].price;
				break;
			case SHOP_COIN_TYPE_SECONDARY_COIN:
				pack_tab.items[i].price = shop_tab.items[i].price;
				break;
			}
			memset(pack_tab.items[i].aAttr, 0, sizeof(pack_tab.items[i].aAttr));
			memset(pack_tab.items[i].alSockets, 0, sizeof(pack_tab.items[i].alSockets));
#endif
		}

		memcpy(buf, &pack_tab, sizeof(pack_tab));
		buf += sizeof(pack_tab);
		size += sizeof(pack_tab);
	}

	pack.size = sizeof(pack) + sizeof(pack2) + size;

	ch->GetDesc()->BufferedPacket(&pack, sizeof(TPacketGCShop));
	ch->GetDesc()->BufferedPacket(&pack2, sizeof(TPacketGCShopStartEx));
	ch->GetDesc()->Packet(temp, size);

	return true;
}

int CShopEx::Buy(LPCHARACTER ch, BYTE pos)
{
	BYTE tabIdx = pos / SHOP_HOST_ITEM_MAX_NUM;
	BYTE slotPos = pos % SHOP_HOST_ITEM_MAX_NUM;
	if (tabIdx >= GetTabCount())
	{
		sys_log(0, "ShopEx::Buy : invalid position %d : %s", pos, ch->GetName());
		return SHOP_SUBHEADER_GC_INVALID_POS;
	}

	sys_log(0, "ShopEx::Buy : name %s pos %d", ch->GetName(), pos);

	auto it = m_map_guest.find(ch);

	if (it == m_map_guest.end())
		return SHOP_SUBHEADER_GC_END;

	TShopTableEx& shopTab = m_vec_shopTabs[tabIdx];
	TShopItemTable& r_item = shopTab.items[slotPos];

	if (r_item.price <= 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_GOLD_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}

	long long dwPrice = r_item.price;

#if defined(ENABLE_RENEWAL_SHOPEX)
	switch (r_item.price_type)
	{
	case SHOPEX_GOLD:
		if (ch->GetGold() < static_cast<int>(dwPrice))
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
		break;
	case SHOPEX_SECONDARY:
		if (ch->CountSpecifyTypeItem(ITEM_SECONDARY_COIN) < static_cast<int>(dwPrice))
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX;
		break;
	case SHOPEX_ITEM:
		if (ch->CountSpecifyItem(r_item.price_vnum) < static_cast<int>(dwPrice))
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_ITEM;
		break;
	case SHOPEX_EXP:
		if (ch->GetExp() < dwPrice)
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_EXP;
	}
#else
	switch (shopTab.coinType)
	{
	case SHOP_COIN_TYPE_GOLD:
		if (ch->GetGold() < (int)dwPrice)
		{
			sys_log(1, "ShopEx::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), static_cast<int>(dwPrice));
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
		}
		break;
	case SHOP_COIN_TYPE_SECONDARY_COIN:
	{
		int count = ch->CountSpecifyTypeItem(ITEM_SECONDARY_COIN);
		if (count < static_cast<int>(dwPrice))
		{
			sys_log(1, "ShopEx::Buy : Not enough myeongdojun : %s has %d, price %d", ch->GetName(), count, static_cast<int>(dwPrice));
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX;
		}
	}
	break;
	}
#endif

	LPITEM item = ITEM_MANAGER::instance().CreateItem(r_item.vnum, r_item.count);

	if (!item)
		return SHOP_SUBHEADER_GC_SOLD_OUT;

	int iEmptyPos;
	if (item->IsDragonSoul())
		iEmptyPos = ch->GetEmptyDragonSoulInventory(item);
#ifdef ENABLE_SPECIAL_INVENTORY
	else if (item->IsUpgradeItem())
		iEmptyPos = ch->GetEmptyUpgradeInventory(item);
	else if (item->IsPotions())
		iEmptyPos = ch->GetEmptyPotionsInventory(item);
	else if (item->IsBonus())
		iEmptyPos = ch->GetEmptyBonusInventory(item);
	else if (item->IsChest())
		iEmptyPos = ch->GetEmptyChestInventory(item);
#endif
	else
		iEmptyPos = ch->GetEmptyInventory(item->GetSize());

	if (iEmptyPos < 0)
	{
		sys_log(1, "ShopEx::Buy : Inventory full : %s size %d", ch->GetName(), item->GetSize());
		M2_DESTROY_ITEM(item);
		return SHOP_SUBHEADER_GC_INVENTORY_FULL;
	}

#ifdef ENABLE_BATTLE_PASS
	std::vector<DWORD> shopsBattlePass = { 14229, 16229, 17229, 30251, 30252, 50512, 50821, 50822, 50823, 50825, 50826, 53010, 70020, 71107, 71128, 71136, 71143, 71145, 72003, 72703, 70704, 80015 };
	if (std::count(shopsBattlePass.begin(), shopsBattlePass.end(), item->GetVnum()))
		ch->UpdateBattlePass(MISSION_FREE_SHOP_BUY, 1);
#endif

#if defined(ENABLE_RENEWAL_SHOPEX)
	switch (r_item.price_type)
	{
	case SHOPEX_GOLD:
		ch->ChangeGold(-static_cast<long long>(dwPrice));
		break;
	case SHOPEX_SECONDARY:
		ch->RemoveSpecifyTypeItem(ITEM_SECONDARY_COIN, dwPrice);
		break;
	case SHOPEX_ITEM:
		ch->RemoveSpecifyItem(r_item.price_vnum, dwPrice);
		break;
	case SHOPEX_EXP:
		ch->PointChange(POINT_EXP, -static_cast<int>(dwPrice), false);
	}

	item->SetAttributes(r_item.aAttr);

	for (BYTE i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
		if (r_item.alSockets[i] != 0)
			item->SetSocket(i, r_item.alSockets[i]);
#else
	switch (shopTab.coinType)
	{
	case SHOP_COIN_TYPE_GOLD:
		ch->PointChange(POINT_GOLD, -dwPrice, false);
		break;
	case SHOP_COIN_TYPE_SECONDARY_COIN:
		ch->RemoveSpecifyTypeItem(ITEM_SECONDARY_COIN, dwPrice);
		break;
	}
#endif

	if (item->IsDragonSoul())
		item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
#ifdef ENABLE_SPECIAL_INVENTORY
	else if (item->IsUpgradeItem())
		item->AddToCharacter(ch, TItemPos(UPGRADE_INVENTORY, iEmptyPos));
	else if (item->IsPotions())
		item->AddToCharacter(ch, TItemPos(POTIONS_INVENTORY, iEmptyPos));
	else if (item->IsBonus())
		item->AddToCharacter(ch, TItemPos(BONUS_INVENTORY, iEmptyPos));
	else if (item->IsChest())
		item->AddToCharacter(ch, TItemPos(CHEST_INVENTORY, iEmptyPos));
#endif
	else
		item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

	ITEM_MANAGER::instance().FlushDelayedSave(item);
	LogManager::instance().ItemLog(ch, item, "BUY_SHOP", item->GetName());

	ch->Save();

	return SHOP_SUBHEADER_GC_OK;
}

