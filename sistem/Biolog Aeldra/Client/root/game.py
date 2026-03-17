# AFTER

		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
		
# ADD
		onPressKeyDict[app.DIK_F4]	= lambda : self.__BiologManagerOpen()

# AFTER

		#if constInfo.PVPMODE_ACCELKEY_ENABLE:
		#	onClickKeyDict[app.DIK_B] = lambda: self.ChangePKMode()

		self.onClickKeyDict=onClickKeyDict

# ADD

	def __BiologManagerOpen(self):
		import biologmgr
		biologmgr.SendPacket(net.BIOLOG_MANAGER_OPEN)

# ADD AT THE BOTTOM OF FILE

	if app.ENABLE_BIOLOG_SYSTEM:
		def BINARY_BiologManagerOpen(self):
			self.interface.ToggleBiologManager()
		
		def BINARY_BiologManagerUpdate(self):
			self.interface.BiologManagerUpdate()

		def BINARY_BiologManagerAlert(self):
			self.interface.BiologManager_Alert()

		def BINARY_BiologManagerClose(self):
			self.interface.BiologManagerClose()
