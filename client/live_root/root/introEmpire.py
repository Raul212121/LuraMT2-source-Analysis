import ui
import net
import wndMgr
import dbg
import app

class SelectEmpireWindow(ui.ScriptWindow):
	def __init__(self, stream):
		print "NEW EMPIRE WINDOW  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, self)

		self.stream=stream
		self.empireID = net.EMPIRE_A
		while self.empireID == net.EMPIRE_A:
			self.empireID=app.GetRandom(net.EMPIRE_B, net.EMPIRE_C)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, 0)
		print "---------------------------------------------------------------------------- DELETE EMPIRE WINDOW"

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE EMPIRE WINDOW"		

		self.ClearDictionary()
		self.selectButton = None
		self.exitButton = None

		self.KillFocus()
		self.Hide()

		app.HideCursor()

	def Open(self):
		print "OPEN EMPIRE WINDOW ----------------------------------------------------------------------------"

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("SelectEmpireWindow")
		self.Show()

		if not self.__LoadScript("uiscript/SelectEmpireWindow.py"):
			dbg.TraceError("SelectEmpireWindow.Open - __LoadScript Error")
			return

		self.OnSelectEmpire(self.empireID)
		app.ShowCursor()

	def OnSelectEmpire(self, arg):
		for key in self.empireButton.keys():
			if key == arg:
				self.empireButton[key].Down()
			else:
				self.empireButton[key].SetUp()

		self.empireID = arg

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)	
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.LoadObject")

		try:
			GetObject=self.GetChild
			self.selectButton		= GetObject("select_button")
			self.exitButton			= GetObject("exit_button")
			self.empireButton		= {
				net.EMPIRE_A: GetObject("empire_button_A"),
				net.EMPIRE_B: GetObject("empire_button_B"),
				net.EMPIRE_C: GetObject("empire_button_C")
			}
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.BindObject")					

		self.selectButton.SetEvent(ui.__mem_func__(self.ClickSelectButton))
		self.exitButton.SetEvent(ui.__mem_func__(self.ClickExitButton))

		for key, button in self.empireButton.items():
			button.SetEvent(ui.__mem_func__(self.OnSelectEmpire), key)

		return 1

	def ClickSelectButton(self):
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetSelectCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetLoginPhase()

	def OnPressEscapeKey(self):
		self.ClickExitButton()
		return True

	def OnPressExitKey(self):
		self.ClickExitButton()
		return True

class ReselectEmpireWindow(SelectEmpireWindow):
	def ClickSelectButton(self):
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetCreateCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetSelectCharacterPhase()
