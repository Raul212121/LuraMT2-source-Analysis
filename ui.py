#1.0 Search:
class Board(Window):

#1.1 Add after whole class:
class BorderA(Window):
	CORNER_WIDTH = 16
	CORNER_HEIGHT = 16
	LINE_WIDTH = 16
	LINE_HEIGHT = 16
	BOARD_COLOR = grp.GenerateColor(0.17, 0.027, 0.0, 0.70)

	LT = 0
	LB = 1
	RT = 2
	RB = 3
	L = 0
	R = 1
	T = 2
	B = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

		CornerFileNames = [ "d:/ymir work/ui/pattern/border_a/border_a_"+dir+".tga" for dir in ["Left_Top","Left_Bottom","Right_Top","Right_Bottom"] ]
		LineFileNames = [ "d:/ymir work/ui/pattern/border_a/border_a_"+dir+".tga" for dir in ["Left","Right","Top","Bottom"] ]

		self.Corners = []
		for fileName in CornerFileNames:
			Corner = ExpandedImageBox()
			Corner.AddFlag("not_pick")
			Corner.LoadImage(fileName)
			Corner.SetParent(self)
			Corner.SetPosition(0, 0)
			Corner.Show()
			self.Corners.append(Corner)

		self.Lines = []
		for fileName in LineFileNames:
			Line = ExpandedImageBox()
			Line.AddFlag("not_pick")
			Line.LoadImage(fileName)
			Line.SetParent(self)
			Line.SetPosition(0, 0)
			Line.Show()
			self.Lines.append(Line)

		self.Base = ExpandedImageBox()
		self.Base.AddFlag("not_pick")
		self.Base.LoadImage("d:/ymir work/ui/pattern/border_a/border_a_center.tga")
		self.Base.SetParent(self)
		self.Base.SetPosition(self.CORNER_WIDTH, self.CORNER_HEIGHT)
		self.Base.Show()

		self.Lines[self.L].SetPosition(0, self.CORNER_HEIGHT)
		self.Lines[self.T].SetPosition(self.CORNER_WIDTH, 0)

	def __del__(self):
		Window.__del__(self)

	def SetSize(self, width, height):

		width = max(self.CORNER_WIDTH*2, width)
		height = max(self.CORNER_HEIGHT*2, height)
		Window.SetSize(self, width, height)

		self.Corners[self.LB].SetPosition(0, height - self.CORNER_HEIGHT)
		self.Corners[self.RT].SetPosition(width - self.CORNER_WIDTH, 0)
		self.Corners[self.RB].SetPosition(width - self.CORNER_WIDTH, height - self.CORNER_HEIGHT)
		self.Lines[self.R].SetPosition(width - self.CORNER_WIDTH, self.CORNER_HEIGHT)
		self.Lines[self.B].SetPosition(self.CORNER_HEIGHT, height - self.CORNER_HEIGHT)

		verticalShowingPercentage = float((height - self.CORNER_HEIGHT*2) - self.LINE_HEIGHT) / self.LINE_HEIGHT
		horizontalShowingPercentage = float((width - self.CORNER_WIDTH*2) - self.LINE_WIDTH) / self.LINE_WIDTH
		self.Lines[self.L].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.R].SetRenderingRect(0, 0, 0, verticalShowingPercentage)
		self.Lines[self.T].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)
		self.Lines[self.B].SetRenderingRect(0, 0, horizontalShowingPercentage, 0)

		if self.Base:
			self.Base.SetRenderingRect(0, 0, horizontalShowingPercentage, verticalShowingPercentage)

	def ShowInternal(self):
		self.Base.Show()
		for wnd in self.Lines:
			wnd.Show()
		for wnd in self.Corners:
			wnd.Show()

	def HideInternal(self):
		self.Base.Hide()
		for wnd in self.Lines:
			wnd.Hide()
		for wnd in self.Corners:
			wnd.Hide()

#2.0 Search for:
			elif Type == "board":
				parent.Children[Index] = Board()
				parent.Children[Index].SetParent(parent)
				self.LoadElementBoard(parent.Children[Index], ElementValue, parent)

#2.1 Add after:
			elif Type == "border_a":
				parent.Children[Index] = BorderA()
				parent.Children[Index].SetParent(parent)
				self.LoadElementBorderA(parent.Children[Index], ElementValue, parent)

#3.0 Search for:
	def LoadElementBoard(self, window, value, parentWindow):

		if FALSE == self.CheckKeyList(value["name"], value, self.BOARD_KEY_LIST):
			return FALSE

		window.SetSize(int(value["width"]), int(value["height"]))
		self.LoadDefaultData(window, value, parentWindow)

		return TRUE

#3.1 Add after:
	## BoardA
	def LoadElementBorderA(self, window, value, parentWindow):

		if FALSE == self.CheckKeyList(value["name"], value, self.BOARD_KEY_LIST):
			return FALSE

		window.SetSize(int(value["width"]), int(value["height"]))
		self.LoadDefaultData(window, value, parentWindow)

		return TRUE