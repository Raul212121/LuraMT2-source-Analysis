"""
interfacemodule.py

hinzufügen : 
"""

if app.ENABLE_BATTLE_PASS_SYSTEM:
	import uiBattlePass




"""
Suchen "class NewGoldChat(ui.Window):  /> def __init__(self):"

darunter 	
		if app.ENABLE_CAPTCHA_SYSTEM:
			self.wndCaptcha = None

hinzufügen : 
"""

		if app.ENABLE_BATTLE_PASS_SYSTEM:
			self.wndBattlePass = None
			self.wndBattlePassButton = None



"""
Suchen "def __MakeWindows(self):"

darunter 	
		if app.ENABLE_CAPTCHA_SYSTEM:
			self.wndCaptcha = uiCaptcha.CaptchaDialog()
			self.wndCaptcha.BindInterface(self)

hinzufügen : 
"""
		if app.ENABLE_BATTLE_PASS_SYSTEM:
			self.wndBattlePass = uiBattlePass.BattlePassWindow()
			self.wndBattlePassButton = uiBattlePass.BattlePassButton()
			self.wndBattlePassButton.BindInterface(self)



"""
Suchen "def MakeInterface(self):"

darunter 	
		if app.ENABLE_PRIVATE_SHOP_SEARCH_SYSTEM:
			self.wndPrivateShopSearch.SetItemToolTip(self.tooltipItem)
		self.wndCube.SetItemToolTip(self.tooltipItem)
		self.wndCubeResult.SetItemToolTip(self.tooltipItem)

hinzufügen : 
"""

		if app.ENABLE_BATTLE_PASS_SYSTEM:
			self.wndBattlePass.SetItemToolTip(self.tooltipItem)



"""
Suchen "def Close(self):"

darunter 	
		if app.EXTEND_DIALOG_INVENTORY:
			if self.dropInventoryExtended:
				self.dropInventoryExtended.Hide()
				self.dropInventoryExtended.Destroy()

hinzufügen : 
"""

		if app.ENABLE_BATTLE_PASS_SYSTEM:
			if self.wndBattlePass:
				self.wndBattlePass.Destroy()

			if self.wndBattlePassButton:
				self.wndBattlePassButton.Destroy()


"""
Suchen "def Close(self):"

darunter 	
		if app.ENABLE_PRIVATE_SHOP_SEARCH_SYSTEM:
			del self.wndPrivateShopSearch

hinzufügen : 
"""

		if app.ENABLE_BATTLE_PASS_SYSTEM:
			if self.wndBattlePass:
				del self.wndBattlePass

			if self.wndBattlePassButton:
				del self.wndBattlePassButton



"""
darunter 	
	def ShowMouseImage(self):
		self.wndTaskBar.ShowMouseImage()

	def HideMouseImage(self):
		self.wndTaskBar.HideMouseImage()

hinzufügen : 
"""

if app.ENABLE_BATTLE_PASS_SYSTEM:
		def OpenBattlePass(self):
			if False == player.IsObserverMode():
				if not self.wndBattlePass.IsShow():
					self.wndBattlePass.Open()
					self.wndBattlePassButton.CompleteLoading()
				else:
					self.wndBattlePass.Close()

		def AddBattlePassMission(self, missionType, missionInfo1, missionInfo2, missionInfo3):
			if self.wndBattlePass:
				self.wndBattlePass.AddMission(missionType, missionInfo1, missionInfo2, missionInfo3)

		def UpdateBattlePassMission(self, missionType, newProgress):
			if self.wndBattlePass:
				self.wndBattlePass.UpdateMission(missionType, newProgress)

		def AddBattlePassMissionReward(self, missionType, itemVnum, itemCount):
			if self.wndBattlePass:
				self.wndBattlePass.AddMissionReward(missionType, itemVnum, itemCount)

		def AddBattlePassReward(self, itemVnum, itemCount):
			if self.wndBattlePass:
				self.wndBattlePass.AddReward(itemVnum, itemCount)

		def AddBattlePassRanking(self, pos, playerName, finishTime):
			if self.wndBattlePass:
				self.wndBattlePass.AddRanking(pos, playerName, finishTime)

		def RefreshBattlePassRanking(self):
			if self.wndBattlePass:
				self.wndBattlePass.RefreshRanking()

		def OpenBattlePassRanking(self):
			if self.wndBattlePass:
				self.wndBattlePass.OpenRanking()




"""
Suchen "def __HideWindows(self):"

darunter 	
		if app.ENABLE_MAILBOX_SYSTEM:
			if self.wndMailBox:
				hideWindows += self.wndMailBox,

hinzufügen : 
"""

		if app.ENABLE_BATTLE_PASS_SYSTEM:
			if self.wndBattlePass and self.wndBattlePassButton:
				hideWindows += self.wndBattlePass,
				hideWindows += self.wndBattlePassButton,
