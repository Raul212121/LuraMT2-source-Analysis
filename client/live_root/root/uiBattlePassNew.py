import ui
import battlepass
import item
import uiToolTip
import player
import grp
import uiCommon

from _weakref import proxy
SKILL_SLOT_ENABLE	= "d:/ymir work/ui/cw/battlepass/x.png"
ITEM_SPACE = 5

def ConvertDamage(damage):
	damage = damage / 1000000
	return "{}M".format(damage)

class RenderBoxItem(ui.Window):
	class Item(ui.Window):
		def __init__(self, itemIcon, itemName, size, itemVnum):
			ui.Window.__init__(self)
			self.SetWindowName("RenderBoxItem")
			self.baseX, self.baseY = 0, 0

			self.itemIcon = ui.MakeExpandedImageBox(self, itemIcon, 0, 0, "not_pick")
			self.itemName = ui.MakeTextLineNew(self, 45, 8, itemName)

			self.itemIcon.SetEvent(ui.__mem_func__(self.OverInItem), "MOUSE_OVER_IN", itemVnum)
			self.itemIcon.SetEvent(ui.__mem_func__(self.OverOutItem), "MOUSE_OVER_OUT")

			self.tooltipItem = uiToolTip.ItemToolTip()
			self.tooltipItem.Hide()
		def __del__(self):
			ui.Window.__del__(self)

			self.baseX, self.baseY = 0, 0

			self.itemIcon = None
			self.itemName = ""

			self.tooltipItem = None

		def OverInItem(self, eventType, rewardIndex):
			if self.tooltipItem:
				self.tooltipItem.ClearToolTip()
				self.tooltipItem.AddItemData(rewardIndex, metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)])
				self.tooltipItem.ShowToolTip()

		def OverOutItem(self):
			if self.tooltipItem:
				self.tooltipItem.HideToolTip()
		def SetBasePosition(self, x, y):
			self.baseX = x
			self.baseY = y

		def GetBasePosition(self):
			return (self.baseX, self.baseY)

		def Show(self):
			ui.Window.Show(self)

		def OnRender(self):
			xList, yList = self.parent.GetGlobalPosition()
			widthList, heightList = self.parent.GetWidth(), self.parent.GetHeight()	

			if self.itemName:
				xText, yText = self.itemName.GetGlobalPosition()
				wText, hText = self.itemName.GetTextSize()
				
				if yText < yList or (yText + hText > yList + self.parent.GetHeight()):
					self.itemName.Hide()
				else:
					self.itemName.Show()

			images = [self.itemIcon]
			for img in images:
				if img:			
					img.SetClipRect(xList, yList, xList + widthList, yList + heightList)
					
		def SetParent(self, parent):
			ui.Window.SetParent(self, parent)
			self.parent = proxy(parent)

	def __init__(self):
		ui.Window.__init__(self)
		self.SetWindowName("ListBoxMissions")
		self.itemList = []

		self.selectedMission = 0

	def __del__(self):
		ui.Window.__del__(self)

		self.itemList = []

		self.selectedMission = 0
		self.globalParent = None

	def SetGlobalParent(self, parent):
		self.globalParent = proxy(parent)

	def OnScroll(self, scrollPos):
		totalHeight = 0
		for itemH in self.itemList:
			totalHeight += itemH.GetHeight()

		totalHeight -= self.GetHeight()

		for i in xrange(len(self.itemList)):
			x, y = self.itemList[i].GetLocalPosition()
			xB, yB = self.itemList[i].GetBasePosition()
			setPos = yB - int(scrollPos * totalHeight)
			self.itemList[i].SetPosition(xB, setPos)

	def AppendWindow(self, itemHeight, itemIcon, itemName, itemVnum):
		item = self.Item(itemIcon, itemName, itemHeight, itemVnum)
		item.SetParent(self)
		item.SetSize(self.GetWidth(), itemHeight)

		if len(self.itemList) == 0:
			item.SetPosition(0, 0)
			item.SetBasePosition(0, 0)
		else:
			x, y = self.itemList[-1].GetLocalPosition()
			item.SetPosition(0, y + self.itemList[-1].GetHeight())
			item.SetBasePosition(0, y + self.itemList[-1].GetHeight())

		item.Show()
		self.itemList.append(item)

	def ClearRenderBox(self):
		for items in xrange(len(self.itemList)):
			self.itemList[items].Hide()
			self.itemList[items].Destroy()

		self.itemList = []

