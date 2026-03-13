import uiScriptLocale

window = {
	"name" : "Biolog",

	"x" : SCREEN_WIDTH - 175 - 650,
	"y" : SCREEN_HEIGHT - 37 - 575,

	"style" : ("movable", "float","animate",),

	"width" : 338 - 7 - 6,
	"height" : 270 - 17,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 338- 7- 6,
			"height" : 270 - 17,

			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 7,

					"width" : 338 - 18 - 6,

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":338 / 2 - 15, "y":3, "text":"Biolog", "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "bg_circle",
					"type" : "thinboard_circle",

					"x" : 7,
					"y" : 30,

        			"width" : 338 - 7 - 21,
        			"height" : 270 - 55,
				},

				{
					"name" : "bg_extra_info","type" : "thinboard_circle","x" : 12,"y" : 147,"width" : 62,"height" : 50,
				},

				{
					"name" : "bg_2info","type" : "thinboard_circle","x" : 12,"y" : 205,"width" : 283 - 38,"height" : 35,
				},

				{
					"name" : "bg_extra_info2","type" : "thinboard_circle","x" : 260,"y" : 147,"width" : 52,"height" : 93,
				},

				{
					"name": "BarHorizontal",
					"type":"horizontalbar",
					"x": 10,
					"y": 35,
					"width": 305,
					"children" :
					(
						{
							"name": "Text1",
							"type":  "text",
							"x": 128,
							"y": 2,
							"text": "Reward List",
						},
					),
				},

				{
					"name": "BarHorizontalDown",
					"type":"horizontalbar",
					"x": 10,
					"y": 125,
					"width": 305,
					"children" :
					(
						{
							"name": "TextDown1",
							"type":  "text",
							"x": 5,
							"y": 2,
							"text": "Extra Reward",
						},
						{
							"name": "TextDown2",
							"type":  "text",
							"x": 128,
							"y": 2,
							"text": "Time Left",
						},
						{
							"name": "TextDown3",
							"type":  "text",
							"x": 255,
							"y": 2,
							"text": "Req. Item",
						},
					),
				},

				{
					"name":"Time_Slot",
					"type":"button",

					"x":0,
					"y":45,

					"horizontal_align":"center",
					"vertical_align":"center",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name" : "TimeLeft",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"text" : "0 Min.",
						},
					),
				},

				{
					"name": "TextRemain",
					"type":  "text",
					"x": 277,
					"y": 210,
					"text": "0 / 5",
				},

				{
					"name" : "DeliveryButton",
					"type" : "button",

					"x" : 80,
					"y" : 211,

					"width" : 61,
					"height" : 21,

					"text" : "Delivery",

					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},

			),
		},
	),
}