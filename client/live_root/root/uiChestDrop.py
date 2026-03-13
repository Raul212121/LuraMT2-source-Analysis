import chat, net, player, wndMgr, mouseModule, ui

class ChestDropWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.tooltipItem = None

		self.currentChest = 0
		self.currentPage = 1
		self.openAmount = 1
		self.invItemPos = -1

		self.chestDrop = { }

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/chestdropwindow.py")
		except:
			import exception
			exception.Abort("ChestDropWindow.__LoadWindow.LoadObject")

		try:
			self.board = self.GetChild("board")
			self.titleBar = self.GetChild("TitleBar")
			self.prevButton = self.GetChild("prev_button")
			self.nextButton = self.GetChild("next_button")
			self.currentPageBack = self.GetChild("CurrentPageBack")
			self.currentPageText = self.GetChild("CurrentPage")
		except:
			import exception
			exception.Abort("ChestDropWindow.__LoadWindow.BindObject")

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))


		self.prevButton.SetEvent(ui.__mem_func__(self.OnClickPrevPage))
		self.nextButton.SetEvent(ui.__mem_func__(self.OnClickNextPage))

		self.currentPageText.SetText(str(self.currentPage))

		wndItem = ui.GridSlotWindow()
		wndItem.SetParent(self)
		wndItem.SetPosition(8, 35)
		wndItem.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		wndItem.ArrangeSlot(0, 10, 4, 32, 32, 0, 0)
		wndItem.RefreshSlot()
		wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		wndItem.Show()

		self.wndItem = wndItem

	def Close(self):
		self.invItemPos = -1
		self.Hide()

	def Destroy(self):
		self.ClearDictionary()

		self.tooltipItem = None
		self.wndItem = None

		self.currentChest = 0
		self.currentPage = 1
		self.openAmount = 1
		self.invItemPos = -1
		self.chestDrop = { }

	def Open(self):
		if self.IsShow():
			return
		self.currentChest = 0
		self.currentPage = 1
		self.chestDrop = { }
		self.RefreshItemSlot()

		self.SetTop()
		self.SetCenterPosition()
		self.Show()

	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip

	def AddChestDropItem(self, chestVnum, pageIndex, slotIndex, itemVnum, itemCount):
		self.Open()
		if not self.chestDrop.has_key(chestVnum):
			self.chestDrop[chestVnum] = {}

		if not self.chestDrop[chestVnum].has_key(pageIndex):
			self.chestDrop[chestVnum][pageIndex] = {}

		if self.chestDrop[chestVnum].has_key(pageIndex):
			if self.chestDrop[chestVnum][pageIndex].has_key(slotIndex):
				if self.chestDrop[chestVnum][pageIndex][slotIndex][0] == itemVnum and self.chestDrop[chestVnum][pageIndex][slotIndex][1] == itemCount:
					return

		self.chestDrop[chestVnum][pageIndex][slotIndex] = [itemVnum, itemCount]

	def OnClickOpenChest(self):
		if self.invItemPos == -1:
			return

		itemCount = player.GetItemCount(self.invItemPos)

		if itemCount >= self.openAmount:
			for i in xrange(self.openAmount):
				if itemCount == 1:
					net.SendItemUsePacket(self.invItemPos)
					self.OnPressEscapeKey()
					break

				net.SendItemUsePacket(self.invItemPos)
				itemCount = itemCount - 1
		else:
			for i in xrange(itemCount):
				if itemCount == 1:
					net.SendItemUsePacket(self.invItemPos)
					self.OnPressEscapeKey()
					break

				net.SendItemUsePacket(self.invItemPos)
				itemCount = itemCount - 1

	def OnClickPrevPage(self):
		if not self.chestDrop.has_key(self.currentChest):
			return

		if self.chestDrop[self.currentChest].has_key(self.currentPage - 1):
			self.currentPage = self.currentPage - 1
			self.currentPageText.SetText(str(self.currentPage))
			self.RefreshItemSlot()

	def OnClickNextPage(self):
		if not self.chestDrop.has_key(self.currentChest):
			return

		if self.chestDrop[self.currentChest].has_key(self.currentPage + 1):
			self.currentPage = self.currentPage + 1
			self.currentPageText.SetText(str(self.currentPage))
			self.RefreshItemSlot()

	def EnableMultiPage(self):
		self.prevButton.Show()
		self.nextButton.Show()
		self.currentPageBack.Show()
		self.board.SetSize(340,202)

	def EnableSinglePage(self):
		self.prevButton.Hide()
		self.nextButton.Hide()
		self.currentPageBack.Hide()
		self.board.SetSize(340,154+25)


	def GetInvItemSlot(self):
		return self.invItemPos

	def RefreshItems(self, chestVnum):
		if chestVnum:
			self.currentChest = chestVnum

		if not self.chestDrop.has_key(self.currentChest):
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Acest cufar nu are drop. Raporteaza probleme unui administrator.")
			self.Close()
			return

		if self.chestDrop[self.currentChest].has_key(2):
			self.EnableMultiPage()
		else:
			self.EnableSinglePage()

		self.RefreshItemSlot()

	def RefreshItemSlot(self):
		for i in xrange(15 * 5):
			self.wndItem.ClearSlot(i)

		if not self.chestDrop.has_key(self.currentChest):
			return

		if not self.chestDrop[self.currentChest].has_key(self.currentPage):
			return

		for key, value in self.chestDrop[self.currentChest][self.currentPage].iteritems():
			itemVnum = value[0]
			itemCount = value[1]

			if itemCount <= 1:
				itemCount = 0

			self.wndItem.SetItemSlot(key, itemVnum, itemCount)

		wndMgr.RefreshSlot(self.wndItem.GetWindowHandle())

	def OverInItem(self, slotIndex):
		if mouseModule.mouseController.isAttached():
			return

		if not self.chestDrop.has_key(self.currentChest):
			return

		if not self.chestDrop[self.currentChest].has_key(self.currentPage):
			return

		if 0 != self.tooltipItem:
			self.tooltipItem.SetItemToolTip(self.chestDrop[self.currentChest][self.currentPage][slotIndex][0])

	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnPressEscapeKey(self):
		self.Close()
		return True
