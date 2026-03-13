import exception
import localeInfo
import net
import player
import ui

def lang(lang):
	return lang
Categories = {
	0 : {
		"name": "Killed Monsters",
		"icon": "mob",
		"type": "base",
	},
	1 : {
		"name": "Killed Metinstones",
		"icon": "stone",
		"type": "base",
	},
	2 : {
		"name": "Killed Bosses",
		"icon": "mobs",
		"type": "base",
	},
	3 : {
		"name": "Killed Players",
		"icon": "char",
		"type": "base",
	},
	4 : {
		"name": "Chests",
		"icon": "coin",
		"type": "base",
	},
}

class RankingCategory(ui.ListBoxEx.Item):
	Background = None
	Icon = None
	Title = None
	
	Index = None
	Category = None
	SelectEvent = None
	isSelected = False
	def __init__(self, index, category, event):
		ui.ListBoxEx.Item.__init__(self)
		
		self.Index = index
		self.Category = category
		self.SelectEvent = event
		
		self.Background = ui.ExpandedImageBox()
		self.Background.SetParent(self)
		self.Background.AddFlag("not_pick")
		self.Background.AddFlag("attach")
		self.Background.SetPosition(15, 10)
		self.Background.LoadImage("d:/ymir work/ui/cw/ranking/button_normal.tga")
		self.Background.Show()
		
		self.Title = ui.TextLine()
		self.Title.SetParent(self.Background)
		self.Title.SetHorizontalAlignLeft()
		self.Title.SetWindowHorizontalAlignLeft()
		self.Title.SetWindowVerticalAlignTop()
		self.Title.SetPosition(48, 5)
		self.Title.SetMultiLine()
		self.Title.SetLimitWidth(95)
		self.Title.SetPackedFontColor(0xFFadadad)
		self.Title.SetText(self.Category["name"])
		self.Title.Show()

		self.Icon = ui.ExpandedImageBox()
		self.Icon.SetParent(self.Background)
		self.Icon.AddFlag("not_pick")
		self.Icon.AddFlag("attach")
		self.Icon.SetPosition(5, -2)
		self.Icon.LoadImage("d:/ymir work/ui/cw/ranking/slots/{}.png".format(self.Category["icon"]))
		self.Icon.Show()
		
		self.SetSize(39, 161)

		self.isSelected = False
		
	def OnSelect(self):
		self.Background.LoadImage("d:/ymir work/ui/cw/ranking/button_over.tga")
		self.Title.SetPackedFontColor(0xFFffffff)
		if self.SelectEvent:
			self.SelectEvent(self.Index)

		self.isSelected = True
		
	def OnUnselect(self):
		self.Background.LoadImage("d:/ymir work/ui/cw/ranking/button_normal.tga")
		self.Title.SetPackedFontColor(0xFFadadad)

		self.isSelected = False
		
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
		self.Background = None
		self.Icon = None
		
		self.Index = None
		self.Category = None
		self.SelectEvent = None
		self.isSelected = False
		
	def OnSelectedRender(self):
		pass


class RankingLine(ui.ListBoxEx.Item):
	Rank = None
	Name = None
	Guild = None
	Empire = None
	Count = None
	Separator = None
	Background = None


	def GetImageRank(self, rank):
		image = "d:/ymir work/ui/cw/ranking/normal.tga"

		specialRankings = ["yellow", "silver", "bronze"]
		if rank in specialRankings:
			image = "d:/ymir work/ui/cw/ranking/{}.tga".format(specialRankings[rank])
		
		return image
	
	def __init__(self, rank, name, guild, empire, count):
		ui.ListBoxEx.Item.__init__(self)
		center = 1

		self.Background = ui.ExpandedImageBox()
		self.Background.SetParent(self)
		self.Background.AddFlag("not_pick")
		self.Background.AddFlag("attach")
		self.Background.SetPosition(0, 0)
		self.Background.LoadImage(self.GetImageRank(rank))
		self.Background.Show()

		self.Rank = ui.TextLine()
		self.Rank.SetParent(self.Background)
		self.Rank.SetHorizontalAlignLeft()
		self.Rank.SetWindowHorizontalAlignLeft()
		self.Rank.SetWindowVerticalAlignTop()
		self.Rank.SetPosition(15, center)
		self.Rank.SetFontName(lang("Tahoma:12"))
		self.Rank.SetPackedFontColor(self.GetRankColor(rank))
		self.Rank.SetText("{}".format(rank))
		self.Rank.Show()
		
		self.Name = ui.TextLine()
		self.Name.SetParent(self.Background)
		self.Name.SetHorizontalAlignLeft()
		self.Name.SetWindowHorizontalAlignLeft()
		self.Name.SetWindowVerticalAlignTop()
		self.Name.SetPosition(35, center)
		self.Name.SetFontName(lang("Tahoma:12"))
		self.Name.SetPackedFontColor(self.GetRankColor(rank))
		self.Name.SetText("{}".format(name))
		self.Name.Show()
		
		self.Guild = ui.TextLine()
		self.Guild.SetParent(self.Background)
		self.Guild.SetHorizontalAlignLeft()
		self.Guild.SetWindowHorizontalAlignLeft()
		self.Guild.SetWindowVerticalAlignTop()
		self.Guild.SetPosition(130, center)
		self.Guild.SetFontName(lang("Tahoma:12"))
		self.Guild.SetPackedFontColor(self.GetRankColor(rank))
		self.Guild.SetText("{}".format(guild))
		self.Guild.Show()
		
		self.Empire = ui.ExpandedImageBox()
		self.Empire.SetParent(self.Background)
		self.Empire.AddFlag("not_pick")
		self.Empire.AddFlag("attach")
		self.Empire.SetWindowHorizontalAlignLeft()
		self.Empire.SetWindowVerticalAlignTop()
		self.Empire.SetPosition(204, center)
		self.Empire.LoadImage("d:/ymir work/ui/cw/ranking/table/{}.png".format(empire))
		self.Empire.SetScale(0.8, 0.8)
		self.Empire.Show()
		
		self.Count = ui.TextLine()
		self.Count.SetParent(self.Background)
		self.Count.SetHorizontalAlignRight()
		self.Count.SetWindowHorizontalAlignLeft()
		self.Count.SetWindowVerticalAlignTop()
		self.Count.SetPosition(344, center)
		self.Count.SetFontName(lang("Tahoma:12"))
		self.Count.SetPackedFontColor(self.GetRankColor(rank))
		self.Count.SetText("{}".format(localeInfo.GetFormattedNumberString(count)))
		self.Count.Show()
		
		#self.Separator = ui.ExpandedImageBox()
		#self.Separator.SetParent(self)
		#self.Separator.AddFlag("not_pick")
		#self.Separator.AddFlag("attach")
		#self.Separator.SetWindowHorizontalAlignLeft()
		#self.Separator.SetPosition(0, 23)
		#self.Separator.LoadImage("d:/ymir work/ui/fallen/ranking/categories/boss_normal.png")
		#self.Separator.Show()
		
	
	def GetRankColor(self, rank):
		if rank == 1:
			return 0xFFf9bc45
		elif rank == 2:
			return 0xFFdbdbdb
		elif rank == 3:
			return 0xFFcb661b
		
		return 0xFFadadad
	
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
		self.Rank = None
		self.Name = None
		self.Guild = None
		self.Empire = None
		self.Count = None
		self.Separator = None
		self.Background = None
		
	def OnSelectedRender(self):
		pass

