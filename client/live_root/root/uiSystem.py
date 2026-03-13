import net
import app
import ui

import uiSystemOption
import uiGameOption
import localeInfo
import uiToolTip
if app.ENABLE_MOVE_CHANNEL:
	import chat

SYSTEM_MENU_FOR_PORTAL = False

###################################################################################################
## System
class SystemDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()

	def __Initialize(self):
		self.systemOptionDlg = None
		self.gameOptionDlg = None
		if app.ENABLE_MOVE_CHANNEL:
			self.moveChannelDlg = None


	def LoadDialog(self):
		if SYSTEM_MENU_FOR_PORTAL:
			self.__LoadSystemMenu_ForPortal()
		else:
			self.__LoadSystemMenu_Default()

	def __LoadSystemMenu_Default(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog.py")

		self.GetChild("system_option_button").SAFE_SetEvent(self.__ClickSystemOptionButton)
		self.GetChild("game_option_button").SAFE_SetEvent(self.__ClickGameOptionButton)
		self.GetChild("change_button").SAFE_SetEvent(self.__ClickChangeCharacterButton)
		self.GetChild("logout_button").SAFE_SetEvent(self.__ClickLogOutButton)
		self.GetChild("exit_button").SAFE_SetEvent(self.__ClickExitButton)
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)

		if app.ENABLE_MOVE_CHANNEL:
			self.GetChild("movechannel_button").SAFE_SetEvent(self.__ClickMoveChannelButton)


	def __LoadSystemMenu_ForPortal(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog_forportal.py")

		self.GetChild("system_option_button").SAFE_SetEvent(self.__ClickSystemOptionButton)
		self.GetChild("game_option_button").SAFE_SetEvent(self.__ClickGameOptionButton)
		self.GetChild("change_button").SAFE_SetEvent(self.__ClickChangeCharacterButton)
		self.GetChild("exit_button").SAFE_SetEvent(self.__ClickExitButton)
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)
		if app.ENABLE_MOVE_CHANNEL:
			self.GetChild("movechannel_button").SAFE_SetEvent(self.__ClickMoveChannelButton)


	def Destroy(self):
		self.ClearDictionary()

		if self.gameOptionDlg:
			self.gameOptionDlg.Destroy()

		if self.systemOptionDlg:
			self.systemOptionDlg.Destroy()

		self.__Initialize()

	def OpenDialog(self):
		self.Show()

	def __ClickChangeCharacterButton(self):
		self.Close()

		net.ExitGame()

	def __OnClosePopupDialog(self):
		self.popup = None

	def __ClickLogOutButton(self):
		if SYSTEM_MENU_FOR_PORTAL:
			if app.loggined:
				self.Close()
				net.ExitApplication()
			else:
				self.Close()
				net.LogOutGame()
		else:
			self.Close()
			net.LogOutGame()


	def __ClickExitButton(self):
		self.Close()
		app.Exit()

	def __ClickSystemOptionButton(self):
		self.Close()

		if not self.systemOptionDlg:
			self.systemOptionDlg = uiSystemOption.OptionDialog()

		self.systemOptionDlg.Show()

	def __ClickGameOptionButton(self):
		self.Close()

		if not self.gameOptionDlg:
			self.gameOptionDlg = uiGameOption.OptionDialog()

		self.gameOptionDlg.Show()


	def __ClickInGameShopButton(self):
		self.Close()
		net.SendChatPacket("/in_game_mall")

	def Close(self):
		self.Hide()
		return True

	def RefreshMobile(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.RefreshMobile()
		#self.optionDialog.RefreshMobile()

	def OnMobileAuthority(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnMobileAuthority()
		#self.optionDialog.OnMobileAuthority()

	def OnBlockMode(self, mode):
		uiGameOption.blockMode = mode
		if self.gameOptionDlg:
			self.gameOptionDlg.OnBlockMode(mode)
		#self.optionDialog.OnBlockMode(mode)

	def OnChangePKMode(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnChangePKMode()
		#self.optionDialog.OnChangePKMode()

	def OnPressExitKey(self):
		self.Close()
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	if app.ENABLE_MOVE_CHANNEL:
		def __ClickMoveChannelButton(self):
			if net.GetChannelNumber() == 99:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_CHANNEL_NOT_MOVE)
				return

			elif net.GetMapIndex() >= 10000:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_CHANNEL_NOT_MOVE)
				return

			if self.moveChannelDlg:
				self.moveChannelDlg.Show()
			else:
				moveChannelDlg = MoveChannelDialog()
				moveChannelDlg.Show()
				self.moveChannelDlg = moveChannelDlg

			self.Close()

if app.ENABLE_MOVE_CHANNEL:
	class MoveChannelDialog(ui.ScriptWindow):
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.__LoadDialog()
			self.IsShow = False
			self.MoveChannelBtnTooltip = None
			self.MoveChannelTooltip = None


		def __del__(self):
			ui.ScriptWindow.__del__(self)
			self.MoveChannelBtnTooltip = None
			self.MoveChannelTooltip = None

		def __LoadDialog(self):
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "UIScript/MoveChannelDialog.py")
			except:
				import exception
				exception.Abort("MoveChannelDialog.__LoadDialog")

			self.ParentBoard = self.GetChild("MoveChannelBoard")
			self.ChildBoard = self.GetChild("BlackBoard")
			self.GetChild("MoveChannelTitle").SetCloseEvent(ui.__mem_func__(self.Close))

			self.MoveChannelToolTipList = [localeInfo.MOVE_CHANNEL_TOOLTIP_LINE1,
			localeInfo.MOVE_CHANNEL_TOOLTIP_LINE2]

			self.ChannelList = []
			cnt = self.GetChannelCount()

			self.DlgWidht = 190
			self.BlackBoardHeight = 23*cnt + 5*(cnt-1) + 13
			self.DlgHeight = self.BlackBoardHeight + 75

			self.AcceptBtn = ui.MakeButton(self.ParentBoard, 13, self.DlgHeight - 33, "", "d:/ymir work/ui/public/", "acceptbutton00.sub", "acceptbutton01.sub", "acceptbutton02.sub")
			self.AcceptBtn.SetEvent(ui.__mem_func__(self.AcceptButton))
			self.CloseBtn = ui.MakeButton(self.ParentBoard, self.DlgWidht - 73, self.DlgHeight - 33, "", "d:/ymir work/ui/public/", "canclebutton00.sub", "canclebutton01.sub", "canclebutton02.sub")
			self.CloseBtn.SetEvent(ui.__mem_func__(self.Close))

			for i in xrange(cnt):
				btn = ui.MakeButton(self.ChildBoard, 8, 6 + i*28, "", "d:/ymir work/ui/game/myshop_deco/", "select_btn_01.sub", "select_btn_02.sub", "select_btn_03.sub")
				btn.SetText(self.GetChannelName(i+1))
				btn.SetEvent(ui.__mem_func__(self.__SelectChannel), i+1)
				self.ChannelList.append(btn)

			self.ParentBoard.SetSize(self.DlgWidht, self.DlgHeight)
			self.ChildBoard.SetSize(self.DlgWidht - 26, self.BlackBoardHeight)
			self.SetSize(self.DlgWidht, self.DlgHeight)

			self.UpdateRect()

			self.MoveChannelBtnTooltip = self.GetChild("MoveChannelBtnTooltip")
			self.MoveChannelTooltip = self.__CreateGameTypeToolTip(localeInfo.MOVE_CHANNEL_TOOLTIP_TITLE,self.MoveChannelToolTipList)
			self.MoveChannelTooltip.SetTop()
			self.MoveChannelBtnTooltip.SetToolTipWindow(self.MoveChannelTooltip)

		def __CreateGameTypeToolTip(self, title, descList):
			toolTip = uiToolTip.ToolTip()
			toolTip.SetTitle(title)
			toolTip.AppendSpace(3)

			for desc in descList:
				toolTip.AutoAppendTextLine(desc)

			toolTip.AlignHorizonalCenter()
			toolTip.SetTop()
			return toolTip

		def __SelectChannel(self, idx):
			self.ChangeChannelNumber = idx

			for btn in self.ChannelList:
				btn.SetUp()
				btn.Enable()

			self.ChannelList[idx-1].Down()
			self.ChannelList[idx-1].Disable()

		def AcceptButton(self):
			net.SendChatPacket("/channel %d" % self.ChangeChannelNumber)
			self.__SaveChannelInfo()
			self.StartChannelNumber = self.ChangeChannelNumber
			self.Close()

		def Show(self):
			ui.ScriptWindow.Show(self)

			self.StartChannelNumber = net.GetChannelNumber()
			self.__SelectChannel(self.StartChannelNumber)

			self.IsShow = True

		def Close(self):
			self.Hide()
			self.IsShow = False

		def OnPressEscapeKey(self):
			self.Close()
			return True

		def IsShowWindow(self):
			return self.IsShow

		def __SaveChannelInfo(self):
			loadRegionID, loadServerID, loadChannelID = self.__LoadChannelInfo()
			try:
				file = open("channel.inf", "w")
				file.write("%d %d %d" % (loadServerID, self.ChangeChannelNumber, loadRegionID))
			except:
				print "MoveChannelDialog.__SaveChannelInfo - SaveError"

		def __LoadChannelInfo(self):
			try:
				file = open("channel.inf")
				lines = file.readlines()

				if len(lines) > 0:
					tokens = lines[0].split()

					selServerID = int(tokens[0])
					selChannelID = int(tokens[1])

					if len(tokens) == 3:
						regionID = int(tokens[2])

					return regionID, selServerID, selChannelID
			except:
				print "MoveChannelDialog.__LoadChannelInfo - OpenError"
				return -1, -1, -1

		def GetChannelName(self, idx):
			return "CH %d" % idx

		def GetChannelCount(self):
			import serverInfo
			loadRegionID, loadServerID, loadChannelID = self.__LoadChannelInfo()
			channelDict = serverInfo.REGION_DICT[loadRegionID][loadServerID]["channel"]
			return len(channelDict)

		def GetChannelNumber(self):
			loadRegionID, loadServerID, loadChannelID = self.__LoadChannelInfo()
			return loadChannelID

if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import ui

	#wndMgr.SetOutlineFlag(True)

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create("METIN2 CLOSED BETA", systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()


	wnd = SystemDialog()
	wnd.LoadDialog()
	wnd.Show()

	app.Loop()

