import grp
import app
import wndMgr
import snd
import net
import systemSetting
import localeInfo
import chr

import ui
import musicInfo
import playerSettingModule
import dbg

LEAVE_BUTTON_FOR_POTAL = False
NOT_NEED_DELETE_CODE = False
ENABLE_ENGNUM_DELETE_CODE = False

if localeInfo.IsJAPAN():
	NOT_NEED_DELETE_CODE = True
elif localeInfo.IsHONGKONG():
	ENABLE_ENGNUM_DELETE_CODE = True
elif localeInfo.IsNEWCIBN() or localeInfo.IsCIBN10():
	ENABLE_ENGNUM_DELETE_CODE = True
elif localeInfo.IsEUROPE():
	ENABLE_ENGNUM_DELETE_CODE = True

ROOT_PATH = "%s/ui/new/select/" % app.GetLocalePath()

###################################
##### CENTER CHARACTER RENDER #####
###################################
CAMERA_X = 10
width = wndMgr.GetScreenWidth()
height = wndMgr.GetScreenHeight()

if width <= 800 and height <= 600:
	CAMERA_X = -20
elif width <= 1024 and height <= 768:
	CAMERA_X = -5
elif width <= 1280 and height < 1024:
	CAMERA_X = 0

###################################

class SelectCharacterWindow(ui.Window):
	SLOT_COUNT = 4

	EMPIRE_NAME = {
		net.EMPIRE_A: localeInfo.EMPIRE_A,
		net.EMPIRE_B: localeInfo.EMPIRE_B,
		net.EMPIRE_C: localeInfo.EMPIRE_C
	}

	class CharacterRenderer(ui.Window):
		def OnRender(self):
			grp.ClearDepthBuffer()

			grp.SetGameRenderState()
			grp.PushState()
			grp.SetOmniLight()

			screenWidth = wndMgr.GetScreenWidth()
			screenHeight = wndMgr.GetScreenHeight()
			newScreenWidth = float(screenWidth - 270)
			newScreenHeight = float(screenHeight)

			grp.SetViewport(270.0 / screenWidth, 0.0, newScreenWidth / screenWidth, newScreenHeight / screenHeight)

			app.SetCenterPosition(CAMERA_X, 10.0, -10.0)
			app.SetCamera(1550.0, 15.0, 180.0, 95.0)
			grp.SetPerspective(10.0, newScreenWidth / newScreenHeight, 1000.0, 3000.0)

			(x, y) = app.GetCursorPosition()
			grp.SetCursorPosition(x, y)

			chr.Deform()
			chr.Render()

			grp.RestoreViewport()
			grp.PopState()
			grp.SetInterfaceRenderState()

	def __init__(self, stream):
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_SELECT, self)

		self.stream = stream
		self.slot = self.stream.GetCharacterSlot()

		self.openLoadingFlag = False
		self.startIndex = -1
		self.startReservingTime = 0
		self.dlgBoard = 0
		self.changeNameFlag = False
		self.nameInputBoard = None
		self.dlgQuestion = None
		self.sendChangeNamePacket = False

		self.startIndex = -1
		self.isLoad = 0

	def __del__(self):
		ui.Window.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_SELECT, 0)

	def Open(self):
		if not self.__LoadBoardDialog("uiscript/selectcharacterwindow.py"):
			dbg.TraceError("SelectCharacterWindow.Open - __LoadScript Error")
			return

		if not self.__LoadQuestionDialog("uiscript/questiondialog.py"):
			return

		playerSettingModule.LoadGameData("INIT")

		self.InitCharacterBoard()

		self.btnStart.Enable()
		self.btnDelete.Enable()
		self.btnExit.Enable()
		self.btnCreate.Enable()
		self.btnLeft.Enable()
		self.btnRight.Enable()

		self.dlgBoard.Show()
		self.SetWindowName("SelectCharacterWindow")
		self.Show()

		if self.slot >= 0:
			self.SelectSlot(self.slot)

		if musicInfo.selectMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/" + musicInfo.selectMusic)

		app.SetCenterPosition(0.0, 0.0, 0.0)
		app.SetCamera(1550.0, 15.0, 180.0, 95.0)

		self.isLoad = 1
		self.Refresh()

		if self.stream.isAutoSelect:
			chrSlot = self.stream.GetCharacterSlot()
			self.SelectSlot(chrSlot)
			self.StartGame()

		self.SetEmpire(net.GetEmpireID())

		self.OpenChangeNameDialog()
		self.CancelInputName()

		app.ShowCursor()

	def Close(self):
		if musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/" + musicInfo.selectMusic)

		self.stream.popupWindow.Close()

		if self.dlgBoard:
			self.dlgBoard.ClearDictionary()

		self.empireName = None
		self.characterGuild = None
		self.dlgBoard = None
		self.btnStart = None
		self.btnDelete = None
		self.btnExit = None
		self.backGround = None

		if self.dlgQuestion:
			self.dlgQuestion.ClearDictionary()
		self.dlgQuestion = None
		self.dlgQuestionText = None
		self.dlgQuestionAcceptButton = None
		self.dlgQuestionCancelButton = None
		self.privateInputBoard = None
		self.nameInputBoard = None

		chr.DeleteInstance(0)
		chr.DeleteInstance(1)
		chr.DeleteInstance(2)
		chr.DeleteInstance(3)

		self.Hide()
		self.KillFocus()

		app.HideCursor()

	def SetEmpire(self, id):
		self.empireName.SetText(localeInfo.SELECT_EMPIRE % self.EMPIRE_NAME.get(id, ""))

	def Refresh(self):
		if not self.isLoad:
			return

		# SLOT4
		indexArray = (3, 2, 1, 0)
		for index in indexArray:
			id = net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_ID)
			race = net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_RACE)
			form = net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_FORM)
			name = net.GetAccountCharacterSlotDataString(index, net.ACCOUNT_CHARACTER_SLOT_NAME)
			hair = net.GetAccountCharacterSlotDataInteger(index, net.ACCOUNT_CHARACTER_SLOT_HAIR)

			if id:
				self.MakeCharacter(index, id, name, race, form, hair)
				self.SelectSlot(index)

		self.SelectSlot(self.slot)

	def GetCharacterSlotID(self, slotIndex):
		return net.GetAccountCharacterSlotDataInteger(slotIndex, net.ACCOUNT_CHARACTER_SLOT_ID)

	def __LoadQuestionDialog(self, fileName):
		self.dlgQuestion = ui.ScriptWindow()

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self.dlgQuestion, fileName)
		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadQuestionDialog.LoadScript")

		try:
			GetObject = self.dlgQuestion.GetChild
			self.dlgQuestionText = GetObject("message")
			self.dlgQuestionAcceptButton = GetObject("accept")
			self.dlgQuestionCancelButton = GetObject("cancel")
		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadQuestionDialog.BindObject")

		self.dlgQuestionText.SetText(localeInfo.SELECT_DO_YOU_DELETE_REALLY)
		self.dlgQuestionAcceptButton.SetEvent(ui.__mem_func__(self.RequestDeleteCharacter))
		self.dlgQuestionCancelButton.SetEvent(ui.__mem_func__(self.dlgQuestion.Hide))
		return 1

	def __LoadBoardDialog(self, fileName):
		self.dlgBoard = ui.ScriptWindow()

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self.dlgBoard, fileName)
		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadBoardDialog.LoadScript")

		try:
			GetObject = self.dlgBoard.GetChild

			self.btnStart = GetObject("start_button")
			self.btnDelete = GetObject("delete_button")
			self.btnExit = GetObject("exit_button")
			self.btnCreate = GetObject("create_button")

			self.btnLeft = GetObject("left_button")
			self.btnRight = GetObject("right_button")

			self.CharacterName = GetObject("character_name_value")
			self.CharacterLevel = GetObject("character_level_value")
			self.empireName = GetObject("character_empire_name_value")
			self.characterGuild = GetObject("character_guild_value")

			self.backGround = GetObject("BackGround")

		except:
			import exception
			exception.Abort("SelectCharacterWindow.LoadBoardDialog.BindObject")

		imgFileNameDict = {
			0: ROOT_PATH + "background1.jpg",
			1: ROOT_PATH + "background2.jpg",
		}

		try:
			imgFileName = imgFileNameDict[app.GetRandom(0, len(imgFileNameDict) - 1)]
		except:
			self.backGround.Hide()

		self.btnStart.SetEvent(ui.__mem_func__(self.StartGame))
		self.btnExit.SetEvent(ui.__mem_func__(self.ExitSelect))
		self.btnCreate.SetEvent(ui.__mem_func__(self.CreateCharacter))

		self.btnLeft.SetEvent(ui.__mem_func__(self.DecreaseSlotIndex))
		self.btnRight.SetEvent(ui.__mem_func__(self.IncreaseSlotIndex))

		if NOT_NEED_DELETE_CODE:
			self.btnDelete.SetEvent(ui.__mem_func__(self.PopupDeleteQuestion))
		else:
			self.btnDelete.SetEvent(ui.__mem_func__(self.InputPrivateCode))

		self.chrRenderer = self.CharacterRenderer()
		self.chrRenderer.SetParent(self.backGround)
		self.chrRenderer.Show()

		return 1

	def MakeCharacter(self, index, id, name, race, form, hair):
		if 0 == id:
			return

		chr.CreateInstance(index)
		chr.SelectInstance(index)
		chr.SetVirtualID(index)
		chr.SetNameString(name)

		chr.SetRace(race)
		chr.SetArmor(form)
		chr.SetHair(hair)

		chr.Refresh()
		chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)

		chr.SetRotation(0.0)

	## Manage Character
	def StartGame(self):

		if self.sendChangeNamePacket:
			return

		if self.changeNameFlag:
			self.OpenChangeNameDialog()
			return

		if -1 != self.startIndex:
			return

		if musicInfo.selectMusic != "":
			snd.FadeLimitOutMusic("BGM/" + musicInfo.selectMusic, systemSetting.GetMusicVolume() * 0.05)

		self.btnStart.SetUp()
		self.btnDelete.SetUp()
		self.btnExit.SetUp()
		self.btnCreate.SetUp()
		self.btnLeft.SetUp()
		self.btnRight.SetUp()

		self.btnStart.Disable()
		self.btnDelete.Disable()
		self.btnExit.Disable()
		self.btnCreate.Disable()
		self.btnLeft.Disable()
		self.btnRight.Disable()
		self.dlgQuestion.Hide()

		self.stream.SetCharacterSlot(self.slot)

		self.startIndex = self.slot
		self.startReservingTime = app.GetTime()

		for i in xrange(self.SLOT_COUNT):

			if False == chr.HasInstance(i):
				continue

			chr.SelectInstance(i)

			if i == self.slot:
				self.slot = self.slot
				chr.PushOnceMotion(chr.MOTION_INTRO_SELECTED, 0.1)
				continue

			chr.PushOnceMotion(chr.MOTION_INTRO_NOT_SELECTED, 0.1)

	def OpenChangeNameDialog(self):
		import uiCommon
		nameInputBoard = uiCommon.InputDialogWithDescription()
		nameInputBoard.SetTitle(localeInfo.SELECT_CHANGE_NAME_TITLE)
		nameInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputName))
		nameInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputName))
		nameInputBoard.SetMaxLength(chr.PLAYER_NAME_MAX_LEN)
		nameInputBoard.SetBoardWidth(200)
		nameInputBoard.SetDescription(localeInfo.SELECT_INPUT_CHANGING_NAME)
		nameInputBoard.Open()
		nameInputBoard.slot = self.slot
		self.nameInputBoard = nameInputBoard

	def OnChangeName(self, id, name):
		self.SelectSlot(id)
		self.sendChangeNamePacket = False
		self.PopupMessage(localeInfo.SELECT_CHANGED_NAME)

	def AcceptInputName(self):
		changeName = self.nameInputBoard.GetText()
		if not changeName:
			return

		self.sendChangeNamePacket = True
		net.SendChangeNamePacket(self.nameInputBoard.slot, changeName)
		return self.CancelInputName()

	def CancelInputName(self):
		self.nameInputBoard.Close()
		self.nameInputBoard = None
		return True

	def OnCreateFailure(self, type):
		self.sendChangeNamePacket = False
		if 0 == type:
			self.PopupMessage(localeInfo.SELECT_CHANGE_FAILURE_STRANGE_NAME)
		elif 1 == type:
			self.PopupMessage(localeInfo.SELECT_CHANGE_FAILURE_ALREADY_EXIST_NAME)
		elif 100 == type:
			self.PopupMessage(localeInfo.SELECT_CHANGE_FAILURE_STRANGE_INDEX)

	def CreateCharacter(self):
		id = self.GetCharacterSlotID(self.slot)
		if 0 == id:
			self.stream.SetCharacterSlot(self.slot)

			EMPIRE_MODE = 1

			if EMPIRE_MODE:
				if self.__AreAllSlotEmpty():
					self.stream.SetReselectEmpirePhase()
				else:
					self.stream.SetCreateCharacterPhase()

			else:
				self.stream.SetCreateCharacterPhase()

	def __AreAllSlotEmpty(self):
		for iSlot in xrange(self.SLOT_COUNT):
			if 0 != net.GetAccountCharacterSlotDataInteger(iSlot, net.ACCOUNT_CHARACTER_SLOT_ID):
				return 0
		return 1

	def PopupDeleteQuestion(self):
		id = self.GetCharacterSlotID(self.slot)
		if 0 == id:
			return

		self.dlgQuestion.Show()
		self.dlgQuestion.SetTop()

	def RequestDeleteCharacter(self):
		self.dlgQuestion.Hide()

		id = self.GetCharacterSlotID(self.slot)
		if 0 == id:
			self.PopupMessage(localeInfo.SELECT_EMPTY_SLOT)
			return

		net.SendDestroyCharacterPacket(self.slot, "1234567")
		self.PopupMessage(localeInfo.SELECT_DELEING)

	def InputPrivateCode(self):

		import uiCommon
		privateInputBoard = uiCommon.InputDialogWithDescription()
		privateInputBoard.SetTitle(localeInfo.INPUT_PRIVATE_CODE_DIALOG_TITLE)
		privateInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputPrivateCode))
		privateInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputPrivateCode))

		if ENABLE_ENGNUM_DELETE_CODE:
			pass
		else:
			privateInputBoard.SetNumberMode()

		privateInputBoard.SetSecretMode()
		privateInputBoard.SetMaxLength(7)

		privateInputBoard.SetBoardWidth(250)
		privateInputBoard.SetDescription(localeInfo.INPUT_PRIVATE_CODE_DIALOG_DESCRIPTION)
		privateInputBoard.Open()
		self.privateInputBoard = privateInputBoard

	def AcceptInputPrivateCode(self):
		privateCode = self.privateInputBoard.GetText()
		if not privateCode:
			return

		id = self.GetCharacterSlotID(self.slot)
		if 0 == id:
			self.PopupMessage(localeInfo.SELECT_EMPTY_SLOT)
			return

		net.SendDestroyCharacterPacket(self.slot, privateCode)
		self.PopupMessage(localeInfo.SELECT_DELEING)

		self.CancelInputPrivateCode()
		return True

	def CancelInputPrivateCode(self):
		self.privateInputBoard = None
		return True

	def OnDeleteSuccess(self, slot):
		self.PopupMessage(localeInfo.SELECT_DELETED)
		self.DeleteCharacter(slot)

	def OnDeleteFailure(self):
		self.PopupMessage(localeInfo.SELECT_CAN_NOT_DELETE)

	def DeleteCharacter(self, index):
		chr.DeleteInstance(index)
		self.SelectSlot(self.slot)

	def ExitSelect(self):
		self.dlgQuestion.Hide()

		if LEAVE_BUTTON_FOR_POTAL:
			if app.loggined:
				self.stream.SetPhaseWindow(0)
			else:
				self.stream.setloginphase()
		else:
			self.stream.SetLoginPhase()

		self.Hide()

	def GetSlotIndex(self):
		return self.slot

	def DecreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() - 1 + self.SLOT_COUNT) % self.SLOT_COUNT
		self.SelectSlot(slotIndex)

	def IncreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() + 1) % self.SLOT_COUNT
		self.SelectSlot(slotIndex)

	def SelectSlot(self, index):

		if index < 0:
			return
		if index >= self.SLOT_COUNT:
			return

		self.slot = index

		for i in xrange(self.SLOT_COUNT):
			chr.SelectInstance(i)
			chr.Hide()

		id = net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_ID)
		if 0 != id:

			chr.SelectInstance(self.slot)
			chr.Show()

			self.btnStart.Show()
			self.btnDelete.Show()
			self.btnCreate.Hide()

			level = net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_LEVEL)
			race = net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_RACE)
			name = net.GetAccountCharacterSlotDataString(self.slot, net.ACCOUNT_CHARACTER_SLOT_NAME)
			guildName = net.GetAccountCharacterSlotDataString(self.slot, net.ACCOUNT_CHARACTER_SLOT_GUILD_NAME)
			self.changeNameFlag = net.GetAccountCharacterSlotDataInteger(self.slot,
																		 net.ACCOUNT_CHARACTER_SLOT_CHANGE_NAME_FLAG)

			self.CharacterName.SetText(name)
			self.CharacterLevel.SetText(localeInfo.SELECT_LEVEL % level)
			self.characterGuild.SetText(localeInfo.SELECT_GUILD % guildName if len(guildName) else localeInfo.SELECT_NOT_JOIN_GUILD)

		else:
			self.InitCharacterBoard()

	def InitCharacterBoard(self):
		try:
			self.btnStart.Hide()
			self.btnDelete.Hide()
			self.btnCreate.Show()

			self.CharacterName.SetText("")
			self.CharacterLevel.SetText("")
			self.characterGuild.SetText("")
		except:
			pass

	## Event
	def OnKeyDown(self, key):

		if 1 == key:
			self.ExitSelect()
		if 2 == key:
			self.SelectSlot(0)
		if 3 == key:
			self.SelectSlot(1)
		if 4 == key:
			self.SelectSlot(2)

		if 28 == key:

			id = net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_ID)
			if 0 == id:
				self.CreateCharacter()

			else:
				self.StartGame()

		if 203 == key:
			self.slot = (self.GetSlotIndex() - 1 + self.SLOT_COUNT) % self.SLOT_COUNT
			self.SelectSlot(self.slot)
		if 205 == key:
			self.slot = (self.GetSlotIndex() + 1) % self.SLOT_COUNT
			self.SelectSlot(self.slot)

		return True

	def OnUpdate(self):
		chr.Update()

		#######################################################
		if -1 != self.startIndex:

			if app.GetTime() - self.startReservingTime > 0.0:
				if False == self.openLoadingFlag:
					chrSlot = self.stream.GetCharacterSlot()
					net.DirectEnter(chrSlot)
					self.openLoadingFlag = True

					import chat
					chat.Clear()

	## Temporary
	#######################################################

	def EmptyFunc(self):
		pass

	def PopupMessage(self, msg, func=0):
		if not func:
			func = self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		self.ExitSelect()
		return True