class RankingWindow(ui.ScriptWindow):
	CloseButton = None
	CategoryList = None
	ScrollBar = None
	RankingList = None
	PlayerRank = {}
	Gasit = False
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Gasit = False
		self.Initialize()
	
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.CloseButton = None
		self.CategoryList = None
		self.ScrollBar = None
		self.RankingList = None
		self.PlayerRank = {}
		
	def Initialize(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/rankingwindow.py")
			
			#self.CloseButton = self.GetChild("close")
			self.CategoryList = self.GetChild("category_list")
			self.ScrollBar = self.GetChild("category_scroll")
			self.RankingList = self.GetChild("rank_list")
			
			self.PlayerRank["rank"] = self.GetChild("rankPlayer")
			self.PlayerRank["name"] = self.GetChild("namePlayer")
			self.PlayerRank["guild"] = self.GetChild("guildPlayer")
			self.PlayerRank["empire"] = self.GetChild("empirePlayer")
			self.PlayerRank["count"] = self.GetChild("countPlayer")
			self.PlayerRank["count"].SetHorizontalAlignRight()
			self.PlayerRank["count"].SetWindowHorizontalAlignLeft()
			self.PlayerRank["count"].SetWindowVerticalAlignTop()
			self.GetChild("TitleBar").SetCloseEvent(self.Hide)

			
		except:
			exception.Abort("RankingWindow.Initialize.LoadScript")

		try:
			#self.CloseButton.SetEvent(ui.__mem_func__(self.Close))
			self.CategoryList.SetScrollBar(self.ScrollBar)

		except:
			exception.Abort("RankingWindow.Initialize.BindObject")

		self.SelectCategory(4)
	
	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def SelectCategory(self, category):
		net.RequestRanking(category)
	
	def ClearPlayerRanking(self):
		self.RankingList.RemoveAllItems()
		self.PlayerRank["rank"].SetText("-")
		self.PlayerRank["name"].SetText("-")
		self.PlayerRank["guild"].SetText("-")
		self.PlayerRank["empire"].LoadImage("d:/ymir work/ui/cw/ranking/table/1.png")
		self.PlayerRank["count"].SetText("-")

		self.startRanking = 1
	
	def AddPlayerRanking(self, rank, name, guild, empire, count, selfpos):
		self.RankingList.AppendItem(RankingLine(self.startRanking, name, guild, int(empire), int(count)))
		self.startRanking = self.startRanking + 1
		if name == player.GetName():
			if selfpos > 0:
				self.PlayerRank["rank"].SetText(str(selfpos))
			else:
				self.PlayerRank["rank"].SetText(str(self.startRanking - 1))
			self.PlayerRank["name"].SetText("{}".format(name))
			self.PlayerRank["guild"].SetText("{}".format(guild))
			self.PlayerRank["empire"].LoadImage("d:/ymir work/ui/cw/ranking/table/{}.png".format(empire))
			self.PlayerRank["empire"].SetScale(0.8, 0.8)
			self.PlayerRank["count"].SetText("{}".format(localeInfo.GetFormattedNumberString(count)))
			self.Gasit = True

			
	def Open(self):
		self.SetCenterPosition()
		self.Show()
		self.CategoryList.RemoveAllItems()
		self.Gasit = False
		for i in range(0, 5):
			self.CategoryList.AppendItem(RankingCategory(i % 5, Categories[i % 5], self.SelectCategory))
		self.CategoryList.SelectIndex(0)
		return True
	
	def Close(self):
		self.Hide()
		return True
		
	def OnMouseWheel(self, len):
		if self.CategoryList.IsInPosition():
			pos = float(len) / 120.0 * float(self.ScrollBar.GetScrollStep())
			self.ScrollBar.SetPos(self.ScrollBar.GetPos() - pos)
			return TRUE
		return FALSE