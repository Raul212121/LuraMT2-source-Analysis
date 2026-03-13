import ui
import snd
import shop
import mouseModule
import player
import chr
import net
import uiCommon
import localeInfo
import chat
import item
import systemSetting
import player
import app
import os
g_isBuildingPrivateShop = False
g_itemPriceDict = {}
g_privateShopAdvertisementBoardDict = {}
g_privateShopAdvertisementLastViewed = {}
g_displayedBoardVIDList = []

##### DISABLE/ENABLE SHOP VISIT COLOR ###
SHOP_VISIT=True
##### SHOP VISIT COLOR #####
SHOP_VISIT_COLOR=0xFFf48042
SHOP_NORMAL_COLOR=0xFFFFFFFF
###########################


def Clear():
	global g_itemPriceDict
	global g_isBuildingPrivateShop
	g_itemPriceDict={}
	g_isBuildingPrivateShop = False

	# @fixme007 BEGIN
	global g_privateShopAdvertisementBoardDict
	g_privateShopAdvertisementBoardDict={}
	# @fixme007 END

def IsPrivateShopItemPriceList():
	return g_itemPriceDict

def IsBuildingPrivateShop():
	global g_isBuildingPrivateShop
	return player.IsOpenPrivateShop() or g_isBuildingPrivateShop

def SetPrivateShopItemPrice(itemVNum, itemPrice):
	global g_itemPriceDict
	g_itemPriceDict[int(itemVNum)]=itemPrice

def GetPrivateShopItemPrice(itemVNum):
	try:
		return g_itemPriceDict[itemVNum]
	except KeyError:
		return 0

def DeleteADBoard(vid):
	if not g_privateShopAdvertisementBoardDict.has_key(vid):
		return

	global g_privateShopAdvertisementLastViewed
	board = g_privateShopAdvertisementBoardDict[vid]
	# If we had offline time, and it should persist, save it so that it does
	if board.lastSeen > 0 and board.lastSeen + PrivateShopAdvertisementBoard.viewedPersistMinutes*60 > app.GetTime():
		g_privateShopAdvertisementLastViewed[vid] = board.lastSeen

	del g_privateShopAdvertisementBoardDict[vid]

def ClearSign():
	global g_privateShopAdvertisementBoardDict
	global g_displayedBoardVIDList
	global g_privateShopAdvertisementLastViewed
	if g_privateShopAdvertisementBoardDict and  type(g_privateShopAdvertisementBoardDict) is dict:
		for key in g_privateShopAdvertisementBoardDict:
			DeleteADBoard(key)
	g_privateShopAdvertisementBoardDict = {}
	g_displayedBoardVIDList = {}
	g_privateShopAdvertisementLastViewed = {}

def RefreshShopBoards():
	global g_displayedBoardVIDList

	# Initialization
	showSalesText = systemSetting.IsShowSalesText()
	allBoardVIDList = g_privateShopAdvertisementBoardDict.keys()
	dictKeys = []

	# Limit the display of shops to those around us if we've chosen to display all
	if showSalesText:
		boardsDist = {}
		for vid in allBoardVIDList:
			dist = player.GetCharacterDistance(vid)
			if dist > 3000: # Too far!
				continue

			boardsDist[vid] = dist

		# This will get us a new keys tuple with the keys sorted
		dictKeys = sorted(boardsDist, key=boardsDist.get)

		# And then we'll pick the first few (i.e those closest to us)
		# ...as well as the board we are hovering / selected
		dictKeys = dictKeys[0:int(100.0)]

	# We'll always display the selected target and the hovered target's names.
	dictKeys = [player.GetTargetVID(), chr.Pick()] + dictKeys

	for vid in dictKeys:
		if not vid in allBoardVIDList:
			continue

		board = g_privateShopAdvertisementBoardDict[vid]
		board.Show()

		# Return back to the color if it's required
		if board.bg == "purple" and board.lastSeen + board.viewedPersistMinutes * 60 < app.GetTime():
			board.MarkUnseen()

	# Hide the ones that were visible before but are not now
	for vid in g_displayedBoardVIDList:
		if vid not in dictKeys and vid in allBoardVIDList:
			g_privateShopAdvertisementBoardDict[vid].Hide()

	# Update the visible board tuple
	g_displayedBoardVIDList = dictKeys


