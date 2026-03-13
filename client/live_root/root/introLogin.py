import dbg
import app
import net
import ui
import ime
import snd
import wndMgr
import musicInfo
import systemSetting
import ServerStateChecker
import localeInfo
import constInfo
import ime
import base64

SERVER_IP = "81.180.202.241" # LIVE

def get_server_ip():
	import ConfigParser
	try:
		config = ConfigParser.ConfigParser()
		config.read('serverinfo.cfg')
		return config.get('SERVER_INFO', 'ip')
	except ConfigParser.NoSectionError:
		pass

	return SERVER_IP

SERVER_IP = get_server_ip()
SERVER_INFO = {
	"data" : {
		"channel1"	: [SERVER_IP, 30003],
		"channel2"	: [SERVER_IP, 30007],
		"channel3"	: [SERVER_IP, 30011],
		"channel4"	: [SERVER_IP, 30015],
		"auth"		: [SERVER_IP, 30001],
		"mark"		: [SERVER_IP, 30003],
	},

	"name" : "luramt2",
}

def base64_encode(string, key):
	encoded_chars = []
	for i in range(len(string)):
		key_c = key[i % len(key)]
		encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
		encoded_chars.append(encoded_c)
		encoded_string = "".join(encoded_chars)
	return base64.encodestring(encoded_string)

def base64_decode(string, key):
	decoded_chars = []
	string = base64.decodestring(string)
	for i in range(len(string)):
		key_c = key[i % len(key)]
		encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
		decoded_chars.append(encoded_c)
		decoded_string = "".join(decoded_chars)
	return decoded_string

# OLD STYLE
def parseAccountFile(fileName):
	try:
		file = open(fileName, "r")
		lines = file.readlines()
		for i in range(len(lines)):
			id, pwd, time = lines[i].replace("\n","").split("~~~")
			id = base64_decode(id, time)
			pwd = base64_decode(pwd, time)

			constInfo.set_reg("login%d" % i, base64_encode(id, constInfo.ACCOUNT_LOGIN_SECRET_KEY))
			constInfo.set_reg("password%d" % i, base64_encode(pwd, constInfo.ACCOUNT_LOGIN_SECRET_KEY))

		file.close()
	except:
		pass

	import os
	if os.path.exists(fileName):
		os.remove(fileName)

parseAccountFile("account_list.txt")

app.SetGuildMarkPath("mark")

