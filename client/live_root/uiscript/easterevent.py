import localeInfo
import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/game/easter_event/"
BOARD_WIDTH = 400
BOARD_HEIGHT = 400

window = {
	"name" : "EasterEvent",
	"style" : ("movable", "float","animate",),
	"x" : 0,
	"y" : 0,
	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,
	"children" :
	(
		{
			"name" : "BoardWithTitle",
			"type" : "new_dragonboard_with_titlebar",
			"x" : 0,
			"y" : 0,
			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			"title" : uiScriptLocale.EASTER_EVENT_2022,
			"children" :
			(
				{
					"name" : "easterBasket",
					"type" : "image",
					"x" : 30,
					"y" : 20,
					"image" : ROOT_PATH + "black.png",
				},
			),
		},
	),
}