class PrivateShopAdvertisementBoard(ui.ThinBoard):
	# These are the minutes for which the shop will display its different "viewed" color.
	viewedPersistMinutes = 30

	def __init__(self, dlgShop):
		ui.ThinBoard.__init__(self, "UI_BOTTOM")
		self.dlgShop = dlgShop
		self.vid = None
		self.title = ""
		self.bg = "new"
		self.lastSeen = 0
		self.__MakeTextLine()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def __MakeTextLine(self):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.Show()

	def Open(self, vid, text):
		self.vid = vid
		self.title = text

		self.textLine.SetText(text)
		self.textLine.UpdateRect()
		self.SetSize(len(text)*6 + 10*2, 10)
		if vid in g_privateShopAdvertisementLastViewed:
			self.lastSeen = g_privateShopAdvertisementLastViewed[vid]
		g_privateShopAdvertisementBoardDict[vid] = self

	def UpdateTitle(self, text):
		self.title = text

	def OnMouseLeftButtonDown(self):
		if self.dlgShop and self.vid != self.dlgShop.vid:
			self.dlgShop.Close()
	def OnMouseLeftButtonUp(self):
		if not self.vid:
			return
		self.MarkSeen()
		net.SendOnClickPacket(self.vid)
		return True

	def UpdatePattern(self, name):
		if self.bg == name:
			return
		self.bg = name

	def MarkUnseen(self):
		self.UpdatePattern("new")
		self.textLine.SetPackedFontColor(SHOP_NORMAL_COLOR)

	def MarkSeen(self):
		self.lastSeen = app.GetTime()
		self.UpdatePattern("purple")
		self.textLine.SetPackedFontColor(SHOP_VISIT_COLOR)
	def Destroy(self):
		DeleteADBoard(self.vid)

	def OnUpdate(self):
		if self.IsShow():
			(x, y) = chr.GetProjectPosition(self.vid, 220)
			self.SetPosition(x - self.GetWidth()/2, y - self.GetHeight()/2)
