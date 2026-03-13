import ui
import grp
import net
import app
import wndMgr
import localeInfo

class Biolog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.bLoaded = False
		self.ToolTip = None
		self.bLoadedInfo = False
		self.time = 0
		self.listBonus = []
		self.ThiniListReward = {}
		self.ThiniListText = {}
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		if self.bLoadedInfo == False:
			net.SendChatPacket("/open_biolog")
		self.LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)

	def LoadWindow(self):
		if self.bLoaded == True:
			return

		self.bLoaded = True
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/Biolog.py")
		except:
			import exception
			exception.Abort("Biolog.LoadWindow.LoadObject")
		try:
			self.titleBar = self.GetChild("TitleBar")
			self.wndTextTitleBar = self.GetChild("TitleName")
			self.board = self.GetChild("board")
			self.btnDelivery = self.GetChild("DeliveryButton")
			self.wndTextRemain = self.GetChild("TextRemain")
			self.wndTextTimeLeft = self.GetChild("TimeLeft")
		except:
			import exception
			exception.Abort("Biolog.__LoadWindow.BindObject")

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.btnDelivery.SetEvent(ui.__mem_func__(self.Delivery))

		self.MakeThings()
		self.MakeRewardThini(0, 10, 54)
		self.MakeRewardThini(1, 165, 54)
		self.MakeRewardThini(2, 10, 85)
		self.MakeRewardThini(3, 165, 85)

	def OnUpdate(self):

		leftTime = 0
		if self.time > app.GetGlobalTimeStamp():
			leftTime = self.time - app.GetGlobalTimeStamp()
		self.wndTextTimeLeft.SetText("Timp ramas %s" % (localeInfo.SecondToDHMS(leftTime)))

	def AppendInfoTime(self, time):
		self.time = time

		leftTime = 0
		if self.time > app.GetGlobalTimeStamp():
			leftTime = self.time - app.GetGlobalTimeStamp()
		self.wndTextTimeLeft.SetText("Timp ramas %s" % (localeInfo.SecondToDHMS(leftTime)))

	def AppendInfo(self, iRewardVnum, iReqVnum, iNeedCount, iRemainCount, iReqLevel):
		self.listBonus = []
		self.ExRewardGrid.SetOverInItemEvent(lambda f=1: self.OnOverInItem(iRewardVnum))
		self.ExRewardGrid.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.ExRewardGrid.SetItemSlot(0, iRewardVnum, 1)

		self.cGrid.SetOverInItemEvent(lambda f=1: self.OnOverInItem(iReqVnum))
		self.cGrid.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.cGrid.SetItemSlot(0, iReqVnum, iNeedCount - iRemainCount)

		self.bLoadedInfo = True
		self.wndTextRemain.SetText(str(iNeedCount - iRemainCount) + " / " + str(iNeedCount))
		self.wndTextTitleBar.SetText("Misiune Biolog Lv. %d" % (iReqLevel))

	def AppendInfoBonus(self, value):
		self.listBonus.append(value)

	def DoneInfoBonus(self):
		self.ThiniListText[0].SetText(self.ToolTip.GetAffectString(self.listBonus[0], self.listBonus[1])) ## 1

		if self.listBonus[2] > 1: # 2
			self.ThiniListText[1].SetText(self.ToolTip.GetAffectString(self.listBonus[2], self.listBonus[3]))
			self.ThiniListText[1].Show()
		else:
			self.ThiniListText[1].Hide()

		if self.listBonus[4] > 1: # 3
			self.ThiniListText[2].SetText(self.ToolTip.GetAffectString(self.listBonus[4], self.listBonus[5]))
			self.ThiniListText[2].Show()
		else:
			self.ThiniListText[2].Hide()

		if self.listBonus[6] > 1: # 4
			self.ThiniListText[3].SetText(self.ToolTip.GetAffectString(self.listBonus[6], self.listBonus[7]))
			self.ThiniListText[3].Show()
		else:
			self.ThiniListText[3].Hide()

	def SetItemToolTip(self, tooltip):
		self.ToolTip = tooltip

	def Delivery(self):
		net.SendChatPacket("/delivery_biolog")

	def Close(self):
		if self.ToolTip:
			self.ToolTip.HideToolTip()
		self.Hide()

	def Destroy(self):
		self.ClearDictionary()

	def OnOverInItem(self, iVnum):
		if self.ToolTip:
			self.ToolTip.SetItemToolTip(iVnum)

	def OnOverOutItem(self):
		if self.ToolTip:
			self.ToolTip.HideToolTip()

	def MakeRewardThini(self, index, x, y):
		self.ThiniListReward[index] = ui.ThinBoard()
		self.ThiniListReward[index].SetParent(self.board)
		self.ThiniListReward[index].SetPosition(x, y)
		self.ThiniListReward[index].SetSize(150, 2)
		self.ThiniListReward[index].Show()

		self.ThiniListText[index] = ui.TextLine()
		self.ThiniListText[index].SetParent(self.ThiniListReward[index])
		self.ThiniListText[index].SetPackedFontColor(grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0))
		self.ThiniListText[index].SetPosition(0, 7)
		self.ThiniListText[index].SetWindowHorizontalAlignCenter()
		self.ThiniListText[index].SetHorizontalAlignCenter()
		self.ThiniListText[index].Show()

	def MakeThings(self):
		self.cGrid = ui.GridSlotWindow()
		self.cGrid.SetParent(self.board)
		self.cGrid.SetPosition(270, 157)
		self.cGrid.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.cGrid.ArrangeSlot(0, 1, 1, 32, 32, 0, 0)
		self.cGrid.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		self.cGrid.Show()

		self.ExRewardGrid = ui.GridSlotWindow()
		self.ExRewardGrid.SetParent(self.board)
		self.ExRewardGrid.SetPosition(27, 157)
		self.ExRewardGrid.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.ExRewardGrid.ArrangeSlot(0, 1, 1, 32, 32, 0, 0)
		self.ExRewardGrid.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		self.ExRewardGrid.Show()

	def OnPressEscapeKey(self):
		self.Close()
		return True
