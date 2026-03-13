import ui
import player
import mouseModule
import net
import app
import snd
import item
import chat
import uiRefine
import uiAttachMetin
import uiPickMoney
import uiCommon
import uiPrivateShopBuilder
import localeInfo
import constInfo
import ime
import wndMgr
import exchange

if app.__ENABLE_NEW_OFFLINESHOP__:
	import offlineshop
	import uiNewOfflineShop

ITEM_MALL_BUTTON_ENABLE = True



ITEM_FLAG_APPLICABLE = 1 << 14

class CostumeWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception

		if not app.ENABLE_COSTUME_SYSTEM:
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return

		ui.ScriptWindow.__init__(self)

		self.isLoaded = 0
		self.wndInventory = wndInventory

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		self.RefreshCostumeSlot()

		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CostumeWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			wndEquip = self.GetChild("CostumeSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		## Equipment
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndEquip = wndEquip

	def RefreshCostumeSlot(self):
		getItemVNum=player.GetItemIndex

		for i in xrange(item.COSTUME_SLOT_COUNT):
			slotNumber = item.COSTUME_SLOT_START + i
			self.wndEquip.SetItemSlot(slotNumber, getItemVNum(slotNumber), 0)

		if app.ENABLE_WEAPON_COSTUME_SYSTEM:
			self.wndEquip.SetItemSlot(item.COSTUME_SLOT_WEAPON, getItemVNum(item.COSTUME_SLOT_WEAPON), 0)

		self.wndEquip.RefreshSlot()

class InventoryWindow(ui.ScriptWindow):

	USE_TYPE_TUPLE = ("USE_CLEAN_SOCKET", "USE_CHANGE_ATTRIBUTE", "USE_ADD_ATTRIBUTE", "USE_ADD_ATTRIBUTE2", "USE_ADD_ACCESSORY_SOCKET", "USE_PUT_INTO_ACCESSORY_SOCKET", "USE_PUT_INTO_BELT_SOCKET", "USE_PUT_INTO_RING_SOCKET", "USE_EXTEND_TIME")

	if app.ENABLE_COSTUME_EXTENDED_RECHARGE:
		USE_TYPE_LIST = list(USE_TYPE_TUPLE)
		USE_TYPE_LIST.append("USE_TIME_CHARGE_PER")
		USE_TYPE_LIST.append("USE_TIME_CHARGE_FIX")
		USE_TYPE_TUPLE = tuple(USE_TYPE_LIST)



	SIDEBAR_BTN_WIKI = 0
	SIDEBAR_BTN_BIOLOG = 1
	SIDEBAR_BTN_BATTLEPASS = 2
	SIDEBAR_BTN_DEPOSIT = 3
	SIDEBAR_BTN_DUNGEON = 4
	SIDEBAR_BTN_EVENTS = 5
	SIDEBAR_BTN_SHOP = 6
	SIDEBAR_BTN_SWITCH = 7
	SIDEBAR_BTN_TELEPORT = 8
	SIDEBAR_BTN_MAX_NUM = 9

	SIDEBAR_BTN_ICONS = {
		SIDEBAR_BTN_WIKI : "d:/ymir work/ui/game/inventory/wikipedia.tga",
		SIDEBAR_BTN_BIOLOG : "d:/ymir work/ui/game/inventory/biolog.png",
		SIDEBAR_BTN_BATTLEPASS : "d:/ymir work/ui/game/inventory/bp.png",
		SIDEBAR_BTN_DEPOSIT : "d:/ymir work/ui/game/inventory/depozit.png",
		SIDEBAR_BTN_DUNGEON : "d:/ymir work/ui/game/inventory/dungeon.png",
		SIDEBAR_BTN_EVENTS : "d:/ymir work/ui/game/inventory/evenimente.png",
		SIDEBAR_BTN_SHOP : "d:/ymir work/ui/game/inventory/shop.png",
		SIDEBAR_BTN_SWITCH : "d:/ymir work/ui/game/inventory/switchbot.png",
		SIDEBAR_BTN_TELEPORT : "d:/ymir work/ui/game/inventory/teleport.tga",
	}			


	SIDEBAR_BTN_ICONS_PRESSED = { #le fac eu pe dict mai tarziu, nu ma injura motz, ms, pupiki
		SIDEBAR_BTN_WIKI : "d:/ymir work/ui/game/inventory/press/wikipedia.tga",
		SIDEBAR_BTN_BIOLOG : "d:/ymir work/ui/game/inventory/press/biolog.png",
		SIDEBAR_BTN_BATTLEPASS : "d:/ymir work/ui/game/inventory/press/bp.png",
		SIDEBAR_BTN_DEPOSIT : "d:/ymir work/ui/game/inventory/press/depozit.png",
		SIDEBAR_BTN_DUNGEON : "d:/ymir work/ui/game/inventory/press/dungeon.png",
		SIDEBAR_BTN_EVENTS : "d:/ymir work/ui/game/inventory/press/evenimente.png",
		SIDEBAR_BTN_SHOP : "d:/ymir work/ui/game/inventory/press/shop.png",
		SIDEBAR_BTN_SWITCH : "d:/ymir work/ui/game/inventory/press/switchbot.png",
		SIDEBAR_BTN_TELEPORT : "d:/ymir work/ui/game/inventory/press/teleport.tga",
	}				

	questionDialog = None
	tooltipItem = None
	wndCostume = None

	dlgPickMoney = None

	sellingSlotNumber = -1
	isLoaded = 0
	isOpenedCostumeWindowWhenClosingInventory = 0

	def __init__(self):
		if app.ENABLE_EASTER_EVENT:
			self.eggSlotNumber = 0
		self.sidebarButtons = []	
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.__BuildSidebar()


	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

		if self.isOpenedCostumeWindowWhenClosingInventory and self.wndCostume:
			self.wndCostume.Show()
		self.__ShowSidebar()

	def BindInterfaceClass(self, interface):
		self.interface = interface

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/InventoryWindow.py")
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.LoadObject")

		try:
			wndItem = self.GetChild("ItemSlot")
			wndEquip = self.GetChild("EquipmentSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.wndMoney = self.GetChild("Money")
			self.wndMoneySlot = self.GetChild("Money_Slot")
	
			self.costumeButton = self.GetChild2("CostumeButton")
			self.offlineShopButton = self.GetChild2("OfflineShopButton")

			self.inventoryTab = []
			self.inventoryTab.append(self.GetChild("Inventory_Tab_01"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_02"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_03"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_04"))

			self.equipmentTab = []
			self.equipmentTab.append(self.GetChild("Equipment_Tab_01"))
			self.equipmentTab.append(self.GetChild("Equipment_Tab_02"))

			self.GetChild("SortButton").SetEvent(self.__RequestSort)

			if self.costumeButton and not app.ENABLE_COSTUME_SYSTEM:
				self.costumeButton.Hide()
				self.costumeButton.Destroy()
				self.costumeButton = 0

		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.BindObject")

		## Item
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## Equipment
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## PickMoneyDialog
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.Hide()

		## RefineDialog
		self.refineDialog = uiRefine.RefineDialog()
		self.refineDialog.Hide()

		## AttachMetinDialog
		self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
		self.attachMetinDialog.Hide()

		## MoneySlot
		self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

		self.inventoryTab[0].SetEvent(lambda arg=0: self.SetInventoryPage(arg))
		self.inventoryTab[1].SetEvent(lambda arg=1: self.SetInventoryPage(arg))
		self.inventoryTab[2].SetEvent(lambda arg=2: self.SetInventoryPage(arg))
		self.inventoryTab[3].SetEvent(lambda arg=3: self.SetInventoryPage(arg))
		self.inventoryTab[0].Down()

		self.equipmentTab[0].SetEvent(lambda arg=0: self.SetEquipmentPage(arg))
		self.equipmentTab[1].SetEvent(lambda arg=1: self.SetEquipmentPage(arg))
		self.equipmentTab[0].Down()
		self.equipmentTab[0].Hide()
		self.equipmentTab[1].Hide()

		self.wndItem = wndItem
		self.wndEquip = wndEquip
		self.dlgPickMoney = dlgPickMoney


		# Costume Button
		if self.costumeButton:
			self.costumeButton.SetEvent(ui.__mem_func__(self.ClickCostumeButton))


		self.wndCostume = None

		if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
			self.listHighlightedSlot = []

		## Refresh
		self.SetInventoryPage(0)
		self.SetEquipmentPage(0)
		self.RefreshItemSlot()
		self.RefreshStatus()

	def Destroy(self):
		self.ClearDictionary()

		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = 0

		self.refineDialog.Destroy()
		self.refineDialog = 0

		self.attachMetinDialog.Destroy()
		self.attachMetinDialog = 0
		if app.ITEM_CHECKINOUT_UPDATE:
			self.wndSafeBox = None
		self.tooltipItem = None
		self.wndItem = 0
		self.wndEquip = 0
		self.dlgPickMoney = 0
		self.wndMoney = 0
		self.wndMoneySlot = 0
		self.questionDialog = None
		self.mallButton = None
		self.DSSButton = None
		self.interface = None

		if self.wndCostume:
			self.wndCostume.Destroy()
			self.wndCostume = 0

		if app.ENABLE_EASTER_EVENT:
			self.eggSlotNumber = 0

		self.inventoryTab = []
		self.equipmentTab = []

	def Hide(self):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			self.OnCloseQuestionDialog()
			return
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

		if self.wndCostume:
			self.isOpenedCostumeWindowWhenClosingInventory = self.wndCostume.IsShow()
			self.wndCostume.Close()

		if self.dlgPickMoney:
			self.dlgPickMoney.Close()

		try:
			self.__HideSidebar()
		except:
			pass

		wndMgr.Hide(self.hWnd)


	def Close(self):
		self.Hide()
		return True

	if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
		def HighlightSlot(self, slot):
			if not slot in self.listHighlightedSlot:
				self.listHighlightedSlot.append(slot)

	def EnableSidebarButton(self, btnIdx):
		btn = self.sidebarButtons[btnIdx]
		btn.Enable()
		btn.icon.Show()

	def DisableSidebarButton(self, btnIdx):
		btn = self.sidebarButtons[btnIdx]
		btn.Disable()
		btn.icon.Hide()

	def SAFE_SetSidebarButtonEvent(self, btnIdx, event):
		btn = self.sidebarButtons[btnIdx]
		btn.SAFE_SetEvent(event)

	def __HideSidebar(self):
		for btn in self.sidebarButtons:
			btn.Hide()

	def __ShowSidebar(self):
		for btn in self.sidebarButtons:
			btn.Show()		
		
	def __BuildSidebar(self):
		for i in xrange(self.SIDEBAR_BTN_MAX_NUM):
			btn = ui.Button()
			btn.AddFlag("float")
			btn.SetUpVisual(self.SIDEBAR_BTN_ICONS[i])
			btn.SetOverVisual(self.SIDEBAR_BTN_ICONS_PRESSED[i])
			btn.SetDownVisual(self.SIDEBAR_BTN_ICONS[i])

			btn.Hide()
			self.sidebarButtons.append(btn)

		self.__UpdateSidebarPosition()
		
	def __UpdateSidebarPosition(self):
		invX, invY = self.GetGlobalPosition()
		y = invY + 13

		for i in xrange(self.SIDEBAR_BTN_MAX_NUM):
			btn = self.sidebarButtons[i]

			x = invX - btn.GetWidth()
			btn.SetPosition(x, y)

			y += btn.GetHeight() + 2

	def SetInventoryPage(self, page):
		self.inventoryPageIndex = page
		for i in range(player.INVENTORY_PAGE_COUNT):
			if i!=page:
				self.inventoryTab[i].SetUp()
		self.RefreshBagSlotWindow()

	def SetEquipmentPage(self, page):
		self.equipmentPageIndex = page
		self.equipmentTab[1-page].SetUp()
		self.RefreshEquipSlotWindow()


	def ClickMallButton(self):
		import uiInventoryMenu
		uiInventoryMenu.wnd.Open()

	def ClickCostumeButton(self):
		if self.wndCostume:
			if self.wndCostume.IsShow():
				self.wndCostume.Hide()
			else:
				self.wndCostume.Show()
		else:
			self.wndCostume = CostumeWindow(self)
			self.wndCostume.Show()

	def OpenPickMoneyDialog(self):

		if mouseModule.mouseController.isAttached():

			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.SLOT_TYPE_SAFEBOX == mouseModule.mouseController.GetAttachedType():

				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

			mouseModule.mouseController.DeattachObject()

		else:
			curMoney = player.GetElk()

			if curMoney <= 0:
				return

			self.dlgPickMoney.SetTitleName(localeInfo.PICK_MONEY_TITLE)
			self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
			self.dlgPickMoney.Open(curMoney)
			self.dlgPickMoney.SetMax(7)

	def OnPickMoney(self, money):
		mouseModule.mouseController.AttachMoney(self, player.SLOT_TYPE_INVENTORY, money)

	def OnPickItem(self, count):
		itemSlotIndex = self.dlgPickMoney.itemGlobalSlotIndex
		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() and uiNewOfflineShop.IsSaleSlot(player.INVENTORY, itemSlotIndex):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
				return
		selectedItemVNum = player.GetItemIndex(itemSlotIndex)
		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, count)

	def __InventoryLocalSlotPosToGlobalSlotPos(self, local):
		if player.IsEquipmentSlot(local) or player.IsCostumeSlot(local):
			return local

		return self.inventoryPageIndex*player.INVENTORY_PAGE_SIZE + local

	def RefreshBagSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndItem.SetItemSlot

		for i in range(player.INVENTORY_PAGE_SIZE):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

			itemCount = getItemCount(slotNumber)
			if 0 == itemCount:
				self.wndItem.ClearSlot(i)
				continue
			elif 1 == itemCount:
				itemCount = 0

			itemVnum = getItemVNum(slotNumber)
			setItemVNum(i, itemVnum, itemCount)


			if itemVnum == 72501 or itemVnum == 72321: ## update 9 aprilie 2019
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in range(player.METIN_SOCKET_MAX_NUM)]
				isActivated = 0 != metinSocket[1]
				if isActivated:
					self.wndItem.ActivateSlot(i)
				else:
					self.wndItem.DeactivateSlot(i)

			elif app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
				if slotNumber in self.listHighlightedSlot:
					self.wndItem.ActivateSlot(i)

			if constInfo.IS_AUTO_POTION(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in range(player.METIN_SOCKET_MAX_NUM)]

				if slotNumber >= player.INVENTORY_PAGE_SIZE:
					slotNumber -= player.INVENTORY_PAGE_SIZE

				isActivated = 0 != metinSocket[0]

				if isActivated:
					self.wndItem.ActivateSlot(slotNumber)
					potionType = 0
					if constInfo.IS_AUTO_POTION_HP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_HP
					elif constInfo.IS_AUTO_POTION_SP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_SP

					usedAmount = int(metinSocket[1])
					totalAmount = int(metinSocket[2])
					player.SetAutoPotionInfo(potionType, isActivated, (totalAmount - usedAmount), totalAmount, self.__InventoryLocalSlotPosToGlobalSlotPos(i))

				else:
					self.wndItem.DeactivateSlot(slotNumber)

			if itemVnum in [71044,71045,71027,71028,71029,71030,27102,27105]:

				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in range(player.METIN_SOCKET_MAX_NUM)]

				if slotNumber >= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex:
					slotNumber -= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex

				isActivated = 0 != metinSocket[0]

				if isActivated:
					self.wndItem.ActivateSlot(i)
				else:
					self.wndItem.DeactivateSlot(i)

		self.wndItem.RefreshSlot()


	def RefreshEquipSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndEquip.SetItemSlot
		for i in range(player.EQUIPMENT_PAGE_COUNT):
			slotNumber = player.EQUIPMENT_SLOT_START + i
			itemCount = getItemCount(slotNumber)
			if itemCount <= 1:
				itemCount = 0
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)

		if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
			for i in range(player.NEW_EQUIPMENT_SLOT_COUNT):
				slotNumber = player.NEW_EQUIPMENT_SLOT_START + i
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)



		self.wndEquip.RefreshSlot()

		if self.wndCostume:
			self.wndCostume.RefreshCostumeSlot()

	def RefreshItemSlot(self):
		self.RefreshBagSlotWindow()
		self.RefreshEquipSlotWindow()

	def RefreshStatus(self):
		money = player.GetElk()
		self.wndMoney.SetText(localeInfo.NumberToMoneyString(money))

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SellItem(self):
		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() and uiNewOfflineShop.IsSaleSlot(player.INVENTORY, self.sellingSlotNumber):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
				return
		if self.sellingSlotitemIndex == player.GetItemIndex(self.sellingSlotNumber):
			if self.sellingSlotitemCount == player.GetItemCount(self.sellingSlotNumber):
				net.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count, player.INVENTORY)
				snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnDetachMetinFromItem(self):
		if None == self.questionDialog:
			return

		#net.SendItemUseToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)
		self.__SendUseItemToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return

		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			attachedCount = mouseModule.mouseController.GetAttachedItemCount()
			if app.__ENABLE_NEW_OFFLINESHOP__:
				if uiNewOfflineShop.IsBuildingShop() and uiNewOfflineShop.IsSaleSlot(player.SlotTypeToInvenType(attachedSlotType),attachedSlotPos):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
					return
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				self.__SendMoveItemPacket(attachedSlotPos, selectedSlotPos, attachedCount)

				if item.IsRefineScroll(attachedItemIndex):
					self.wndItem.SetUseMode(False)

			elif app.ENABLE_SWITCHBOT and player.SLOT_TYPE_SWITCHBOT == attachedSlotType:
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				net.SendItemMovePacket(player.SWITCHBOT, attachedSlotPos, player.INVENTORY, selectedSlotPos, attachedCount)

			elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
				mouseModule.mouseController.RunCallBack("INVENTORY")

			elif player.SLOT_TYPE_SHOP == attachedSlotType:
				net.SendShopBuyPacket(attachedSlotPos)

			elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:

				if player.ITEM_MONEY == attachedItemIndex:
					net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					net.SendSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)

			elif player.SLOT_TYPE_MALL == attachedSlotType:
				net.SendMallCheckoutPacket(attachedSlotPos, selectedSlotPos)

			elif app.ENABLE_SPECIAL_INVENTORY_SYSTEM and player.SLOT_TYPE_UPGRADE_INVENTORY == attachedSlotType:
				net.SendSpecialMovePacket(player.UPGRADE_INVENTORY, attachedSlotPos, selectedSlotPos, attachedCount)

			elif app.ENABLE_SPECIAL_INVENTORY_SYSTEM and player.SLOT_TYPE_POTIONS_INVENTORY == attachedSlotType:
				net.SendSpecialMovePacket(player.POTIONS_INVENTORY, attachedSlotPos, selectedSlotPos, attachedCount)

			elif app.ENABLE_SPECIAL_INVENTORY_SYSTEM and player.SLOT_TYPE_BONUS_INVENTORY == attachedSlotType:
				net.SendSpecialMovePacket(player.BONUS_INVENTORY, attachedSlotPos, selectedSlotPos, attachedCount)

			elif app.ENABLE_SPECIAL_INVENTORY_SYSTEM and player.SLOT_TYPE_CHEST_INVENTORY == attachedSlotType:
				net.SendSpecialMovePacket(player.CHEST_INVENTORY, attachedSlotPos, selectedSlotPos, attachedCount)

			mouseModule.mouseController.DeattachObject()


	def SelectItemSlot(self, itemSlotIndex):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return


		itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(itemSlotIndex)

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()

			if app.ENABLE_SPECIAL_INVENTORY_SYSTEM:
				if attachedSlotType in [ player.SLOT_TYPE_INVENTORY, player.SLOT_TYPE_UPGRADE_INVENTORY, player.SLOT_TYPE_POTIONS_INVENTORY, player.SLOT_TYPE_BONUS_INVENTORY, player.SLOT_TYPE_CHEST_INVENTORY]:
					self.__DropSrcItemToDestItemInInventory(attachedItemVID, attachedSlotPos, itemSlotIndex, attachedSlotType)
			else:
				if player.SLOT_TYPE_INVENTORY == attachedSlotType:
					self.__DropSrcItemToDestItemInInventory(attachedItemVID, attachedSlotPos, itemSlotIndex)

			mouseModule.mouseController.DeattachObject()

		else:

			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				self.__SellItem(itemSlotIndex)

			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)

			elif app.IsPressed(app.DIK_LALT):
				link = player.GetItemLink(itemSlotIndex)
				ime.PasteString(link)

			elif app.IsPressed(app.DIK_LSHIFT):
				itemCount = player.GetItemCount(itemSlotIndex)

				if itemCount > 1:
					self.dlgPickMoney.SetTitleName(localeInfo.PICK_ITEM_TITLE)
					self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickItem))
					self.dlgPickMoney.Open(itemCount)
					self.dlgPickMoney.itemGlobalSlotIndex = itemSlotIndex
				#else:
					#selectedItemVNum = player.GetItemIndex(itemSlotIndex)
					#mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum)

			elif app.IsPressed(app.DIK_LCONTROL):
				itemIndex = player.GetItemIndex(itemSlotIndex)

				if True == item.CanAddToQuickSlotItem(itemIndex):
					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_INVENTORY, itemSlotIndex)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.QUICKSLOT_REGISTER_DISABLE_ITEM)

			else:
				selectedItemVNum = player.GetItemIndex(itemSlotIndex)
				itemCount = player.GetItemCount(itemSlotIndex)
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)

				if self.__IsUsableItemToItem(selectedItemVNum, itemSlotIndex):
					self.wndItem.SetUseMode(True)
				else:
					self.wndItem.SetUseMode(False)

				snd.PlaySound("sound/ui/pick.wav")

	def	ExtendObjectTime(self):
		self.__SendUseItemToItemPacket(self.questionDialog.src, self.questionDialog.dst)
		self.OnCloseQuestionDialog()

	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos, attachedSlotType):
		if srcItemSlotPos == dstItemSlotPos and attachedSlotType == player.INVENTORY:
			return

		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() and (uiNewOfflineShop.IsSaleSlot(player.INVENTORY, srcItemSlotPos) or uiNewOfflineShop.IsSaleSlot(player.INVENTORY , dstItemSlotPos)):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
				return

		dstItemVnum = player.GetItemIndex(dstItemSlotPos)
		if dstItemVnum != 0:
			item.SelectItem(srcItemVID)
			srcItemType = item.GetItemType()
			srcItemSubType = item.GetItemSubType()
			item.SelectItem(dstItemVnum)
			if srcItemType == item.ITEM_TYPE_USE and srcItemSubType == item.USE_EXTEND_TIME and item.GetItemType() == item.ITEM_TYPE_COSTUME and (item.GetItemSubType() == item.COSTUME_TYPE_BODY or item.GetItemSubType() == item.COSTUME_TYPE_HAIR or item.GetItemSubType() == item.COSTUME_TYPE_WEAPON):
				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.EXTEND_TIME_OBJECT)
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.ExtendObjectTime))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				self.questionDialog.Open()
				self.questionDialog.src = srcItemSlotPos
				self.questionDialog.dst = dstItemSlotPos

		attachedSlotPos = mouseModule.mouseController.GetRealAttachedSlotNumber()
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()

			if attachedSlotType == 16:
				attachedSlotType = 10

			if attachedSlotType == 15:
				attachedSlotType = 9

			if attachedSlotType == 14:
				attachedSlotType = 8

			if attachedSlotType == 13:
				attachedSlotType = 7

			if attachedSlotType == 12:
				attachedSlotType = 6

		if item.IsRefineScroll(srcItemVID):
			self.RefineItem(srcItemSlotPos, dstItemSlotPos, attachedSlotPos)
			self.wndItem.SetUseMode(False)

		elif item.IsMetin(srcItemVID):
			self.AttachMetinToItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsDetachScroll(srcItemVID):
			self.DetachMetinFromItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsKey(srcItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif (player.GetItemFlags(srcItemSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif item.GetUseType(srcItemVID) in self.USE_TYPE_TUPLE:
			net.SendItemUseToItemPacket(attachedSlotType, attachedSlotPos, player.INVENTORY, dstItemSlotPos)

		else:
			#snd.PlaySound("sound/ui/drop.wav")

			if player.IsEquipmentSlot(dstItemSlotPos):

				if item.IsEquipmentVID(srcItemVID):
					self.__UseItem(srcItemSlotPos)

			else:
				self.__SendMoveItemPacket(srcItemSlotPos, dstItemSlotPos, 0)
				#net.SendItemMovePacket(srcItemSlotPos, dstItemSlotPos, 0)

	def __SellItem(self, itemSlotPos):
		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
				return

		if not player.IsEquipmentSlot(itemSlotPos):
			self.sellingSlotNumber = itemSlotPos
			itemIndex = player.GetItemIndex(itemSlotPos)
			itemCount = player.GetItemCount(itemSlotPos)


			self.sellingSlotitemIndex = itemIndex
			self.sellingSlotitemCount = itemCount

			item.SelectItem(itemIndex)
			## 20140220
			if item.IsAntiFlag(item.ANTIFLAG_SELL):
				popup = uiCommon.PopupDialog()
				popup.SetText(localeInfo.SHOP_CANNOT_SELL_ITEM)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return

			itemPrice = item.GetISellItemPrice()

			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 5
			else:
				itemPrice = itemPrice * itemCount / 5

			item.GetItemName(itemIndex)
			itemName = item.GetItemName()

			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, itemCount, itemPrice))
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellItem))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.count = itemCount

			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def __OnClosePopupDialog(self):
		self.pop = None

	def RefineItem(self, scrollSlotPos, targetSlotPos, attachedSlotPos = -1):
		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
				return
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			newScrollIndex = player.GetItemIndex(player.UPGRADE_INVENTORY, scrollSlotPos)

			if player.REFINE_OK != player.CanRefine(newScrollIndex, targetSlotPos):
				return

		if app.ENABLE_REFINE_RENEWAL:
			constInfo.AUTO_REFINE_TYPE = 1
			constInfo.AUTO_REFINE_DATA["ITEM"][0] = scrollSlotPos
			constInfo.AUTO_REFINE_DATA["ITEM"][1] = targetSlotPos

		###########################################################
		net.SendItemUseToItemPacket(attachedSlotType, attachedSlotPos, player.INVENTORY, targetSlotPos)#srcItemSlotPos
		#net.SendItemUseToItemPacket(scrollSlotPos, targetSlotPos)
		return
		###########################################################

		###########################################################
		#net.SendRequestRefineInfoPacket(targetSlotPos)
		#return
		###########################################################

		result = player.CanRefine(scrollIndex, targetSlotPos)
		if result == 0:
			result = player.CanRefine(scrollIndex, 10, targetSlotPos)

		if player.REFINE_ALREADY_MAX_SOCKET_COUNT == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_MORE_SOCKET)

		elif player.REFINE_NEED_MORE_GOOD_SCROLL == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NEED_BETTER_SCROLL)

		elif player.REFINE_CANT_MAKE_SOCKET_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_SOCKET_DISABLE_ITEM)

		elif player.REFINE_NOT_NEXT_GRADE_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_UPGRADE_DISABLE_ITEM)

		elif player.REFINE_CANT_REFINE_METIN_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.REFINE_OK != result:
			return

		self.refineDialog.Open(scrollSlotPos, targetSlotPos)

	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if not player.CanDetach(scrollIndex, targetSlotPos):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
			return

		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REFINE_DO_YOU_SEPARATE_METIN)
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()
		self.questionDialog.sourcePos = scrollSlotPos
		self.questionDialog.targetPos = targetSlotPos

	def AttachMetinToItem(self, metinSlotPos, targetSlotPos):
		metinIndex = player.GetItemIndex(metinSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		item.SelectItem(metinIndex)
		itemName = item.GetItemName()

		result = player.CanAttachMetin(metinIndex, targetSlotPos)

		if player.ATTACH_METIN_NOT_MATCHABLE_ITEM == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_CAN_NOT_ATTACH(itemName))

		if player.ATTACH_METIN_NO_MATCHABLE_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_SOCKET(itemName))

		elif player.ATTACH_METIN_NOT_EXIST_GOLD_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_GOLD_SOCKET(itemName))

		elif player.ATTACH_METIN_CANT_ATTACH_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.ATTACH_METIN_OK != result:
			return

		self.attachMetinDialog.Open(metinSlotPos, targetSlotPos)



	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()


	def OverInItem(self, overSlotPos):
		if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
			stat = 0
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
			itemVnum = player.GetItemIndex(slotNumber)
			if constInfo.IS_AUTO_POTION(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				tempSlotNum = slotNumber
				if tempSlotNum >= player.INVENTORY_PAGE_SIZE:
					tempSlotNum -= (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE)

				isActivated = 0 != metinSocket[0]
				if isActivated:
					stat = 1

			if not stat:
				if slotNumber in self.listHighlightedSlot:
					self.wndItem.DeactivateSlot(overSlotPos)
					try:
						self.listHighlightedSlot.remove(slotNumber)
					except:
						pass

		overSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
		self.wndItem.SetUsableItem(False)

		if mouseModule.mouseController.isAttached():
			attachedItemType = mouseModule.mouseController.GetAttachedType()
			if player.SLOT_TYPE_INVENTORY == attachedItemType:

				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()

				if attachedItemVNum==player.ITEM_MONEY: # @fixme005
					pass
				elif self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, overSlotPos):
					self.wndItem.SetUsableItem(True)
					self.ShowToolTip(overSlotPos)
					return

		self.ShowToolTip(overSlotPos)


	def __IsUsableItemToItem(self, srcItemVNum, srcSlotPos):
		if srcItemVNum != 0:
			item.SelectItem(srcItemVNum)
			if item.GetItemType() == item.ITEM_TYPE_USE and item.GetItemSubType() == item.USE_EXTEND_TIME:
				return True

		if item.IsRefineScroll(srcItemVNum):
			return True
		elif item.IsMetin(srcItemVNum):
			return True
		elif item.IsDetachScroll(srcItemVNum):
			return True
		elif item.IsKey(srcItemVNum):
			return True
		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True
		else:
			if item.GetUseType(srcItemVNum) in self.USE_TYPE_TUPLE:
				return True

		return False

	def __CanUseSrcItemToDstItem(self, srcItemVNum, srcSlotPos, dstSlotPos):
		if app.ENABLE_SPECIAL_INVENTORY_SYSTEM:
			if srcSlotPos == dstSlotPos and not item.IsMetin(srcItemVNum):
				return False
		else:
			if srcSlotPos == dstSlotPos:
				return False


		dstItemVnum = player.GetItemIndex(dstSlotPos)
		if dstItemVnum != 0:
			item.SelectItem(srcItemVNum)
			srcItemType = item.GetItemType()
			srcItemSubType = item.GetItemSubType()
			item.SelectItem(dstItemVnum)

			if srcItemType == item.ITEM_TYPE_USE and srcItemSubType == item.USE_EXTEND_TIME and item.GetItemType() == item.ITEM_TYPE_COSTUME and (item.GetItemSubType() == item.COSTUME_TYPE_BODY or item.GetItemSubType() == item.COSTUME_TYPE_HAIR or item.GetItemSubType() == item.COSTUME_TYPE_WEAPON):
				return True

		if item.IsRefineScroll(srcItemVNum):
			if player.REFINE_OK == player.CanRefine(srcItemVNum, dstSlotPos):
				return True
		elif item.IsMetin(srcItemVNum):
			if player.ATTACH_METIN_OK == player.CanAttachMetin(srcItemVNum, dstSlotPos):
				return True
		elif item.IsDetachScroll(srcItemVNum):
			if player.DETACH_METIN_OK == player.CanDetach(srcItemVNum, dstSlotPos):
				return True
		elif item.IsKey(srcItemVNum):
			if player.CanUnlock(srcItemVNum, dstSlotPos):
				return True

		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True

		else:
			useType=item.GetUseType(srcItemVNum)

			if "USE_CLEAN_SOCKET" == useType:
				if self.__CanCleanBrokenMetinStone(dstSlotPos):
					return True
			elif "USE_CHANGE_ATTRIBUTE" == useType:
				if self.__CanChangeItemAttrList(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE2" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ACCESSORY_SOCKET" == useType:
				if self.__CanAddAccessorySocket(dstSlotPos):
					return True
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == useType:
				if self.__CanPutAccessorySocket(dstSlotPos, srcItemVNum):
					return True
			elif "USE_TIME_CHARGE_PER" == useType:
				if self.__CanExtendTime(dstSlotPos):
					return True
			elif "USE_TIME_CHARGE_FIX" == useType:
				if self.__CanExtendTime(dstSlotPos):
					return True
				item.SelectItem(dstItemVNum)

		return False

	def __CanCleanBrokenMetinStone(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.ITEM_TYPE_WEAPON != item.GetItemType():
			return False

		for i in range(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemMetinSocket(dstSlotPos, i) == constInfo.ERROR_METIN_STONE:
				return True

		return False

	def __CanChangeItemAttrList(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):
			return False

		for i in range(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i) != 0:
				return True

		return False

	def __CanPutAccessorySocket(self, dstSlotPos, mtrlVnum):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return False

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return False

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)

		if mtrlVnum != constInfo.GET_ACCESSORY_MATERIAL_VNUM(dstItemVNum, item.GetItemSubType()):
			return False

		if curCount>=maxCount:
			return False

		return True

	def __CanAddAccessorySocket(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return False

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return False

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)

		ACCESSORY_SOCKET_MAX_SIZE = 3
		if maxCount >= ACCESSORY_SOCKET_MAX_SIZE:
			return False

		return True

	def __CanAddItemAttr(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):
			return False

		attrCount = 0
		for i in range(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i)[0] != 0:
				attrCount += 1

		if attrCount<4:
			return True

		return False

	if app.ENABLE_COSTUME_EXTENDED_RECHARGE:
		def __CanExtendTime(self, dstSlotPos):
			dstItemVNum = player.GetItemIndex(dstSlotPos)
			if dstItemVNum == 0:
				return False

			item.SelectItem(dstItemVNum)

			if item.GetItemType() != item.ITEM_TYPE_COSTUME:
				return False

			if app.ENABLE_PET_COSTUME_SYSTEM:
				if item.GetItemSubType() == item.COSTUME_TYPE_PET:
					return False

			if app.ENABLE_MOUNT_COSTUME_SYSTEM:
				if item.GetItemSubType() == item.COSTUME_TYPE_MOUNT:
					return False

			metinSlot = [player.GetItemMetinSocket(dstSlotPos, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
			leftSec = max(0, metinSlot[0] - app.GetGlobalTimeStamp())

			if leftSec >= item.MIN_INFINITE_DURATION:
				return False

			return True

	def ShowToolTip(self, slotIndex):
		if None != self.tooltipItem:
			itemVnum = player.GetItemIndex(slotIndex)
			if itemVnum != 0:
				self.tooltipItem.SetInventoryItem(slotIndex)
				self.tooltipItem.AppendEmojiForInventory(slotIndex, itemVnum)
				if app.__ENABLE_NEW_OFFLINESHOP__:
					if uiNewOfflineShop.IsBuildingShop() or uiNewOfflineShop.IsBuildingAuction():
						self.__AddTooltipSaleMode(slotIndex)

	if app.__ENABLE_NEW_OFFLINESHOP__:
		def __AddTooltipSaleMode(self, slot):
			if player.IsEquipmentSlot(slot):
				return

			itemIndex = player.GetItemIndex(slot)
			if itemIndex !=0:
				item.SelectItem(itemIndex)
				if item.IsAntiFlag(item.ANTIFLAG_MYSHOP) or item.IsAntiFlag(item.ANTIFLAG_GIVE):
					return

				self.tooltipItem.AddRightClickForSale()

	def OnTop(self):
		if None != self.tooltipItem:
			self.tooltipItem.SetTop()

		for btn in self.sidebarButtons:
			btn.SetTop()		

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def GetExchangeEmptyItemPos(self, itemHeight):
		inventorySize = exchange.EXCHANGE_ITEM_MAX_NUM
		inventoryWidth = 4
		GetBlockedSlots = lambda slot, size: [slot+(round*inventoryWidth) for round in range(size)]
		blockedSlots = [element for sublist in [GetBlockedSlots(slot, item.GetItemSize(item.SelectItem(exchange.GetItemVnumFromSelf(slot)))[1]) for slot in range(inventorySize) if exchange.GetItemVnumFromSelf(slot) != 0] for element in sublist]
		freeSlots = [slot for slot in range(inventorySize) if not slot in blockedSlots and not True in [e in blockedSlots for e in [slot+(round*inventoryWidth) for round in range(itemHeight)]]]
		return [freeSlots, -1][len(freeSlots) == 0]

	# if app.ENABLE_10X_CHEST_OPEN:
	def IsTreasureBox(self, slotIndex):
		itemVnum = player.GetItemIndex(slotIndex)
		item.SelectItem(itemVnum)

		if item.GetItemType() == item.ITEM_TYPE_GIFTBOX:
			return True

		treasures = [
			50011,
			50125,
			50131,
		]

		if itemVnum in treasures:
			return True

		return False

	def SendMultipleUseItemPacket(self, slotIndex):
		itemCount = player.GetItemCount(slotIndex)
		if itemCount == 0:
			return
		
		if itemCount > 10:
			itemCount = 10
		
		for i in range(itemCount):
			self.__SendUseItemPacket(slotIndex)


	def UseItemSlot(self, slotIndex):
		curCursorNum = app.GetCursor()
		if app.SELL == curCursorNum:
			return

		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return

		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)

		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop():
				globalSlot 	= slotIndex
				itemIndex 	= player.GetItemIndex(globalSlot)

				item.SelectItem(itemIndex)

				if not item.IsAntiFlag(item.ANTIFLAG_GIVE) and not item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
					offlineshop.ShopBuilding_AddInventoryItem(globalSlot)

				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)

				return

			elif uiNewOfflineShop.IsBuildingAuction():
				globalSlot = slotIndex
				itemIndex = player.GetItemIndex(globalSlot)

				item.SelectItem(itemIndex)

				if not item.IsAntiFlag(item.ANTIFLAG_GIVE) and not item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
					offlineshop.AuctionBuilding_AddInventoryItem(globalSlot)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)

				return

		if app.ITEM_CHECKINOUT_UPDATE:
			if app.IsPressed(app.DIK_LCONTROL) and self.wndSafeBox.IsShow() and slotIndex < player.EQUIPMENT_SLOT_START and not exchange.isTrading():
				net.SendSafeboxCheckinPacket(slotIndex)
				return

			if app.IsPressed(app.DIK_LCONTROL) and exchange.isTrading() and slotIndex < player.EQUIPMENT_SLOT_START:
				net.SendExchangeItemAddPacket(player.INVENTORY, slotIndex, -1)
				return

		self.__UseItem(slotIndex)
		mouseModule.mouseController.DeattachObject()
		self.OverOutItem()

	if app.ENABLE_EASTER_EVENT:
		def SetEggSlotNumber(self, eggSlotNumber):
			self.eggSlotNumber = 0

	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(slotIndex)
		if ItemVNum == 0:
			return

		item.SelectItem(ItemVNum)

		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() and uiNewOfflineShop.IsSaleSlot(player.INVENTORY, slotIndex):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
				return

		if app.ENABLE_EASTER_EVENT:
			if app.IsPressed(app.DIK_LCONTROL) and constInfo.IsItemEgg(slotIndex) and self.interface.wndEasterEvent.IsShow():
				if self.eggSlotNumber == 5:
					return


				self.interface.wndEasterEvent.SetItemSlot(ItemVNum, self.eggSlotNumber, slotIndex)
				self.eggSlotNumber = self.eggSlotNumber + 1
				return

		if item.IsFlag(item.ITEM_FLAG_CONFIRM_WHEN_USE):
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.INVENTORY_REALLY_USE_ITEM)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
			self.questionDialog.Open()
			self.questionDialog.slotIndex = slotIndex

			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

		if item.GetItemType() == item.ITEM_TYPE_GIFTBOX and app.IsPressed(app.DIK_LCONTROL):
			net.SendChestDropInfo(ItemVNum)
			return

		if ItemVNum == 50011 and app.IsPressed(app.DIK_LCONTROL):
			net.SendChestDropInfo(ItemVNum)
			return

		# if app.ENABLE_10X_CHEST_OPEN:
		if app.IsPressed(app.DIK_LALT) and self.IsTreasureBox(slotIndex):
			net.SendChatPacket("/chestdrop click {} {} {}".format(player.INVENTORY, slotIndex, 1000))
			return

		else:
			self.__SendUseItemPacket(slotIndex)
			#net.SendItemUsePacket(slotIndex)

	def __UseItemQuestionDialog_OnCancel(self):
		self.OnCloseQuestionDialog()

	def __UseItemQuestionDialog_OnAccept(self):
		self.__SendUseItemPacket(self.questionDialog.slotIndex)
		self.OnCloseQuestionDialog()

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() or uiNewOfflineShop.IsBuildingAuction():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
				return

		net.SendItemUseToItemPacket(srcSlotPos, dstSlotPos)

		# net.SendItemUseToItemPacket(srcSlotPos, dstSlotPos)

	def __SendUseItemPacket(self, slotPos):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() or uiNewOfflineShop.IsBuildingAuction():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
				return

		net.SendItemUsePacket(slotPos)

	def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() or uiNewOfflineShop.IsBuildingAuction():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
				return

		net.SendItemMovePacket(srcSlotPos, dstSlotPos, srcItemCount)

	if app.ITEM_CHECKINOUT_UPDATE:
		def SetSafeboxWindow(self, wndSafeBox):
			self.wndSafeBox = wndSafeBox

	def OnMoveWindow(self, x, y):
		print ("Inventory Global Pos : ", self.GetGlobalPosition())
		self.__UpdateSidebarPosition()

	def __RequestSort(self):
		if self.questionDialog:
			self.OnCloseQuestionDialog()

		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText("Esti sigur ca vrei sa sortezi inventarul?")
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__Sort))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()

	def __Sort(self):
		self.OnCloseQuestionDialog()
		if app.__ENABLE_NEW_OFFLINESHOP__:
			if uiNewOfflineShop.IsBuildingShop() or uiNewOfflineShop.IsBuildingAuction():
				return

		net.SendChatPacket("/sortinv")
