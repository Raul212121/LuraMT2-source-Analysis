# ADD

if app.ENABLE_BIOLOG_SYSTEM:
	import uiBiologManager

# BEFORE

	def __del__(self):
		systemSetting.DestroyInterfaceHandler()
		event.SetInterfaceWindow(None)

# ADD

		if app.ENABLE_BIOLOG_SYSTEM:
			self.wndBiologManager = {}

# BEFORE

	def __MakeDialogs(self):
		self.dlgExchange = uiExchange.ExchangeDialog(self.wndInventory)
		self.dlgExchange.BindInterface(self)
		self.dlgExchange.LoadDialog()

# ADD

		if app.ENABLE_BIOLOG_SYSTEM:
			self.wndBiologManager["PANEL"] = uiBiologManager.BiologManager()
			self.wndBiologManager["ALERT"] = uiBiologManager.BiologManager_Alert()

# AFTER

		self.dlgShop.SetItemToolTip(self.tooltipItem)
		self.dlgExchange.SetItemToolTip(self.tooltipItem)
		self.privateShopBuilder.SetItemToolTip(self.tooltipItem)

# ADD

		if app.ENABLE_BIOLOG_SYSTEM:
			self.wndBiologManager["PANEL"].SetItemToolTip(self.tooltipItem)

# BEFORE

		for btn in self.questButtonList:
			btn.SetEvent(0)
		for btn in self.whisperButtonList:
			btn.SetEvent(0)

# ADD

		if app.ENABLE_BIOLOG_SYSTEM:
			if self.wndBiologManager:
				for wnd in self.wndBiologManager.values():
					wnd.Destroy()

# BEFORE

		self.questButtonList = []
		self.whisperButtonList = []
		self.whisperDialogDict = {}

# ADD

		if app.ENABLE_BIOLOG_SYSTEM:
			for wnd in self.wndBiologManager.values():
				del wnd

# BEFORE

	def ShowMouseImage(self):
		self.wndTaskBar.ShowMouseImage()

# ADD
		if app.ENABLE_BIOLOG_SYSTEM:
			if self.wndBiologManager:
				for wnd in self.wndBiologManager.values():
					wnd.Hide()

# BEFORE

if __name__ == "__main__":

# ADD

	if app.ENABLE_BIOLOG_SYSTEM:
		def ToggleBiologManager(self):
			if self.wndBiologManager["PANEL"].IsShow():
				self.wndBiologManager["PANEL"].Close()
			else:
				self.wndBiologManager["PANEL"].Open()

		def BiologManagerUpdate(self):
			self.wndBiologManager["PANEL"].RecvUpdate()

		def BiologManager_Alert(self):
			self.wndBiologManager["ALERT"].RecvUpdate(5)

		def BiologManagerClose(self):
			if self.wndBiologManager["PANEL"].IsShow():
				self.wndBiologManager["PANEL"].Close()