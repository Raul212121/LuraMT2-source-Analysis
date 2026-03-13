import net
import ui
import uiCommon
import localeInfo
import constInfo

class EasterEvent(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.tooltipItem = None
		self.attachedSlotPos = 0
		self.setItemVnum = 0
		self.eggItemVnum = 0
		self.eggCount = 0
		self.questionDialog = None
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/easterevent.py")

			self.__BindObject()
			self.__BindEvent()
		except:
			import exception
			exception.Abort("EasterEvent.__LoadWindow")

	def __BindObject(self):
		self.boardTitleBar = self.GetChild("BoardWithTitle")
		self.easterBasket = self.GetChild("easterBasket")

	def __BindEvent(self):
		self.boardTitleBar.SetCloseEvent(ui.__mem_func__(self.Close))


	def BindInterface(self, interface):
		self.interface = interface

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def Destroy(self):
		self.ClearDictionary()
		self.tooltipItem = None
		self.attachedSlotPos = 0
		self.setItemVnum = 0
		self.eggItemVnum = 0
		self.interface = None
		self.eggCount = 0
		self.questionDialog = None

	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

		for i in range(5):
			self.ClearEggSlot(i)

		self.Hide()

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.SetTop()
			self.Show()

	def ClearEggSlot(self, selectedSlotPos):
		self.eggItemVnum = 0
		self.eggCount = 0
		self.interface.wndInventory.SetEggSlotNumber(0)

		self.easterBasket.LoadImage("d:/ymir work/ui/game/easter_event/black.png")

	def SetItemSlot(self, itemIndex, selectedSlotPos, attachedSlotPos):
		if itemIndex != constInfo.EGGS_VNUM[0] and \
			 itemIndex != constInfo.EGGS_VNUM[1] and \
			 itemIndex != constInfo.EGGS_VNUM[2] and \
			 itemIndex != constInfo.EGGS_VNUM[3] and \
			 itemIndex != constInfo.EGGS_VNUM[4]:
			return

		self.eggItemVnum = itemIndex
		self.attachedSlotPos = attachedSlotPos

		self.eggCount = self.eggCount +1
		self.easterBasket.LoadImage("d:/ymir work/ui/game/easter_event/{}.png".format(self.eggCount))

		if self.eggCount == 5:
			questionDialog = uiCommon.QuestionDialogWithTimeLimitTHL()
			questionDialog.SetText1(localeInfo.COMPLETE_BASKET)
			questionDialog.SetTimeOverMsg("Timpul a expirat.")
			questionDialog.SetTimeOverEvent(self.AnswerQuestion, False)
			questionDialog.SetAcceptEvent(lambda arg=True: self.AnswerQuestion(arg))
			questionDialog.SetCancelEvent(lambda arg=False: self.AnswerQuestion(arg))
			questionDialog.Open(10)
			self.questionDialog = questionDialog

	def AnswerQuestion(self, answer):
		if not self.questionDialog:
			return

		if answer:
			net.SendChatPacket("/get_easter_reward")
			self.Close()

		self.questionDialog.Close()
		self.questionDialog = None

	def OnPressEscapeKey(self):
		self.Close()
		return True

