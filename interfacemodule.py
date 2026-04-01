#1.0 Add this import:
#BONUS CHANGER
import uiBonusChanger
#END OF BONUS CHANGER

#2.0 Search:
	def __MakeCubeResultWindow(self):
		self.wndCubeResult = uiCube.CubeResultWindow()
		self.wndCubeResult.LoadWindow()
		self.wndCubeResult.Hide()

#2.1 Add under:
	#BONUS CHANGER
	def __MakeChangerWindow(self):
		self.wndChangerWindow = uiBonusChanger.ChangerWindow()
		self.wndChangerWindow.LoadWindow()
		self.wndChangerWindow.Hide()
	#END OF BONUS CHANGER

#3.0 Search:
		self.__MakeCubeResultWindow()

#3.1 Add under:
		#BONUS CHANGER
		self.__MakeChangerWindow()
		#END OF BONUS CHANGER
		
#4.0 Search:
		if self.privateShopBuilder:
			self.privateShopBuilder.Destroy()
			
#4.1 Add under:
		#BONUS CHANGER
		if self.wndChangerWindow:
			self.wndChangerWindow.Destroy()
		#END OF BONUS CHANGER
		
			
#5.0 Search:
		del self.wndItemSelect
		
#5.1 Add under:
		#BONUS CHANGER
		del self.wndChangerWindow
		#END OF BONUS CHANGER
		
		
#6.0 Search:
	def RefreshInventory(self):
		self.wndTaskBar.RefreshQuickSlot()
		self.wndInventory.RefreshItemSlot()
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.RefreshItemSlot()

#6.1 Add under:
		#BONUS CHANGER
		if constInfo.IS_BONUS_CHANGER:
			self.UpdateBonusChanger()
		#END OF BONUS CHANGER
			
#7.0 Search:
	def DisappearPrivateShop(self, vid):

		if not self.privateShopAdvertisementBoardDict.has_key(vid):
			return

		del self.privateShopAdvertisementBoardDict[vid]
		uiPrivateShopBuilder.DeleteADBoard(vid)

#7.1 Add under:

	#BONUS CHANGER
	def UpdateBonusChanger(self):
		if self.wndChangerWindow:
			self.wndChangerWindow.OnUpdate()
	
	def AddToBonusChange(self, item1, item2):
		if self.wndChangerWindow:
			self.wndChangerWindow.AddItems(item1, item2)
	#END OF BONUS CHANGER
	