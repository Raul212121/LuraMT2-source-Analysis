import ui
import uiToolTip
import item
import net
import grp
import wndMgr
import constInfo
import app

class Eveniment(ui.ScriptWindow):
	LITERE = 5
	VNUM_LITERE = [
	24471, #ITEM_VNUM LITERA S
	24472,
	24473,
	24474,
	24475,
	#24475,
	#24471,
	#24476,
	]

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.toolTip = None
		self.tooltipItem = None

		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.HideToolTip()

		self.dropletter = []

		self.LoadWindow()
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.LoadWindow()
		self.SetCenterPosition()

		ui.ScriptWindow.Show(self)

	def LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/eventlitere.py")
		except:
			import exception
			exception.Abort("eventlitere.LoadWindow.LoadObject")

		try:
			self.titleBar = self.GetChild("TitleBar")
			self.board = self.GetChild("board")
			self.reward_board = self.GetChild("board_reward")
			self.take_reward = self.GetChild("TakeReward")
			self.manage_reward = self.GetChild("ManageReward")
		except:
			import exception
			exception.Abort("eventlitere.__LoadWindow.BindObject")

		# Set func, exit game
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		# Set Func, take - reward
		self.take_reward.SetEvent(ui.__mem_func__(self.TakeReward))
		self.manage_reward.SetEvent(ui.__mem_func__(self.ManageReward))

		# Litere Slots
		wndItem = ui.GridSlotWindow()
		wndItem.SetParent(self)
		wndItem.SetPosition(45, 115)
		wndItem.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		wndItem.ArrangeSlot(0, self.LITERE, 1, 52, 48, 0, 0)
		wndItem.RefreshSlot()
		wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub",1.0, 1.0, 1.0, 1.0)
		wndItem.Show()

		self.wndItem = wndItem

		# Reward
		wndreward = ui.GridSlotWindow()
		wndreward.SetParent(self)
		wndreward.SetPosition(5, 247)
		wndreward.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		wndreward.SetOverInItemEvent(ui.__mem_func__(self.OverInItemFromReward))
		wndreward.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		wndreward.ArrangeSlot(0, 6, 3, 32, 32, 0, 0)
		wndreward.RefreshSlot()
		wndreward.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		wndreward.Hide()
		self.reward_board.Hide()

		self.wndreward = wndreward

		## load slots
		self.SloturiLitere()
		# self.SloturiLitere2()
		self.SloturiRecompensa()

		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.HideToolTip()

	def ManageReward(self):
		if self.wndreward.IsShow():
			self.wndreward.Hide()
			self.reward_board.Hide()
		else:
			self.wndreward.Show()
			self.reward_board.Show()

	def Close(self):
		if self.toolTip:
			self.toolTip.HideToolTip()

		self.Hide()

	def AddDropLetters(self, bPageIndex, bSlotIndex, bItemVnum, bItemCount):
		self.dropletter = [bItemVnum, bItemCount]

	def Destroy(self):
		self.ClearDictionary()

		self.tooltipItem = None
		self.toolTip = None
		self.wndItem = None
		self.wndreward = None

	def TakeReward(self):
		net.SendChatPacket("/give_reward")

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SloturiLitere(self):
		for index in range(self.LITERE):
			self.wndItem.SetItemSlot(index, self.VNUM_LITERE[index], 0)
			self.wndItem.ActivateSlot(index)

	def GetVnum(self,index):
		try:
			return int(constInfo.drop_letters[int(index)]["iVnum"])
		except KeyError:
			return 0

	def GetCount(self,index):
		try:
			return int(constInfo.drop_letters[int(index)]["iCount"])
		except KeyError:
			return 0

	def SloturiRecompensa(self):
		for i in xrange(constInfo.vnums_letters):
			vnum=self.GetVnum(i)
			itemCount = self.GetCount(i)

			self.wndreward.SetItemSlot(i, vnum, itemCount)

	def OverInItem(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetItemToolTip(self.VNUM_LITERE[slotIndex])

	def OverInItemFromReward(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetItemToolTip(constInfo.drop_letters[int(slotIndex)]["iVnum"])

	def OverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressExitKey(self):
		self.Close()
		return True
