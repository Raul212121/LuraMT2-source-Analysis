import ui
import net
import chat
import item
import player
import exception
import constInfo

import uiCommon
import uiToolTip
import uiScriptLocale

class ChangerWindow(ui.ScriptWindow):

	MAX_BONUSES = 5

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.ChangerPosition = None
		self.ItemPosition = None
		self.ChangersCount = 0

		self.acceptQuestionDialog = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/bonuschanger.py")
		except:
			exception.Abort("ChangerWindow.LoadDialog.LoadObject")

		try:
			self.TitleBar = self.GetChild("TitleBar")
			self.Board = self.GetChild("Board")
			self.ItemsSlots = self.GetChild("ItemsSlots")

			self.BonusName = [self.GetChild("BonusName{}".format(i)) for i in range(1, 6)]
			self.BonusInput = [self.GetChild("BonusInput{}".format(i)) for i in range(1, 6)]

			self.ChangeBonusButton = self.GetChild("ChangeButton")

		except:
			exception.Abort("ChangerWindow.LoadDialog.BindObject")

		self.BonusBackground = ui.BorderA()
		self.BonusBackground.SetParent(self.Board)
		self.BonusBackground.SetSize(300, 165)
		self.BonusBackground.SetPosition(10, 250)
		self.BonusBackground.Show()

		self.ChangeBonusButton.SetEvent(ui.__mem_func__(self.ChangeBonus))
		self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.ItemsSlots.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.ItemsSlots.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.ItemToolTip = uiToolTip.ItemToolTip()
		self.ItemToolTip.Hide()

	def OverInItem(self, slot):
		if self.ItemToolTip and self.ItemPosition != None and self.ChangerPosition != None:
			if slot == 0:
				self.ItemToolTip.SetInventoryItem(self.ItemPosition)
				self.ItemToolTip.Show()
			elif slot == 1:
				self.ItemToolTip.SetInventoryItem(self.ChangerPosition)
				self.ItemToolTip.Show()

	def OverOutItem(self):
		if self.ItemToolTip:
			self.ItemToolTip.Hide()

	def AddItems(self, itemPositon, changerPosition):
		if item.ITEM_TYPE_WEAPON == item.GetItemType() or item.ITEM_TYPE_ARMOR == item.GetItemType():
			attrSlot = [player.GetItemAttribute(itemPositon, i) for i in xrange(self.MAX_BONUSES)]
			countBonus = sum(1 for attr in attrSlot if attr[0] != 0)

			for i in range(self.MAX_BONUSES):
				if i < countBonus:
					self.BonusName[i].Show()
					self.BonusInput[i].Show()
					self.BonusInput[i].SetParent(self.BonusBackground)
				else:
					self.BonusName[i].Hide()
					self.BonusInput[i].Hide()
					self.BonusInput[i].SetParent(self.BonusBackground)

			for i in range(countBonus):
				type = attrSlot[i][0]
				value = attrSlot[i][1]
				affectString = self.__GetBonusName(type, value)

				if affectString:
					self.BonusName[i].SetText(affectString)
					self.BonusInput[i].Show()
					self.BonusInput[i].SetParent(self.BonusBackground)
				else:
					self.BonusInput[i].Hide()
					self.BonusInput[i].SetParent(self.BonusBackground)

			board_width = 320
			board_height = 425

			board_width2 = 300
			board_height2 = 165

			if countBonus == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO, uiScriptLocale.BONUS_CHANGER_ERROR_ITEM)
				return
			elif countBonus == 1:
				board_height -= 128
				board_height2 -= 128
			elif countBonus == 2:
				board_height -= 95
				board_height2 -= 95
			elif countBonus == 3:
				board_height -= 63
				board_height2 -= 63
			elif countBonus == 4:
				board_height -= 31
				board_height2 -= 31

			self.Board.SetSize(board_width, board_height)
			self.BonusBackground.SetSize(board_width2, board_height2)

		else:
			return

		self.ItemsSlots.SetItemSlot(0, player.GetItemIndex(itemPositon), 0)
		self.ItemsSlots.SetItemSlot(1, player.GetItemIndex(changerPosition), player.GetItemCount(changerPosition))

		self.ItemPosition = itemPositon
		self.ChangerPosition = changerPosition

		self.ChangersCount = player.GetItemCount(self.ChangerPosition)
		self.Open()

	def __GetBonusName(self, affectType, affectValue):
		if 0 == affectType:
			return None

		if 0 == affectValue:
			return None

		try:
			return self.ItemToolTip.AFFECT_DICT[affectType](affectValue)

		except TypeError:
			pass
		except KeyError:
			pass

	def ChangeBonus(self):
		if self.ChangerPosition == None or self.ItemPosition == None:
			return

		if (player.GetItemAttribute(self.ItemPosition, 0)[0] == item.APPLY_NORMAL_HIT_DAMAGE_BONUS and player.GetItemAttribute(self.ItemPosition, 0)[1] >= 30):
			self.ChangeBonusQuestion()
		else:
			self.DoChangeBonus()

	def DoChangeBonus(self):
		self.ChangersCount -= 1
		net.SendItemUseToItemPacket(self.ChangerPosition, self.ItemPosition)

		if player.GetItemIndex(self.ChangerPosition) != 0:
			self.ItemsSlots.SetItemSlot(1, player.GetItemIndex(self.ChangerPosition), self.ChangersCount)
		else:
			self.ItemsSlots.SetItemSlot(1, 0, 0)

		if self.ChangersCount <= 0:
			self.Close()
			return

		self.OnCloseQuestionDialog()

	def ChangeBonusQuestion(self):
		acceptQuestionDialog = uiCommon.QuestionDialog()
		acceptQuestionDialog.SetText(uiScriptLocale.BONUS_CHANGER_QUESTION)
		acceptQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.DoChangeBonus())
		acceptQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.OnCloseQuestionDialog())
		acceptQuestionDialog.Open()
		self.acceptQuestionDialog = acceptQuestionDialog

	def OnCloseQuestionDialog(self):
		if self.acceptQuestionDialog:
			self.acceptQuestionDialog.Close()

		self.acceptQuestionDialog = None

	def OnUpdate(self):
		if constInfo.IS_BONUS_CHANGER:
			attrSlot = [player.GetItemAttribute(self.ItemPosition, i) for i in xrange(self.MAX_BONUSES)]
			for i in xrange(self.MAX_BONUSES):
				type = attrSlot[i][0]
				value = attrSlot[i][1]
				affectString = self.__GetBonusName(type, value)

				self.BonusName[i].SetText("") #Clear old bonuses.

				if affectString:
					self.BonusName[i].SetText(affectString)
		else:
			return

	def Destroy(self):
		self.Close()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def Close(self):
		if self.IsShow():
			self.ChangerPosition = None
			self.ItemPosition = None
			constInfo.IS_BONUS_CHANGER = FALSE
			self.Hide()

	def Open(self):
		constInfo.IS_BONUS_CHANGER = TRUE
		self.Show()
