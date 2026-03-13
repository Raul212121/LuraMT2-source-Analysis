import ui
import grp
import component
import player

BOARD_WIDTH = 465
PLAYER_LIMIT = 10

class GuildWarPlayer(ui.Window):

	NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
	POSITIVE_COLOR = grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)
	TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
	SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0)
	
	def __init__(self):
		ui.Window.__init__(self)
	
		self.name = ""
		self.kills = 0
		self.deaths = 0
		self.balance = 0
		self.damage = "0"
		self.level = 0
		
		self.__BuildWindow()
		
	def __del(self):
		ui.Window.__del__(self)
		
	def __TextLine(self, text, x, color = None, centered = False):
		element = self.component.TextLine(self, "", x, 0, None)
		element.SetFontName("Tahoma:14")
		element.SetText(text)
		
		if centered:
			element.SetHorizontalAlignCenter()
		
		if color:
			element.SetPackedFontColor(color)
		
		return element
		
	def __BuildWindow(self):
		c = component.Component()
		self.component = c
		
		self.nameLine = self.__TextLine(self.GetName(), 5)
		self.killsLine = self.__TextLine(self.GetKills(), 126, self.POSITIVE_COLOR, True)
		self.deathsLine = self.__TextLine(self.GetDeaths(), 185, self.NEGATIVE_COLOR, True)
		self.levelLine = self.__TextLine(self.GetLevel(), 239, None, True)
		self.damageLine = self.__TextLine(self.GetDamage(), 358, None, True)
		
		self.Show()
		
	def SetName(self, name):
		self.name = str(name)
		
	def GetName(self):
		return self.name
		
	def SetKills(self, kills):
		self.kills = int(kills)
		self.CalculateBalance()
		
	def GetKills(self):
		return self.kills
		
	def SetDeaths(self, deaths):
		self.deaths = int(deaths)
		self.CalculateBalance()
		
	def GetDeaths(self):
		return self.deaths
		
	def CalculateBalance(self):
		self.balance = max(0, int(self.GetDamage()))
		
	def GetBalance(self):
		return self.balance

	def SetDamage(self, damage):
		self.damage = int(damage)
		
	def GetDamage(self):
		return self.damage

	def SetLevel(self, level):
		self.level = int(level)
		
	def GetLevel(self):
		return self.level
		
	def Render(self):
		name = self.GetName()
		self.killsLine.SetText(str(self.GetKills()))
		self.deathsLine.SetText(str(self.GetDeaths()))
		self.levelLine.SetText(str(self.GetLevel()))
		
		n = self.GetDamage()
		self.damageLine.SetText("%s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ])))
		
		if player.GetName() == name:
			self.nameLine.SetText("> %s <" % name)
			self.nameLine.SetPackedFontColor(self.SPECIAL_POSITIVE_COLOR)
		else:
			self.nameLine.SetText(name)
			self.nameLine.SetPackedFontColor(self.TITLE_COLOR)
		
class GuildWarBoard(ui.Window):
	
	GOLD_COLOR = grp.GenerateColor(1.0, 0.7843, 0.0, 1.0)
	
	def __init__(self, parent):
		self.players = []
		self.guild_id = 0
		self.guild_name = "Guild"
		
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.__BuildWindow()
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def SetGuildName(self, name):
		self.guild_name = name
		self.title.SetText("%s" % name)
		
	def GetGuildName(self):
		return self.guild_name
		
	def SetGuildId(self, id):
		self.guild_id = int(id)
		
		if self.mark:
			self.mark.SetIndex(id)
		
	def GetGuildId(self):
		return self.guild_id
		
	def __CreatePlayer(self, name):
		for player in self.players:
			if player.GetName() == name:
				return player
				
		player = GuildWarPlayer()
		player.SetParent(self)
		player.SetName(name)
		player.Show()
		
		self.players.append(player)
		return player
		
	def AddPlayer(self, name, kills = 0, deaths = 0, level = 0, damage = 0):
		player = self.__CreatePlayer(name)
		
		player.SetKills(kills)
		player.SetDeaths(deaths)
		player.SetLevel(level)
		player.SetDamage(damage)
		
		self.Render()
		
	def ClearPlayers(self):
		self.players = []
		
	def GetMVP(self):
		players = sorted(self.players, key = lambda player: (player.balance, player.damage), reverse = True)

		if len(players) == 0:
			return "~"
			
		return players[0].GetName()
		
	def GetTotalKills(self):
		x = 0
		for player in self.players:
			x += player.GetKills()
		return x
		
	def Render(self):
		players = sorted(self.players, key = lambda player: (player.balance, player.damage), reverse = True)
		players = players[:PLAYER_LIMIT]
		
		y = 29
		
		for player in players:
			player.SetPosition(0, y)
			player.Render()
			y += 20
			
		self.SetSize(BOARD_WIDTH - 22, y + 5)
		
	def __BuildWindow(self):
		c = component.Component()
		self.SetPosition(11, 15)
		
		mark = ui.MarkBox()
		mark.SetParent(self)
		mark.SetPosition(3, 3)
		mark.SetIndex(self.guild_id)
		mark.SetScale(1)
		mark.Show()
		self.mark = mark
		
		title = c.TextLine(self, "", 22, 0, None)
		title.SetPackedFontColor(self.GOLD_COLOR)
		title.SetFontName("Tahoma:14")
		title.SetText("")
		self.title = title
		
		kills = c.TextLine(self, "", 100, 0, None)
		kills.SetFontName("Tahoma:14")
		kills.SetText("Kills")
		self.kills = kills
		
		deaths = c.TextLine(self, "", 170, 0, None)
		deaths.SetFontName("Tahoma:14")
		deaths.SetText("Death")
		self.deaths = deaths
		
		level = c.TextLine(self, "", 223, 0, None)
		level.SetFontName("Tahoma:14")
		level.SetText("Level")
		self.level = level
		
		damage = c.TextLine(self, "", 310, 0, None)
		damage.SetFontName("Tahoma:14")
		damage.SetText("Total Damage")
		self.damage = damage
		
		separator = ui.Line()	
		separator.SetParent(self)
		separator.SetPosition(0, 25)
		separator.SetColor(-1124073473)
		separator.SetSize(BOARD_WIDTH - 22, 0)
		separator.Show()
		self.separator = separator
		
		self.Render()
		
		self.component = c
		self.Show()

class WarVersusBox(ui.Window):

	GOLD_COLOR = grp.GenerateColor(1.0, 0.7843, 0.0, 1.0)
	POSITIVE_COLOR = grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)

	def __init__(self):
		self.boards = []
		self.marks = []
		self.names = []
		self.mvps = []
	
		ui.Window.__init__(self)
		self.__BuildWindow()
		
	def __del__(self):
		del self.boards
		del self.marks
		del self.names
		del self.mvps
		
		ui.Window.__del__(self)
		
	def __MarkBox(self, x):
		mark = ui.MarkBox()
		mark.SetParent(self)
		mark.SetPosition(x, 0)
		mark.SetIndex(0)
		mark.SetScale(3)
		mark.Show()
		
		self.marks.append(mark)
	
	def __TextLine(self, text, x, color = None, centered = False):
		element = self.component.TextLine(self, "", x, 0, None)
		element.SetFontName("Tahoma:14")
		element.SetText(text)
		
		if centered:
			element.SetHorizontalAlignCenter()
		
		if color:
			element.SetPackedFontColor(color)
		
		return element
		
	def __BuildWindow(self):
		c = component.Component()
		
		self.__MarkBox(16)
		self.__MarkBox(237)
		
		self.names.append(c.TextLine(self, "", 68, 1, None))
		self.names.append(c.TextLine(self, "", 289, 1, None))
		
		for name in self.names:
			name.SetPackedFontColor(self.GOLD_COLOR)
			name.SetFontName("Tahoma:14")
		
		self.mvps.append(c.TextLine(self, "", 68, 17, None))
		self.mvps.append(c.TextLine(self, "", 289, 17, None))
		
		for mvp in self.mvps:
			mvp.SetPackedFontColor(self.POSITIVE_COLOR)
			mvp.SetFontName("Tahoma:14")
		
		self.component = c
		self.Show()
		
	def Render(self, y):
		self.SetPosition(0, y)
		
		for i, board in enumerate(self.boards):
			self.marks[i].SetIndex(board.GetGuildId())
			self.marks[i].SetScale(3)
			self.names[i].SetText("%s (%d kills)" % (board.GetGuildName(), board.GetTotalKills()))
			self.mvps[i].SetText("MVP: %s" % board.GetMVP())
		
	def SetBoards(self, boards):
		self.boards = boards
	
