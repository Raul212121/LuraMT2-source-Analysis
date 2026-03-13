import ui
import exception
import net
import player

rewardList = [
	{
		"id" : 0,
		"minutes" : 5000,
		"rewards" : [ [80007, 5], [71136, 1] ],
	},
	{
		"id" : 1,
		"minutes" : 10000,
		"rewards" : [ [80007, 10], [71128, 1] ],
	},
	{
		"id" : 2,
		"minutes" : 15000,
		"rewards" : [ [80007, 10], [80016, 1] ],
	},
	{
		"id" : 3,
		"minutes" : 20000,
		"rewards" : [ [80007, 10], [70015, 50] ],
	},
	{
		"id" : 4,
		"minutes" : 25000,
		"rewards" : [ [80007, 10], [50011, 200] ],
	},
	{
		"id" : 5,
		"minutes" : 30000,
		"rewards" : [ [80007, 25], [25424, 3], [25422, 3], [27987, 500] ],
	},
	{
		"id" : 6,
		"minutes" : 35000,
		"rewards" : [ [80007, 10], [70032, 5], [70033, 5], [70034, 5] ],
	},
	{
		"id" : 7,
		"minutes" : 40000,
		"rewards" : [ [80007, 15], [71084, 20000] ],
	},
	{
		"id" : 8,
		"minutes" : 45000,
		"rewards" : [ [80007, 15], [71124, 1] ],
	},
	{
		"id" : 9,
		"minutes" : 50000,
		"rewards" : [ [80007, 15], [80017, 1] ],
	},
	{
		"id" : 10,
		"minutes" : 75000,
		"rewards" : [ [25103, 1] ],
	},
	{
		"id" : 11,
		"minutes" : 90000,
		"rewards" : [ [80007, 20], [71148, 1], [80017, 1] ],
	},
	{
		"id" : 12,
		"minutes" : 100000,
		"rewards" : [ [80007, 25], [80017, 1], [80017, 1] , [80017, 1] ],
	},
	{
		"id" : 13,
		"minutes" : 125000,
		"rewards" : [ [80007, 30], [80018, 1] ],
	},
	{
		"id" : 14,
		"minutes" : 150000,
		"rewards" : [ [80007, 20], [25105, 1] ],
	},
	{
		"id" : 15,
		"minutes" : 175000,
		"rewards" : [ [80007, 50], [71148, 1], [71149, 1] ],
	},
	{
		"id" : 16,
		"minutes" : 200000,
		"rewards" : [ [80007, 50], [80018, 1], [53018, 1] ],
	}
]
class HourWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()


	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "uiscript/houreventwindow.py")

		except:
			exception.Abort("ItemCombionation.__LoadWindow.BindObject")

		self.GetChild("AcceptButton").SetEvent(ui.__mem_func__(self.SendCollect))


		self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Hide))

		self.SetCenterPosition()

	def Destroy(self):
		ui.ScriptWindow.Destroy(self)

		self.itemToolTip = None
		self.interface = None


	def SetToolTip(self, tooltip):
		self.itemToolTip = tooltip

	def BindInterface(self, interface):
		self.interface = interface

	def ClearWindow(self):
		if self.itemToolTip:
			self.itemToolTip.ClearToolTip()

	def OverInItem(self, slotIndex):
		if self.itemToolTip:
			self.itemToolTip.ClearToolTip()

	def OverOutItem(self):
		if self.itemToolTip:
			self.itemToolTip.HideToolTip()

	def SendCollect(self):
		net.SendChatPacket("/collect_hour_reward")

	def Open(self):
		self.SetCenterPosition()
		self.Show()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Close(self):
		self.ClearWindow()
		self.Hide()

	def OnUpdate(self):
		actualLevel = player.GetHoursEventStage()
		if actualLevel >= len(rewardList): #Stop if max ranked is reached.
			return

		for x in xrange(4):
			self.GetChild("Slot").ClearSlot(x)
			self.GetChild("Slot2").ClearSlot(x)
		self.GetChild("First").SetText("")
		self.GetChild("Second").SetText("")


		firstReward = rewardList[actualLevel]
		for x in xrange(len(firstReward["rewards"])):
			itemCount = 0
			if firstReward["rewards"][x][1] > 1:
				itemCount = firstReward["rewards"][x][1]
			self.GetChild("Slot").SetItemSlot(x, firstReward["rewards"][x][0], itemCount)

		self.GetChild("First").SetText("Target Minute : {}".format(firstReward["minutes"]))

		if actualLevel + 1 >= len(rewardList): #Don't show next reward if it's at last level.
			return

		secondReward = rewardList[actualLevel + 1]
		for x in xrange(len(secondReward["rewards"])):
			itemCount = 0
			if secondReward["rewards"][x][1] > 1:
				itemCount = secondReward["rewards"][x][1]
			self.GetChild("Slot2").SetItemSlot(x, secondReward["rewards"][x][0], itemCount)

		self.GetChild("Second").SetText("Urmatorul Target : {}".format(secondReward["minutes"]))

	def Close(self):
		self.ClearWindow()
		self.Hide()
