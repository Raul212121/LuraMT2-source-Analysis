"""
ui.py

Suchen "class TextLine(Window):"

darunter 	
	def SetFontColor(self, red, green, blue):
		wndMgr.SetFontColor(self.hWnd, red, green, blue)

hinzufügen : 
"""

	if app.ENABLE_BATTLE_PASS_SYSTEM:
		def SetTextColor(self, color):
			self.SetPackedFontColor(color)



"""
Suchen "class ExpandedImageBox(ImageBox):"

darunter 	
	# [0.0, 1.0] »çÀÌÀÇ °ª¸¸Å­ ÆÛ¼¾Æ®·Î ±×¸®Áö ¾Ê´Â´Ù.
	def SetRenderingRect(self, left, top, right, bottom):
		wndMgr.SetRenderingRect(self.hWnd, left, top, right, bottom)

hinzufügen : 
"""

	if app.ENABLE_IMAGE_CLIP_RECT or app.ENABLE_BATTLE_PASS_SYSTEM:
		def SetClipRect(self, left, top, right, bottom, isVertical = False):
			wndMgr.SetClipRect(self.hWnd, left, top, right, bottom, isVertical)
			


"""
Suchen "class Button(Window):"

darunter 	
	if app.ENABLE_PRIVATE_SHOP_SEARCH_SYSTEM:
		def SetAlpha(self, alpha):
			wndMgr.SetButtonDiffuseColor(self.hWnd, 1.0, 1.0, 1.0, alpha)

		def GetText(self):
			if self.ButtonText:
				return self.ButtonText.GetText()
			else:
				return ""

		def IsDisable(self):
			return wndMgr.IsDisable(self.hWnd)

hinzufügen : 
"""

	if app.ENABLE_BATTLE_PASS_SYSTEM:
		def SetTextColor(self, color):
			if not self.ButtonText:
				return

			self.ButtonText.SetPackedFontColor(color

"""
Suchen "class ThinBoardCircle(Window):"

darunter 	
	def HideInternal(self):
		self.Base.Hide()
		for wnd in self.Lines:
			wnd.Hide()
		for wnd in self.Corners:
			wnd.Hide()

hinzufügen : 
"""

if app.ENABLE_BATTLE_PASS_SYSTEM:
	class BorderA(ThinBoardCircle):
		def __init__(self, layer = "UI"):
			ThinBoardCircle.__init__(self)

		def __del__(self):
			ThinBoardCircle.__del__(self)

		def SetSize(self, width, height):
			ThinBoardCircle.SetSize(self, width, height)



"""
Suchen "def LoadChildren(self, parent, dicChildren):"

darunter 	
			elif Type == "listbar" and app.ENABLE_QUEST_RENEWAL:
				parent.Children[Index] = ListBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBar(parent.Children[Index], ElementValue, parent)

hinzufügen : 
"""

			elif Type == "border_a" and app.ENABLE_BATTLE_PASS_SYSTEM:
				parent.Children[Index] = BorderA()
				parent.Children[Index].SetParent(parent)
				self.LoadElementBoard(parent.Children[Index], ElementValue, parent)


"""
darunter 	
def MakeTextLine(parent):
	textLine = TextLine()
	textLine.SetParent(parent)
	textLine.SetWindowHorizontalAlignCenter()
	textLine.SetWindowVerticalAlignCenter()
	textLine.SetHorizontalAlignCenter()
	textLine.SetVerticalAlignCenter()
	if app.WJ_MULTI_TEXTLINE:
		textLine.DisableEnterToken()
	textLine.Show()
	return textLine

hinzufügen : 
"""

if app.ENABLE_BATTLE_PASS_SYSTEM:
	def AddTextLine(parent, x, y, text):
		textLine = TextLine()
		textLine.SetParent(parent)
		textLine.SetPosition(x, y)
		textLine.SetText(text)
		if app.WJ_MULTI_TEXTLINE:
			textLine.DisableEnterToken()
		textLine.Show()
		return textLine

	def MakeNewTextLine(parent, horizontalAlign = True, verticalAlgin = True, x = 0, y = 0):
		textLine = TextLine()
		textLine.SetParent(parent)

		if horizontalAlign == True:
			textLine.SetWindowHorizontalAlignCenter()

		if verticalAlgin == True:
			textLine.SetWindowVerticalAlignCenter()

		textLine.SetHorizontalAlignCenter()
		textLine.SetVerticalAlignCenter()
		if app.WJ_MULTI_TEXTLINE:
			textLine.DisableEnterToken()

		if x != 0 and y != 0:
			textLine.SetPosition(x, y)

		textLine.Show()
		return textLine

	def MakeExpandedImageBox(parent, name, x, y, flag = ""):
		image = ExpandedImageBox()
		image.SetParent(parent)
		image.LoadImage(name)
		image.SetPosition(x, y)

		if flag != "":
			image.AddFlag(flag)

		image.Show()

		return image
