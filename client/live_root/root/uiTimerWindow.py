import ui
import app
import net
import localeInfo
import chat

DESCRIPTION = {
	0 : [ "d:/ymir work/ui/game/dungeon_list/catacomba.tga", "Catacomba Diavolului", 75, "Optional", "30 Min", 30319, None, None, None, None, None, None  ], #img, title, level, group request, cooldown, item, dungeon desc
	1 : [ "d:/ymir work/ui/game/dungeon_list/beran.tga", "Beran Setaou", 75, "Optional", "1 Ora", 30179, None, None, None, None, None, None  ],
	2 : [ "d:/ymir work/ui/game/dungeon_list/dt.tga", "Turnul Demonilor", 40, "Optional", "0 Min", None, None, None, None, None, None, None  ],
	3 : [ "d:/ymir work/ui/game/dungeon_list/alastor.tga", "Barlogul lui Alastor", 95, "Optional", "6 ore", None, None, None, None, None, None, None  ],
	4 : [ "d:/ymir work/ui/game/dungeon_list/razador.tga", "Purgatoriul Iadului", 95, "Optional", "1 Ora", 71173, None, None, None, None, None, None  ],
    5 : [ "d:/ymir work/ui/game/dungeon_list/nemere.tga", "Turnul lui Nemere", 95, "Optional", "1 Ora", 71174, None, None, None, None, None, None  ],
	6 : [ "d:/ymir work/ui/game/dungeon_list/baronesa.tga", "Barlogul Baronesei", 55, "Optional", "1 Ora", 30324, None, None, None, None, None, None  ],
    7 : [ "d:/ymir work/ui/game/dungeon_list/orc_malefic.tga", "Pestera Malefica", 40, "Optional", "6 ore", None, None, None, None, None, None, None  ],
	8 : [ "d:/ymir work/ui/game/dungeon_list/incoming.tga", "", "Necunoscut", "Necunoscut", "Necunoscut", None, None, None, None, None, None, None  ],
}


def load_dungeon_desc():
	for x in xrange(9):
		f = open("%s/dungeon_desc/%d.txt" % (app.GetLocalePath(), x), "r")
		lines = [line.rstrip('\n') for line in f]
		global DESCRIPTION
		DESCRIPTION[x][9] = lines


class TimerBoard(ui.ImageBox):
	def __init__(self, parent, index):
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.index = index
		self.parent = parent
		self.__Build()

		load_dungeon_desc()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def __Build(self):

		self.LoadImage("d:/ymir work/ui/game/dungeon_list/available.tga")

		self.Show()

		self.image = ui.MakeImageBox(self, ("d:/ymir work/ui/game/dungeon_list/%d.tga" % self.index), 3, 3)

		self.textLine = ui.MakeTextLine(self)
		self.textLine.SetPosition(46, -10)
		self.textLine.SetWindowHorizontalAlignLeft()
		self.textLine.SetHorizontalAlignLeft()
		self.textLine.SetText(DESCRIPTION[self.index][1])

		self.textLine2 = ui.MakeTextLine(self)
		self.textLine2.SetPosition(8, 0)
		self.textLine2.SetWindowHorizontalAlignRight()
		self.textLine2.SetHorizontalAlignRight()
		self.textLine2.SetText(localeInfo.QUEST_TIMER_AVAILABLE)

		self.textLine3 = ui.MakeTextLine(self)
		self.textLine3.SetPosition(46, 7)
		self.textLine3.SetWindowHorizontalAlignLeft()
		self.textLine3.SetHorizontalAlignLeft()
		self.textLine3.SetText("00:00:00")

		self.incoming = ui.MakeTextLine(self)
		self.incoming.SetPosition(150, 0)
		self.incoming.SetWindowHorizontalAlignLeft()
		self.incoming.SetHorizontalAlignLeft()
		self.incoming.SetText("In curand")

		self.endTime = 0

	def SetTimeLeft(self, time):
		self.endTime = app.GetGlobalTimeStamp() + time

	def UpdateTime(self, indexNum):
		if self.endTime - app.GetGlobalTimeStamp() > 0:
			m, s = divmod(self.endTime - app.GetGlobalTimeStamp(), 60)
			h, m = divmod(m, 60)
			self.textLine3.SetText("%02d:%02d:%02d" % (h, m, s))
			self.textLine2.SetText(localeInfo.QUEST_TIMER_LOCKED)
			self.incoming.SetText("")
			self.LoadImage("d:/ymir work/ui/game/dungeon_list/unavailable.tga")
		else:
			self.textLine3.SetText("00:00:00")
			self.textLine2.SetText(localeInfo.QUEST_TIMER_AVAILABLE)
			self.incoming.SetText("")
			self.LoadImage("d:/ymir work/ui/game/dungeon_list/available.tga")

		if indexNum > 7:
			self.textLine3.SetText("")
			self.textLine2.SetText("")
			self.incoming.SetText("In curand")
			self.LoadImage("d:/ymir work/ui/game/dungeon_list/unavailable.tga")

	def OnMouseLeftButtonDown(self):
		self.parent.SetDescription(self.index)

	def Destroy(self):
		self.image = None
		self.textLine = None
		self.textLine2 = None
		self.textLine3 = None


class TimerWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/timerwindow.py")
		except:
			import exception
			exception.Abort("TimerWindow.LoadWindow.LoadObject")

		try:
			self.titleBar = self.GetChild("TitleBar")
			self.itemSlot = self.GetChild("ItemSlot")
			self.teleport = self.GetChild("Button")
			self.listDesc = self.GetChild("ListDesc")
			self.scrollBar = self.GetChild("ScrollBar")
		except:
			import exception
			exception.Abort("TimerWindow.LoadWindow.BindObject")

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))

		self.listDesc.SetItemSize(225, 11)
		self.listDesc.SetScrollBar(self.scrollBar)

		self.teleport.SetEvent(ui.__mem_func__(self.Teleport))

		self.timerBoards = []
		for x in xrange(9):
			board = TimerBoard(self, x)
			board.SetPosition(23, 50 * (x + 1) - 7)
			self.timerBoards.append(board)

		self.tooltip = None

		self.image = ui.ImageBox()
		self.image.SetParent(self)
		self.image.SetPosition(342, 36)

		self.textLine = ui.MakeTextLine(self)
		self.textLine.SetPosition(342 - 178, 36 - 85 - 142)

		self.textLine2 = ui.MakeTextLine(self)
		self.textLine2.SetPosition(28, -167)
		self.textLine2.SetWindowHorizontalAlignRight()
		self.textLine2.SetHorizontalAlignRight()

		self.textLine3 = ui.MakeTextLine(self)
		self.textLine3.SetPosition(28, -150)
		self.textLine3.SetWindowHorizontalAlignRight()
		self.textLine3.SetHorizontalAlignRight()

		self.textLine4 = ui.MakeTextLine(self)
		self.textLine4.SetPosition(28, -133)
		self.textLine4.SetWindowHorizontalAlignRight()
		self.textLine4.SetHorizontalAlignRight()

		self.index = 0
		self.SetDescription(0) #default

	def SetDescription(self, index):
		self.index = index
		self.image.LoadImage(DESCRIPTION[index][0])
		self.textLine.SetText(DESCRIPTION[index][1])
		self.itemSlot.SetItemSlot(0, DESCRIPTION[index][5])
		self.image.Show()
		self.textLine2.SetText(str(DESCRIPTION[index][2]))
		self.textLine3.SetText(str(DESCRIPTION[index][3]))
		self.textLine4.SetText(str(DESCRIPTION[index][4]))

		self.__ClearList()
		for line in DESCRIPTION[index][9]:
			textLine = ui.TextLine()
			textLine.SetParent(self.listDesc)
			textLine.Show()
			textLine.SetText(line)
			self.listDesc.AppendItem(textLine)

	def __ClearList(self):
		for item in self.listDesc.itemList:
			item = None

		self.listDesc.RemoveAllItems()

	def SetTimeLeft(self, index, time):
		self.timerBoards[index].SetTimeLeft(time)

	def SetToolTip(self, tooltip):
		self.tooltip = tooltip
		self.tooltip.Hide()

	def __OnOverInItem(self, slotIndex):
		self.tooltip.SetItemToolTip(DESCRIPTION[self.index][5])

	def __OnOverOutItem(self):
		self.tooltip.HideToolTip()

	def Teleport(self):

		if self.index >= 8:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[Informatie] - Aceasta temnita nu este disponibila momentan")
			return
		else:
			net.SendChatPacket("/timer_teleport %d" % self.index)


	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def OnUpdate(self):
		for x in xrange(9):
			self.timerBoards[x].UpdateTime(x)

	def OnScrollWheel(self, len):
		if len >= 0:
			self.scrollBar.OnUp()
		else:
			self.scrollBar.OnDown()
		return True

	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.scrollBar.OnUp()
		else:
			self.scrollBar.OnDown()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Destroy(self):
		self.ClearDictionary()
		self.image = None
		self.textLine = None
		self.textLine2 = None
		self.textLine3 = None
		self.textLine4 = None
		self.titleBar = None
		self.itemSlot = None
		self.teleport = None
		self.listDesc = None
		self.scrollBar = None
		for t in self.timerBoards:
			t.Destroy()
			t = None
		del self.timerBoards[:]