class LoginWindow(ui.ScriptWindow):
	def __init__(self, stream):
		print ("NEW LOGIN WINDOW  ----------------------------------------------------------------------------")
		ui.ScriptWindow.__init__(self)

		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.stream=stream
		self.channelSlotList = []
		self.channelStatus = [0, 0, 0, 0]
		self.accountSlotList = []

	def __del__(self):
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)
		ui.ScriptWindow.__del__(self)
		print ("---------------------------------------------------------------------------- DELETE LOGIN WINDOW")

	def Open(self):
		ServerStateChecker.Create(self)

		for i in range(4):
			ch_hostname = SERVER_INFO["data"]["channel%d" % (i+1)][0]
			ch_port = SERVER_INFO["data"]["channel%d" % (i+1)][1]
			ServerStateChecker.AddChannel(i, ch_hostname, ch_port)

		ServerStateChecker.Request()

		print ("LOGIN WINDOW OPEN ----------------------------------------------------------------------------")

		self.loginFailureMsgDict={
			#"DEFAULT" : localeInfo.LOGIN_FAILURE_UNKNOWN,

			"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: localeInfo.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: localeInfo.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: localeInfo.LOGIN_FAILURE_WEB_BLOCK,
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: self.__DisconnectAndInputPassword,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")

		if not self.__LoadScript("uiscript/LoginWindow.py"):
			dbg.TraceError("LoginWindow.Open - __LoadScript Error")
			return

		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/"+musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		# pevent key "[" "]"
		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
			
		self.Show()
		self.__OnClickChannelButton(0)

		self.idEditLine.SetFocus()

		self.__RefreshSavedAccount()
		self.__RefreshChannelStatus()

		app.ShowCursor()

	def Close(self):
		# ServerStateChecker.Destroy(self)

		print ("---------------------------------------------------------------------------- CLOSE LOGIN WINDOW ")

		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)

		self.idEditLine = None
		self.pwdEditLine = None

		self.KillFocus()
		self.Hide()

		self.stream.popupWindow.Close()
		self.loginFailureFuncDict=None

		ime.ClearExceptKey()

		app.HideCursor()

	def __OnClickChannelButton(self, index):
		for channelSlot in self.channelSlotList:
			channelSlot["button"].SetUp()

		self.channelSlotList[index]["button"].Down()
		net.SetServerInfo("%s, Channel %i" % (SERVER_INFO["name"], index+1))

		ch_hostname = SERVER_INFO["data"]["channel%d" % (index+1)][0]
		ch_port = SERVER_INFO["data"]["channel%d" % (index+1)][1]
		auth_hostname = SERVER_INFO["data"]["auth"][0]
		auth_port = SERVER_INFO["data"]["auth"][1]

		self.stream.SetConnectInfo(ch_hostname, ch_port, auth_hostname, auth_port)

	def SetIDEditLineFocus(self):
		if self.idEditLine != None:
			self.idEditLine.SetFocus()

	def SetPasswordEditLineFocus(self):
		if localeInfo.IsEUROPE():
			if self.idEditLine != None:
				self.idEditLine.SetText("")
				self.idEditLine.SetFocus()

			if self.pwdEditLine != None:
				self.pwdEditLine.SetText("")
		else:
			if self.pwdEditLine != None:
				self.pwdEditLine.SetFocus()

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.SetPasswordEditLineFocus)

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")
		self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)

	def OnLoginFailure(self, error):

		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
			loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN  + error


		loginFailureFunc=self.loginFailureFuncDict.get(error, self.SetPasswordEditLineFocus)
		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __DisconnectAndInputPassword(self):

		self.SetPasswordEditLineFocus()
		net.Disconnect()

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			GetObject=self.GetChild
			self.idEditLine				= GetObject("ID_EditLine")
			self.idText			    	= GetObject("id_text")
			self.pwdEditLine			= GetObject("Password_EditLine")
			self.pwdText    			= GetObject("password_text")
			self.loginButton			= GetObject("login_button")
			self.accountSaveButton		= GetObject("account_save_button")
			self.loginExitButton		= GetObject("close_button")

			for i in range(4):
				channelSlot = {
					"button" : GetObject("channel%d_button" % (i + 1)),
					"status_off" : GetObject("channel%d_status_off" % (i + 1)),
					"status_on" : GetObject("channel%d_status_on" % (i + 1)),
				}

				channelSlot["button"].SetEvent(ui.__mem_func__(self.__OnClickChannelButton), i)
				self.channelSlotList.append(channelSlot)

			for i in range(8):
				accountSlot = {
					"text" : GetObject("account%d_text" % (i+1)),
					"load_button" : GetObject("account%d_load_button" % (i+1)),
					"delete_button" : GetObject("account%d_delete_button" % (i+1))
				}

				accountSlot["load_button"].SetEvent(ui.__mem_func__(self.__OnClickAccountConnectButton), i)
				accountSlot["delete_button"].SetEvent(ui.__mem_func__(self.__OnClickAccountDeleteButton), i)
				self.accountSlotList.append(accountSlot)

		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")


		self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))

		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))

		self.idEditLine.OnIMEUpdate = ui.__mem_func__(self.__OnIMEUpdateIDEditLine)
		self.pwdEditLine.OnIMEUpdate = ui.__mem_func__(self.__OnIMEUpdatePWDEditLine)

		self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.accountSaveButton.SetEvent(ui.__mem_func__(self.__OnClickAccountSaveButton))
		self.loginExitButton.SetEvent(ui.__mem_func__(self.__OnClickExitButton))

		return 1

	def Connect(self, id, pwd):
		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.SetPasswordEditLineFocus, localeInfo.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd)
		self.stream.Connect()

	def __OnClickExitButton(self):
		self.stream.SetPhaseWindow(0)

	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=None):
		if not func:
			func=self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return True

	def OnExit(self):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE, app.Exit, localeInfo.UI_OK)

	def OnUpdate(self):
		ServerStateChecker.Update()

	def EmptyFunc(self):
		pass

	def __OnIMEUpdateIDEditLine(self):
		ui.EditLine.OnIMEUpdate(self.idEditLine)

		if len(self.idEditLine.GetText()) > 0:
			self.idText.Hide()
		else:
			self.idText.Show()

	def __OnIMEUpdatePWDEditLine(self):
		ui.EditLine.OnIMEUpdate(self.pwdEditLine)

		if len(self.pwdEditLine.GetText()) > 0:
			self.pwdText.Hide()
		else:
			self.pwdText.Show()
		
	def __OnClickLoginButton(self, id=None, pwd=None):
		if id == None:
			id = self.__GetLogin()
		if pwd == None:
			pwd = self.__GetPassword()

		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return

		self.Connect(id, pwd)
		
	def __OnClickAccountConnectButton(self, index, by_key=False):
		id = constInfo.get_reg("login%d" % index, "")
		pwd = constInfo.get_reg("password%d" % index, "")
		if id == "" and pwd == "":
			if not by_key:
				self.PopupNotifyMessage(localeInfo.LOGIN_DATA_NOT_FOUND)
		else:
			id = base64_decode(id, constInfo.ACCOUNT_LOGIN_SECRET_KEY)
			pwd = base64_decode(pwd, constInfo.ACCOUNT_LOGIN_SECRET_KEY)
			self.__OnClickLoginButton(id, pwd)

	def __OnClickAccountDeleteButton(self, index):
		constInfo.set_reg("login%d" % index, "")
		constInfo.set_reg("password%d" % index, "")

		self.__RefreshSavedAccount()

		self.PopupNotifyMessage(localeInfo.LOGIN_DATA_DELETED)

	def __RefreshSavedAccount(self):
		for i, accountSlot in enumerate(self.accountSlotList):
			id = constInfo.get_reg("login%d" % i, "")

			if id == "":
				id = localeInfo.LOGIN_EMPTY_SLOT
			else:
				id = base64_decode(id, constInfo.ACCOUNT_LOGIN_SECRET_KEY)
			accountSlot["text"].SetText("F%d. %s" % (i + 1, id))

	def __GetLogin(self):
		return self.idEditLine.GetText() if self.idEditLine else ""

	def __GetPassword(self):
		return self.pwdEditLine.GetText() if self.pwdEditLine else ""

	def __OnClickAccountSaveButton(self):
		id = self.__GetLogin()
		pwd = self.__GetPassword()

		index = -1

		for i in range(8):
			login = constInfo.get_reg("login%d" % i, "")
			if login == "":
				index = i
				break

		if index == -1:
			self.PopupNotifyMessage(localeInfo.LOGIN_SAVE_FULL)
			return
		
		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return
			
		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return

		constInfo.set_reg("login%d" % index, base64_encode(id, constInfo.ACCOUNT_LOGIN_SECRET_KEY))
		constInfo.set_reg("password%d" % index, base64_encode(pwd, constInfo.ACCOUNT_LOGIN_SECRET_KEY))
		self.PopupNotifyMessage(localeInfo.LOGIN_DATA_SAVE)

		self.__RefreshSavedAccount()

	def NotifyChannelState(self, addrKey, state):
		self.channelStatus[addrKey] = state

		self.__RefreshChannelStatus()

	def __RefreshChannelStatus(self):
		for i, channelSlot in enumerate(self.channelSlotList):
			channelSlot["status_on"].Hide()
			if self.channelStatus[i] > 0:
				channelSlot["status_on"].Show()

	def OnKeyDown(self, key):
		if key in range(app.DIK_F1, app.DIK_F8):
			self.__OnClickAccountConnectButton(key - app.DIK_F1, True)
		return True