class WarBoardWindow(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.__BuildWindow()
		
		self.toggle = False
		
	def __del__(self):
		ui.ThinBoard.__del__(self)
		
	def __BuildWindow(self):
		self.boards = []
	
		self.boards.append(GuildWarBoard(self))
		self.boards.append(GuildWarBoard(self))
		
		versus = WarVersusBox()
		versus.SetParent(self)
		versus.SetBoards(self.boards)
		self.versus = versus
		
		self.Render()
		
	def Render(self):
		y = self.boards[0].GetHeight()
		self.boards[1].SetPosition(11, 15 + y + 5)
		
		height = y + self.boards[1].GetHeight() + 20
		self.versus.Render(height)
		
		height += 15 * 2 + 15
		self.SetSize(BOARD_WIDTH, height)
		
	def AddPlayer(self, guildId, player):
		for board in self.boards:
			if board.GetGuildId() == guildId:
				board.AddPlayer(*player)
				return
		
	def Handle(self, input):
		input = input.split("|")
		
		if len(input) == 0:
			return
		
		if input[0] == "toggle":
			self.toggle = bool(input[1])
			return
		
		if input[0] == "versus":
			self.boards[0].SetGuildId(int(input[1]))
			self.boards[0].SetGuildName(input[2])
			self.boards[1].SetGuildId(int(input[3]))
			self.boards[1].SetGuildName(input[4])
			self.versus.SetBoards(self.boards)
			
			for board in self.boards:
				board.ClearPlayers()
			
			self.Render()
			return
			
		if input[0] == "update":
			self.AddPlayer(int(input[1]), input[2:])
			self.Render()
			return
		
	def IsOnWar(self):
		return self.toggle
		
	def Open(self):
		if not self.IsOnWar():
			return False
			
		self.SetTop()
		self.SetCenterPosition()
		self.Show()
		return True
		
	def Close(self):
		if not self.IsShow():
			return False
			
		self.Hide()
		return True
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
