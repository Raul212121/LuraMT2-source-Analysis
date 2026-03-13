import ui
import net

class InventoryMenuDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = False
		self.interface = None
		if False == self.isLoaded:
			self._LoadScript()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.interface = None

	def Destroy(self):
		self.Hide()

	def Close(self):
		self.Hide()

	def _LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, 'uiscript/inventorymenu.py')
		except:
			import exception
			exception.Abort('InventoryMenuDialog.LoadScriptFile')
		try:
			self._LoadUi()
		except:
			exception.Abort('InventoryMenuDialog.LoadUi')

		try:
			self._LoadEvents()
		except:
			exception.Abort('InventoryMenuDialog.LoadEvents')

		self.isLoaded = True

	def _LoadUi(self):
		self.elements = {
			'board' : self.GetChild("board"),
			'buttons': {
				'normal_storage_button' : self.GetChild("normal_storage"),
				'itemshop_storage' : self.GetChild("itemshop_storage"),
				'special_storage' : self.GetChild("special_storage")
			}
		}

	def _LoadEvents(self):
		self.elements['board'].SetCloseEvent(ui.__mem_func__(self.Close))
		self.elements['buttons']['normal_storage_button'].SetEvent(ui.__mem_func__(self.__OnClickNormalStorageButton))
		self.elements['buttons']['itemshop_storage'].SetEvent(ui.__mem_func__(self.__OnClickItemShopStorageButton))
		self.elements['buttons']['special_storage'].SetEvent(ui.__mem_func__(self.__OnClickSpecialStorageButton))

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def __OnClickNormalStorageButton(self):
		self.Close()
		print "click_storage_button"
		net.SendChatPacket("/click_safebox")

	def __OnClickItemShopStorageButton(self):
		self.Close()
		print "click_mall_button"
		net.SendChatPacket("/click_mall")

	def __OnClickSpecialStorageButton(self):
		self.Close()
		print "click_special_storage"
		net.SendChatPacket("/do_click_special_inv")

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
