import uiScriptLocale

WINDOW_WIDTH = 513
WINDOW_HEIGHT = 350

PASS_X = 12
PASS_Y = 5

ROOT_PATH = "d:/ymir work/ui/game/battle_pass/"

window = {
	"name" : "DungeonListWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float", ),

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children":
	(
		{
			"name": "board",
			"type": "image",

			"style" : ("attach",),

			"width": WINDOW_WIDTH,
			"height": WINDOW_HEIGHT,

			"x": 0,
			"y": 0,

			"image" : "d:/ymir work/ui/cw/battlepass/background.png",

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : WINDOW_WIDTH - 15,
					"color" : "yellow",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",

							"x" : (WINDOW_WIDTH - 15) / 2,
							"y" : 3,

							"text" : "Battlepass System",
							"text_horizontal_align":"center"
						},
					),
				},

				{
					"name" : "BorderMissions",
					"type" : "window",

					"width": 305,
					"height": 310,
					"x" : 10,
					"y" : 31,


				},

				# Buttons scroll
				{
					"name" : "ButtonsScrollBar",
					"type" : "slimscrollbar",

					#"bar_image" : "d:/ymir work/ui/cw/battlepass/scrollbar_big.png",

					"x" : 321,
					"y" : 30,
					"size" : 337,
				},

				{
					"name" : "BorderMissionReward",
					"type" : "window",

					"width": 140,
					"height": 160,

					"x" : 335,
					"y" : 178,
				},

				{
					"name" : "ButtonsScrollBarReward",
					"type" : "slimscrollbar",

					#"bar_image" : "d:/ymir work/ui/cw/battlepass/scrollbar_big.png",

					"x" : 478,
					"y" : 208,
					"size" : 128,
				},

				{
					"name" : "BattlePassInfo",
					"type" : "text",

					"x" : 340 + 76,
					"y" : 41,

					#"color" : 0xFF9C8B55,

					"text" : "Battlepass Information",
					"text_horizontal_align":"center"
				},

				{
					"name" : "BattlePassInfo",
					"type" : "text",

					"x" : 340 + 76,
					"y" : 65,

					"color" : 0xFF9C8B55,

					"text" : "Description",
					"text_horizontal_align":"center"
				},

				{  "name" : "Desc0", "type" : "text",  "x" : 340 + 77, "y" : 83 + 5,  "text" : "Complete each quest to get", "text_horizontal_align":"center" },
				{  "name" : "Desc1", "type" : "text",  "x" : 340 + 77, "y" : 93 + 5,  "text" : "a special reward", "text_horizontal_align":"center" },
				{  "name" : "Desc2", "type" : "text",  "x" : 340 + 77, "y" : 110 + 15,  "text" : "This is a beginner BattlePass", "text_horizontal_align":"center" },
				{  "name" : "Desc3", "type" : "text",  "x" : 340 + 77, "y" : 110 + 25,  "text" : "This one will not expire", "text_horizontal_align":"center" },

				{
					"name" : "BattlePassInfoReward",
					"type" : "text",

					"x" : 340 + 76,
					"y" : 191,

					"color" : 0xFF9C8B55,

					"text" : "Final Reward",
					"text_horizontal_align":"center"
				},

				{
					"name" : "bar",
					"type" : "bar",

					"x" : 5,
					"y" : 30,

					"width" : 540 - 39,
					"height" : 500 - 182,

				},
			),
		},
	),
}

