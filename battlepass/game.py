"""
game.py

Suchen "def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):"

darunter 	
		elif app.ENABLE_DS_SET and chr.NEW_AFFECT_DS_SET == type:
			self.interface.DragonSoulSetGrade(value)

hinzufügen : 
"""

		if app.ENABLE_BATTLE_PASS_SYSTEM:
			if type == chr.AFFECT_BATTLE_PASS:
				if self.interface:
					if self.interface.wndBattlePassButton:
						self.interface.wndBattlePassButton.ShowButton()
						self.interface.wndBattlePassButton.Show()

					if self.interface.wndBattlePass:
						self.interface.wndBattlePass.SetBattlePassInfo(value, duration)


"""
Suchen "def BINARY_NEW_RemoveAffect(self, type, pointIdx):"

darunter 	
		elif app.ENABLE_DS_SET and chr.NEW_AFFECT_DS_SET == type:
			self.interface.DragonSoulSetGrade(0)
			
hinzufügen : 
"""

		if app.ENABLE_BATTLE_PASS_SYSTEM:
			if type == chr.AFFECT_BATTLE_PASS:
				if self.interface and self.interface.wndBattlePassButton:
					self.interface.wndBattlePassButton.HideButton()
					self.interface.wndBattlePassButton.Hide()



"""
darunter 	
		hour = (app.GetGlobalTimeStamp() / 60) / 60 % 24
		for key, c_pszName in EnvironmentData.iteritems():
			if hour is key and app.IsExistFile(c_pszName):
				background.RegisterEnvironmentData(0, c_pszName)
				background.SetEnvironmentData(0)
	## END_OF_EVENTS

hinzufügen : 
"""

	if app.ENABLE_BATTLE_PASS_SYSTEM:
		def BINARY_BattlePassOpen(self):
			if self.interface:
				self.interface.OpenBattlePass()

		def BINARY_BattlePassAddMission(self, missionType, missionInfo1, missionInfo2, missionInfo3):
			if self.interface:
				self.interface.AddBattlePassMission(missionType, missionInfo1, missionInfo2, missionInfo3)

		def BINARY_BattlePassAddMissionReward(self, missionType, itemVnum, itemCount):
			if self.interface:
				self.interface.AddBattlePassMissionReward(missionType, itemVnum, itemCount)

		def BINARY_BattlePassUpdate(self, missionType, newProgress):
			if self.interface:
				self.interface.UpdateBattlePassMission(missionType, newProgress)

		def BINARY_BattlePassAddReward(self, itemVnum, itemCount):
			if self.interface:
				self.interface.AddBattlePassReward(itemVnum, itemCount)

		def BINARY_BattlePassAddRanking(self, pos, playerName, finishTime):
			if self.interface:
				self.interface.AddBattlePassRanking(pos, playerName, finishTime)

		def BINARY_BattlePassRefreshRanking(self):
			if self.interface:
				self.interface.RefreshBattlePassRanking()

		def BINARY_BattlePassOpenRanking(self):
			if self.interface:
				self.interface.OpenBattlePassRanking()