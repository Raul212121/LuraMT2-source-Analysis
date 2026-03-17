import ui
import wndMgr
import net
import biologmgr

import dbg
import item

import localeInfo
import app

import player

class BiologManager(ui.ScriptWindow):
	BIOLOG_ADDITIONAL_ITEMS = (71035, 172001)

	TEXT_OBJECTS = {}
	CHECKBOX_OBJECTS = {}

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.__Initialize()

	def __Initialize(self):
		self.__LoadWindow()
		self.ToolTip = None
		TEXT_OBJECTS = {}
		CHECKBOX_OBJECTS = {}

	def __LoadWindow(self):
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "uiscript/BiologManagerWindow.py")

		except KeyError, msg:
			dbg.TraceError("BiologManager #1")

		try:
			self.__BindObjects()

		except KeyError, msg:
			dbg.TraceError("BiologManager #2 - %s" % str(msg))

		try:
			self.__BindEvents()
		
		except KeyError, msg:
			dbg.TraceError("BiologManager #3 - %s" % str(msg))
	
	def __BindObjects(self):
		GetObject = self.GetChild

		self.TEXT_OBJECTS["BiologLevelinfo"] = [GetObject("BiologRequiredLevel"), 0]
		self.TEXT_OBJECTS["BiologItemInfo"] = [GetObject("BiologItemInfo"), 0]
		self.TEXT_OBJECTS["BiologCooldownInfo"] = [GetObject("BiologCooldownInfo"), 0]
		self.TEXT_OBJECTS["BiologRewardData"] = [GetObject("BiologRewardData"), 0]
		
		self.CHECKBOX_OBJECTS["AdditionalCheckboxes"] = [GetObject("AdditionalCheckbox_%d" % (i)) for i in xrange(2)]
		self.CHECKBOX_OBJECTS["CheckBoxReminder"] = GetObject("CheckBoxReminder")

		self.main = {
			"board" : GetObject("BiologBoard"),
			"item_required" : GetObject("BiologRequiredItem"),

			"additional_items" : [GetObject("AdditionalItem_%d" % (i)) for i in xrange(2)],

			"biolog_submit" : GetObject("SubmitButton"),
		}

	def __BindEvents(self):
		GetObject = self.GetChild
		wnd = self.main

		wnd["board"].SetCloseEvent(ui.__mem_func__(self.Close))

		wnd["additional_items"][0].SetItemSlot(0, self.BIOLOG_ADDITIONAL_ITEMS[0], 0)
		wnd["additional_items"][1].SetItemSlot(0, self.BIOLOG_ADDITIONAL_ITEMS[1], 0)

		for i in xrange(2):
			wnd["additional_items"][i].SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
			wnd["additional_items"][i].SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

		self.CHECKBOX_OBJECTS["CheckBoxReminder"].SetEvent(self.__selectCooldownCheckBox)

		wnd["biolog_submit"].SetEvent(self.__submitPacket)

	def Open(self):
		self.RecvUpdate()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def RecvUpdate(self):
		wnd = self.main

		biologLevel = biologmgr.GetInfoLevel()

		data = localeInfo.BIOLOG_MANAGER_REQUIRED_LEVEL + " |cFF{}(Lv.{}) ".format("05E310" if player.GetStatus(player.LEVEL) >= biologLevel else "E30505", biologLevel)

		self.UpdateElement("BiologLevelinfo", data)

		biologItem = biologmgr.GetInfoItem()
		biologGiven, biologItemRequired = biologmgr.GetInfoCount()

		item.SelectItem(biologItem)

		data = localeInfo.BIOLOG_MANAGER_REQUIRED_ITEM_TITLE + " {} ({}/{})".format(item.GetItemName(), biologGiven, biologItemRequired)

		wnd["item_required"].SetItemSlot(0, biologItem, 0)
		wnd["item_required"].SetOverInItemEvent(lambda slotNumber, iVnum = biologItem: self.OnOverInRequiredItem(slotNumber, iVnum))
		wnd["item_required"].SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

		self.UpdateElement("BiologItemInfo", data)

		GCooldown, Cooldown = biologmgr.GetInfoCooldown()
		self.UpdateElement("BiologCooldownInfo", app.GetTime() + Cooldown)

		biologReminder = biologmgr.GetInfoReminder()
		self.CHECKBOX_OBJECTS["CheckBoxReminder"].SetChecked(True if biologReminder else False)

		rType, rValue = biologmgr.GetInfoReward()

		if rType != 0 and rValue != 0:
			tData = self.ToolTip.GetAffectString(rType, rValue)
			if tData:
				self.UpdateElement("BiologRewardData", tData)

	def UpdateElement(self, key, value):
		templ_tab = {"BiologLevelinfo" : "%s", "BiologItemInfo" : "%s", "BiologCooldownInfo" : "Wait: %s", "BiologRewardData" : "%s"}
		if key == "BiologCooldownInfo":
			if value > app.GetTime():
				self.TEXT_OBJECTS["BiologCooldownInfo"][1] = value
				self.TEXT_OBJECTS["BiologCooldownInfo"][0].SetText(templ_tab[key] % localeInfo.SecondToHMS(self.TEXT_OBJECTS["BiologCooldownInfo"][1] - app.GetTime()))
			else:
				self.TEXT_OBJECTS["BiologCooldownInfo"][0].SetText(localeInfo.BIOLOG_MANAGER_TIME_TEXT)
		else:
			if key in self.TEXT_OBJECTS:
				self.TEXT_OBJECTS[key][0].SetText(templ_tab[key] % value)
				self.TEXT_OBJECTS[key][1] = value

	def __selectCooldownCheckBox(self):
		wnd = self.CHECKBOX_OBJECTS["CheckBoxReminder"]
		biologmgr.SendPacketReminder(wnd.IsChecked())

	def __submitPacket(self):
		wnd = self.CHECKBOX_OBJECTS["AdditionalCheckboxes"]
		biologmgr.SendPacketItem(wnd[0].IsChecked(), wnd[1].IsChecked())

	def SetItemToolTip(self, tooltip):
		self.ToolTip = tooltip

	def OnOverInItem(self, pos):
		item = self.BIOLOG_ADDITIONAL_ITEMS[pos]
		if self.ToolTip:
			self.ToolTip.ClearToolTip()
			self.ToolTip.AddItemData(item, 0)

	def OnOverInRequiredItem(self, slotNumber, iVnum):
		if self.ToolTip:
			self.ToolTip.ClearToolTip()
			self.ToolTip.AddItemData(iVnum, 0)

	def OnOverOutItem(self):
		if self.ToolTip:
			self.ToolTip.HideToolTip()

	def Close(self):
		if self.ToolTip:
			self.ToolTip.HideToolTip()
		self.Hide()
	
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		if self.TEXT_OBJECTS["BiologCooldownInfo"][1] >= app.GetTime():
			self.TEXT_OBJECTS["BiologCooldownInfo"][0].SetText(localeInfo.BIOLOG_MANAGER_TIME_WAIT + localeInfo.SecondToHMS(self.TEXT_OBJECTS["BiologCooldownInfo"][1] - app.GetTime()))
		else:
			self.TEXT_OBJECTS["BiologCooldownInfo"][0].SetText(localeInfo.BIOLOG_MANAGER_TIME_TEXT)

class BiologManager_Alert(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.endTime = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def	Destroy(self):
		self.ClearDictionary()
		self.ReasonText = None
		self.StartTimeText = None
		self.endTime = 0

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/BiologManagerAlert.py")
		except:
			import exception
			exception.Abort("Maintenance_Alert.__LoadWindow.LoadObject")

		try:
			self.ReasonText = self.GetChild("Reason_Text")
			self.StartTimeText = self.GetChild("Start_Time_Text")
		except:
			import exception
			exception.Abort("Maintenance_Alert.__LoadWindow.BindObject")

		self.Hide()

	def	RecvUpdate(self, tTime):
		self.ReasonText.SetText(localeInfo.BIOLOG_MANAGER_TITLE)
		self.StartTimeText.SetText(localeInfo.BIOLOG_MANAGER_ALERT)

		self.SetTop()
		self.Show()

		self.endTime = app.GetTime() + tTime

	def	Close(self):
		self.Hide()

	def	Open(self):
		self.SetTop()
		self.Show()

	def	UpdateWindow(self):
		if self.IsShow():
			self.Hide()
		else:
			self.Show()
	
	def OnUpdate(self):
		leftTime = max(0, self.endTime - app.GetTime())
		if leftTime < 0.5:
			self.Close()