class RenderBox(ui.Window):
	class Item(ui.Window):
		def __init__(self, missionVnum):
			ui.Window.__init__(self)
			self.SetWindowName("RenderBox")
			self.bIsSelected = False
			self.missionVnum = missionVnum

			self.baseX, self.baseY = 0, 0

			self.imageBackground = ui.MakeExpandedImageBox(self, "d:/ymir work/ui/cw/battlepass/miniboard_normal.png", 0, 0, "not_pick")
			self.imageBackgroundLogo = ui.MakeExpandedImageBox(self.imageBackground, "d:/ymir work/ui/cw/battlepass/icons/{}.png".format(missionVnum + 1), 16, 16, "not_pick")
			self.imageBackgroundLogo.SetScale(0.60, 0.60)

			self.gaugeBackground = ui.MakeExpandedImageBox(self.imageBackground, "d:/ymir work/ui/cw/battlepass/bar.png", 46, 32, "not_pick")
			self.gaugeExpanded = ui.MakeExpandedImageBox(self.gaugeBackground, "d:/ymir work/ui/cw/battlepass/bar_full.png", 1, 1, "not_pick")
			self.gaugeExpanded.SetWindowName("gaugeFull")
			self.gaugeExpandedDone = ui.MakeExpandedImageBox(self.gaugeBackground, "d:/ymir work/ui/cw/battlepass/bar_full_done.png", 1, 1, "not_pick")
			self.gaugeExpandedDone.SetWindowName("gaugeFull")

			self.missionTitle = ui.MakeTextLineNew(self.imageBackground, 50, 8, "")

			self.missionInformation = ui.MakeTextLineNew(self.imageBackground, 50, 18, "")
			self.missionInformation.SetPackedFontColor(0xFF9C8B55)
			#self.missionInformation.SetOutline(True)

			self.rewardList = [[0, 0], [0, 0], [0, 0]]
			self.rewardImages = []
			self.rewardListCount = []

			self.tooltipItem = uiToolTip.ItemToolTip()
			self.tooltipItem.Hide()

			
			for x in xrange(3):
				(vnum, count) = battlepass.GetMissionReward(self.missionVnum, x)
				rewardImage = None
				if vnum > 0:
					item.SelectItem(vnum)
					icon = item.GetIconImageFileName()

					rewardImage = ui.MakeExpandedImageBox(self.imageBackground, icon, 179 + (41 * x), 11)

					self.rewardList[x] = [vnum, count]

					
					itemCount = ui.NumberLine()
					itemCount.SetParent(rewardImage)
					itemCount.SetHorizontalAlignRight()
					itemCount.SetPosition(32 - 5, 32 - 10)
					itemCount.SetNumber(str(count))
					itemCount.Show()
					self.rewardListCount.append(itemCount)			

				else:
					rewardImage = ui.MakeExpandedImageBox(self.imageBackground, SKILL_SLOT_ENABLE, 179 + (41 * x), 11)


				rewardImage.SetEvent(ui.__mem_func__(self.OverInItem), "MOUSE_OVER_IN", x)
				rewardImage.SetEvent(ui.__mem_func__(self.OverOutItem), "MOUSE_OVER_OUT")

				self.rewardImages.append(rewardImage)


		def __del__(self):
			ui.Window.__del__(self)
			self.bIsSelected = False
			self.missionVnum = 0

			self.baseX, self.baseY = 0, 0

			self.imageBackground = None
			self.imageBackgroundLogo = None
			self.gaugeBackground = None

			self.missionTitle = None
			self.missionInformation = None

			self.rewardList = [[0, 0], [0, 0], [0, 0]]
			self.rewardImages = []
			self.rewardListCount = []

			self.tooltipItem = None


		def OverInItem(self, eventType, rewardIndex):
			if self.tooltipItem:
				self.tooltipItem.ClearToolTip()
				if self.rewardList[rewardIndex][0]:
					self.tooltipItem.AddItemData(self.rewardList[rewardIndex][0], metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)])
					self.tooltipItem.ShowToolTip()

		def OverOutItem(self):
			if self.tooltipItem:
				self.tooltipItem.HideToolTip()

		def SetBasePosition(self, x, y):
			self.baseX = x
			self.baseY = y

		def GetBasePosition(self):
			return (self.baseX, self.baseY)

		def GetMissionData(self):
			return self.missionVnum

		def OnMouseLeftButtonUp(self):
			self.Select()

		def Select(self):
			self.bIsSelected = True
			self.parent.SetSelectedMission(self.missionVnum)
			self.imageBackground.LoadImage("d:/ymir work/ui/cw/battlepass/miniboard_over.png")

		def Deselect(self):
			self.bIsSelected = False
			self.imageBackground.LoadImage("d:/ymir work/ui/cw/battlepass/miniboard_normal.png")

		def IsCompleted(self):
			if self.percentActual >= self.percentTotal:
				return True

			return False

		def OverInItem(self, eventType, rewardIndex):
			if self.tooltipItem:
				self.tooltipItem.ClearToolTip()
				if self.rewardList[rewardIndex][0]:
					self.tooltipItem.AddItemData(self.rewardList[rewardIndex][0], metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)])
					self.tooltipItem.ShowToolTip()

		def OverOutItem(self):
			if self.tooltipItem:
				self.tooltipItem.HideToolTip()

		def SetMissionName(self, missionTitle):
			if self.missionTitle:
				self.missionTitle.SetText(missionTitle)

		def SetMissionInfo1(self, missionInfo):
			if self.missionInformation:
				self.missionInformation.SetText(missionInfo)

		def GetMissionInfo(self):
			return (self.missionInfo1, self.percentActual, self.percentTotal)

		def Show(self):
			ui.Window.Show(self)

		def SetParent(self, parent):
			ui.Window.SetParent(self, parent)
			self.parent = proxy(parent)

		def OnRender(self):
			xList, yList = self.parent.GetGlobalPosition()
			widthList, heightList = self.parent.GetWidth(), self.parent.GetHeight()	

			images = [self.imageBackground, self.imageBackgroundLogo, self.gaugeBackground, self.gaugeExpanded, self.gaugeExpandedDone]
			for img in images:
				if img:
					if img.GetWindowName() == "gaugeFull":
						if self.percentTotal == 0:
							self.percentTotal = 1
						img.SetClipRect(0.0, yList, -1.0 + float(self.percentActual) / float(self.percentTotal), yList + self.parent.GetHeight(), True)	
					else:				
						img.SetClipRect(xList, yList, xList + widthList, yList + heightList)

			for item in self.rewardImages:
				item.SetClipRect(xList, yList, xList + self.parent.GetWidth(), yList + self.parent.GetHeight())						
						
			if self.missionTitle:
				xText, yText = self.missionTitle.GetGlobalPosition()
				wText, hText = self.missionTitle.GetTextSize()
				
				if yText < yList or (yText + hText > yList + self.parent.GetHeight()):
					self.missionTitle.Hide()
				else:
					self.missionTitle.Show()   

			if self.missionInformation:
				xText, yText = self.missionInformation.GetGlobalPosition()
				wText, hText = self.missionInformation.GetTextSize()
				
				if yText < yList or (yText + hText > yList + self.parent.GetHeight()):
					self.missionInformation.Hide()
				else:
					self.missionInformation.Show()  

			for count in self.rewardListCount:
				xList, yList = self.parent.GetGlobalPosition()
				xText, yText = count.GetGlobalPosition()
				wText, hText = count.GetWidth(), 7
				
				if yText < yList or (yText + hText > yList + self.parent.GetHeight()):
					count.Hide()
				else:
					count.Show()				

		def UpdateMissionData(self):
			missionCount = self.missionVnum
			missionName = battlepass.GetMissionName(missionCount)
			missionMax = battlepass.GetMissionMax(missionCount)
			missionDesc = battlepass.GetMissionDesc(missionCount, 0)
			missionProgress = battlepass.GetMissionProgress(missionCount)
			if missionMax > 0:
				subIsFormat = battlepass.IsFormat(missionCount)
				if subIsFormat:
					subCount = battlepass.GetMissionMax(missionCount)
					maxData = min(missionProgress, subCount)

					self.missionInformation.SetText("{} : ( {} / {} )".format(missionDesc, missionProgress, subCount))
					if missionCount == 19: # Damage Mission
						self.missionInformation.SetText("{} : ( {} / {} )".format(missionDesc, ConvertDamage(missionProgress), ConvertDamage(subCount)))
					self.UpdateGauge(missionProgress, subCount)
					self.percentActual = missionProgress
					self.percentTotal = subCount					
				else:
					self.missionInformation.SetText("{}".format(missionDesc))
					self.UpdateGauge(missionProgress, 1)
					self.percentActual = missionProgress
					self.percentTotal = 1								

		def UpdateGauge(self, data, max):
			self.gaugeExpandedDone.Hide()
			if data >= max:
				data = max
				self.gaugeExpandedDone.Show()

			self.gaugeExpanded.SetPercentage(data, max)

	def __init__(self):
		ui.Window.__init__(self)
		self.SetWindowName("ListBoxMissions")
		self.itemList = []

		self.selectedMission = 0

	def __del__(self):
		ui.Window.__del__(self)

		self.itemList = []

		self.selectedMission = 0
		self.globalParent = None

	def SetSelectedMission(self, missionVnum):
		self.selectedMission = missionVnum

		for itemH in self.itemList:
			if itemH.GetMissionData() != self.selectedMission:
				itemH.Deselect()

		if self.globalParent:
			self.globalParent.SetBattlePassData(self.selectedMission)

	def GetSelectedMission(self):
		return self.selectedMission

	def SetMission(self, missionVnum):
		for item in self.itemList:
			if missionVnum == item.GetMissionData():
				item.Select()

	def HaveMission(self, missionVnum):
		for item in self.itemList:
			if missionVnum == item.GetMissionData():
				return True

		return False

	def SelectFirstMission(self):
		if len(self.itemList) > 0:
			self.itemList[0].Select()

	def SetGlobalParent(self, parent):
		self.globalParent = proxy(parent)

	def OnScroll(self, scrollPos):
		totalHeight = 0
		for itemH in self.itemList:
			totalHeight += itemH.GetHeight()

		totalHeight -= self.GetHeight()

		for i in xrange(len(self.itemList)):
			x, y = self.itemList[i].GetLocalPosition()
			xB, yB = self.itemList[i].GetBasePosition()
			setPos = yB - int(scrollPos * totalHeight)
			self.itemList[i].SetPosition(xB, setPos)

	def AppendWindow(self, itemHeight, missionVnum, missionName, missionInfo1):
		item = self.Item(missionVnum)
		item.SetParent(self)
		item.SetSize(self.GetWidth() - 3, itemHeight)
		item.SetMissionName(missionName)
		item.SetMissionInfo1(missionInfo1)
		if len(self.itemList) == 0:
			item.SetPosition(0, 0)
			item.SetBasePosition(0, 0)
		else:
			x, y = self.itemList[-1].GetLocalPosition()
			item.SetPosition(0, y + self.itemList[-1].GetHeight())
			item.SetBasePosition(0, y + self.itemList[-1].GetHeight())

		item.Show()
		self.itemList.append(item)

	def UpdateRenders(self):
		for items in xrange(len(self.itemList)):
			self.itemList[items].UpdateMissionData()

	def ClearRenderBox(self):
		for items in xrange(len(self.itemList)):
			self.itemList[items].Hide()
			self.itemList[items].Destroy()

		self.itemList = []
		self.selectedMission = 0

class BattlePassWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.data = {}

		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/battlepassnew.py")
		except:
			import exception
			exception.Abort("PetUpgradeWindow.LoadDialog.LoadScript")

		try:
			self.data = {}

			self.data["board"] = self.GetChild("board")

			self.data["missionWindow"] = self.GetChild("BorderMissions")
			#self.data["missionWindow"].SetInsideRender(True)

			self.data["BorderMissionReward"] = self.GetChild("BorderMissionReward")
			#self.data["BorderMissionReward"].SetInsideRender(True)

			self.data["scrollBar"] = self.GetChild("ButtonsScrollBar")
			self.data["scrollBarReward"] = self.GetChild("ButtonsScrollBarReward")

			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))



		except:
			import exception
			exception.Abort("PetUpgradeWindow.LoadDialog.BindObject")

		self.data["missionBox"] = RenderBox()
		self.data["missionBox"].SetParent(self.data["missionWindow"])
		self.data["missionBox"].SetGlobalParent(self)
		self.data["missionBox"].SetPosition(2, 2)
		self.data["missionBox"].SetSize(309, 312)
		self.data["missionBox"].Show()

		self.data["scrollBar"].SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.data["scrollBar"].SetMiddleBarSize(float(1.0 / 3))

		self.data["scrollBar"].middleImage.Hide()
		self.data["scrollBar"].middleBar.topScale.Hide()
		self.data["scrollBar"].middleBar.bottom.Hide()
		self.data["scrollBar"].middleBar.bottomScale.Hide()
		self.data["scrollBar"].middleBar.middle.Hide()

		self.data["scrollBar"].middleBar.top.LoadImage("d:/ymir work/ui/cw/battlepass/scrollbar_big.png")
		self.data["scrollBar"].SetPos(0)


		self.data["missionBoxReward"] = RenderBoxItem()
		self.data["missionBoxReward"].SetParent(self.data["BorderMissionReward"])
		self.data["missionBoxReward"].SetGlobalParent(self)
		self.data["missionBoxReward"].SetPosition(10, 30)
		self.data["missionBoxReward"].SetSize(130, 120)
		self.data["missionBoxReward"].Show()


		self.data["scrollBarReward"].SetScrollEvent(ui.__mem_func__(self.OnScrollReward))
		self.data["scrollBarReward"].SetMiddleBarSize(float(1.0 / 3))

		self.data["scrollBarReward"].middleImage.Hide()
		self.data["scrollBarReward"].middleBar.topScale.Hide()
		self.data["scrollBarReward"].middleBar.bottom.Hide()
		self.data["scrollBarReward"].middleBar.bottomScale.Hide()
		self.data["scrollBarReward"].middleBar.middle.Hide()

		self.data["scrollBarReward"].middleBar.top.LoadImage("d:/ymir work/ui/cw/battlepass/scrollbar_small.png")
		self.data["scrollBarReward"].SetPos(0)

		self.GetChild("bar").SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.GetChild("bar").Hide()

		self.data["dialog"] = uiCommon.PopupDialog()
		self.data["dialog"].SetText("Acest battlepass este blocat!")
		self.data["dialog"].SetAcceptEvent(self.OnClosePopup)
		self.data["dialog"].SetTop()
		self.data["dialog"].Hide()

		self.OnClickFree()
		self.SetCenterPosition()


	def OnClosePopup(self):
		self.data["dialog"].Hide()
		self.GetChild("bar").Hide()

	def OnClickFree(self, openFrombutton = False):
		self.GetChild("bar").Hide()
		isActive = True
		self.data["missionBox"].ClearRenderBox()
		for missionCount in xrange(0, battlepass.MISSION_FREE_END):
			isActive = battlepass.IsActive(missionCount)
			missionName = battlepass.GetMissionName(missionCount)
			missionMax = battlepass.GetMissionMax(missionCount)
			missionDesc = battlepass.GetMissionDesc(missionCount, 0)
			if missionMax > 0:
				subIsFormat = battlepass.IsFormat(missionCount)
				if subIsFormat:
					subCount = battlepass.GetMissionMax(missionCount)
					self.data["missionBox"].AppendWindow(53, missionCount, missionName, missionDesc.format(subCount))
				else:
					self.data["missionBox"].AppendWindow(53, missionCount, missionName, missionDesc)

		self.data["missionBox"].SelectFirstMission()
		self.data["scrollBar"].SetPos(0)
		self.data["missionBoxReward"].ClearRenderBox()

		if isActive == False and openFrombutton:
			self.GetChild("bar").Show()
			self.data["dialog"].Open()

		for x in xrange(battlepass.GetMissionRewardFinalSize(0)):
			(itemVnum, count) = battlepass.GetMissionRewardFinal(0, x)
			item.SelectItem(itemVnum)

			(_, size) = item.GetItemSize()
			icon = item.GetIconImageFileName()
			self.data["missionBoxReward"].AppendWindow(32 * size + ITEM_SPACE, icon, item.GetItemName(), itemVnum)
		self.UpdateBattlePass()



	def GetMissionSize(self):
		return 53

	def OnScroll(self):
		if self.data["missionBox"]:
			self.data["missionBox"].OnScroll(self.data["scrollBar"].GetPos())

	def OnScrollReward(self):
		if self.data["missionBoxReward"]:
			self.data["missionBoxReward"].OnScroll(self.data["scrollBarReward"].GetPos())

	def ClearWindow(self):
		pass

	def SetBattlePassData(self, id):
		for x in xrange(0, 4):
			self.GetChild("Desc{}".format(x)).SetText("")
			missionDesc = battlepass.GetMissionDesc(id, x + 1)
			if missionDesc != "":
				self.GetChild("Desc{}".format(x)).SetText(missionDesc)
		self.ClearWindow()

	def UpdateBattlePass(self):
		self.data["missionBox"].UpdateRenders()

	def Destroy(self):
		self.data["missionBox"].ClearRenderBox()
		self.data = {}
		self.Close()

	def Open(self):
		self.Show()
		self.SetCenterPosition()
		self.OnClickFree(True)

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True