class PrivateShopBuilder(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__LoadWindow()
		self.itemStock = {}
		self.tooltipItem = None
		self.priceInputBoard = None
		self.days = 0
		self.interface = None
		self.title = ""

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopBuilder.py")
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.LoadObject")

		try:
			GetObject = self.GetChild
			self.nameLine = GetObject("NameLine")
			self.itemSlot = GetObject("ItemSlot")
			self.btnOk = GetObject("OkButton")
			self.btnClose = GetObject("CloseButton")
			self.titleBar = GetObject("TitleBar")
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.BindObject")

		self.btnOk.SetEvent(ui.__mem_func__(self.OnOk))
		self.btnClose.SetEvent(ui.__mem_func__(self.OnClose))
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.OnClose))

		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

	def Destroy(self):
		self.ClearDictionary()

		self.nameLine = None
		self.itemSlot = None
		self.btnOk = None
		#self.days = 0
		self.btnClose = None
		self.titleBar = None
		self.priceInputBoard = None

	def Open(self, title,days):

		self.days = days
		self.title = title

		if len(title) > 25:
			title = title[:22] + "..."

		self.itemStock = {}
		shop.ClearPrivateShopStock()
		self.nameLine.SetText(title)
		self.SetCenterPosition()
		self.Refresh()
		self.Show()
		self.SetTop()

		global g_isBuildingPrivateShop
		g_isBuildingPrivateShop = True

	def Close(self):
		global g_isBuildingPrivateShop
		g_isBuildingPrivateShop = False

		self.priceInputBoard = None
		self.title = ""
		#self.days = 0
		self.itemStock = {}
		shop.ClearPrivateShopStock()
		self.Hide()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def Refresh(self):
		getitemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setitemVNum=self.itemSlot.SetItemSlot
		delItem=self.itemSlot.ClearSlot

		for i in xrange(shop.SHOP_SLOT_COUNT):
			if not self.itemStock.has_key(i):
				delItem(i)
				continue

			pos = self.itemStock[i]

			itemCount = getItemCount(*pos)
			if itemCount <= 1:
				itemCount = 0
			setitemVNum(i, getitemVNum(*pos), itemCount)

		self.itemSlot.RefreshSlot()

	def OnSelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			if app.ENABLE_SPECIAL_INVENTORY_SYSTEM:
				if player.SLOT_TYPE_INVENTORY != attachedSlotType and\
					player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedSlotType and\
					player.SLOT_TYPE_UPGRADE_INVENTORY != attachedSlotType and\
					player.SLOT_TYPE_POTIONS_INVENTORY != attachedSlotType and\
					player.SLOT_TYPE_BONUS_INVENTORY != attachedSlotType and\
					player.SLOT_TYPE_CHEST_INVENTORY != attachedSlotType:
					return
			else:
				if player.SLOT_TYPE_INVENTORY != attachedSlotType and player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedSlotType:
					return

			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)

			itemVNum = player.GetItemIndex(attachedInvenType, attachedSlotPos)
			count = player.GetItemCount(attachedInvenType, attachedSlotPos)
			item.SelectItem(itemVNum)

			if item.IsAntiFlag(item.ANTIFLAG_GIVE) or item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PRIVATE_SHOP_CANNOT_SELL_ITEM)
				return

			priceInputBoard = uiCommon.MoneyInputDialog()

			priceInputBoard.SetTitle(localeInfo.PRIVATE_SHOP_INPUT_PRICE_DIALOG_TITLE)
			priceInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputPrice))
			priceInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputPrice))
			#priceInputBoard.SetMaxLength(16)
			priceInputBoard.Open()

			itemPrice=self.ReadFilePrice(itemVNum,count)

			if itemPrice>0:
				priceInputBoard.SetValue(itemPrice)

			self.priceInputBoard = priceInputBoard
			self.priceInputBoard.itemVNum = itemVNum
			self.priceInputBoard.sourceWindowType = attachedInvenType
			self.priceInputBoard.sourceSlotPos = attachedSlotPos
			self.priceInputBoard.targetSlotPos = selectedSlotPos



	def OnSelectItemSlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			snd.PlaySound("sound/ui/loginfail.wav")
			mouseModule.mouseController.DeattachObject()

		else:
			if not selectedSlotPos in self.itemStock:
				return

			invenType, invenPos = self.itemStock[selectedSlotPos]
			shop.DelPrivateShopItemStock(invenType, invenPos)
			snd.PlaySound("sound/ui/drop.wav")

			del self.itemStock[selectedSlotPos]

			self.Refresh()

	def ReadFilePrice(self,vnum,count):
		d = "lib/shops"
		if not os.path.exists(d):
			os.makedirs(d)
		oldPrice=0
		n=d+"/"+str(vnum)+"_"+str(count)+".txt"
		if os.path.exists(n):
			fd = open( n,'r')
			oldPrice=int(fd.readlines()[0])

		return oldPrice
	def SaveFilePrice(self,vnum,count,price):
		d = "lib/shops"
		if not os.path.exists(d):
			os.makedirs(d)
		n=d+"/"+str(vnum)+"_"+str(count)+".txt"
		f = file(n, "w+")
		f.write(str(price))
		f.close()

	def AcceptInputPrice(self):

		if not self.priceInputBoard:
			return True

		text = self.priceInputBoard.GetText()

		if not text:
			return True

		if not text.isdigit():
			return True

		if long(text or 0) <= 0:
			return True

		attachedInvenType = self.priceInputBoard.sourceWindowType
		sourceSlotPos = self.priceInputBoard.sourceSlotPos
		targetSlotPos = self.priceInputBoard.targetSlotPos

		for privatePos, (itemWindowType, itemSlotIndex) in self.itemStock.items():
			if itemWindowType == attachedInvenType and itemSlotIndex == sourceSlotPos:
				shop.DelPrivateShopItemStock(itemWindowType, itemSlotIndex)
				del self.itemStock[privatePos]

		price = long(self.priceInputBoard.GetText())

		if IsPrivateShopItemPriceList():
			SetPrivateShopItemPrice(self.priceInputBoard.itemVNum, price)

		shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price)
		count = player.GetItemCount(attachedInvenType, sourceSlotPos)
		vnum = player.GetItemIndex(attachedInvenType, sourceSlotPos)
		self.SaveFilePrice(vnum,count,price)
		self.itemStock[targetSlotPos] = (attachedInvenType, sourceSlotPos)
		snd.PlaySound("sound/ui/drop.wav")

		self.Refresh()

		#####

		self.priceInputBoard = None
		return True

	def CancelInputPrice(self):
		self.priceInputBoard = None
		return True

	def OnOk(self):

		if not self.title:
			return

		if 0 == len(self.itemStock):
			return

		shop.BuildPrivateShop(self.title,self.days)
		self.Close()

	def OnClose(self):
		self.Close()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnOverInItem(self, slotIndex):

		if self.tooltipItem:
			if self.itemStock.has_key(slotIndex):
				self.tooltipItem.SetPrivateShopBuilderItem(*self.itemStock[slotIndex] + (slotIndex,))

	def OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
