import uiScriptLocale

window = {
	"name" : "Eveniment",

	"x" : SCREEN_WIDTH - 175 - 650,
	"y" : SCREEN_HEIGHT - 37 - 575,

	"style" : ("movable", "float", "animate", "window_without_alpha",),

	"width" : 485,
	"height" : 350,

	"children" :
	(
		## Board and buttons
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 485,
			"height" : 240,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 7,

					"width" : 474,

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":240, "y":3, "text":"Evenimentul Literelor", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "board_event",
					"type" : "image",
					"style" : ("attach",),

					"x" : 5,
					"y" : 30,

					"image" : "d:/ymir work/eventlitere/letters_event.png",
				},
				{
					"name" : "board_reward",
					"type" : "border_a",

					"x" : 1,
					"y" : 240,

					"width" : 200,
					"height" : 110,

				},
				# Take Reward
				{
					"name" : "TakeReward",
					"type" : "button",
					"tooltip_text" : "Colecteaza recompensa",

					"x" : 280,
					"y" : 170,

					#"tooltip_text" : "Colecteaza recompensa",

					"default_image" : "d:/ymir work/eventlitere/btn_take_02.tga",
					"over_image" : "d:/ymir work/eventlitere/btn_take_03.tga",
					"down_image" : "d:/ymir work/eventlitere/btn_take_03.tga",
				},
				{
					"name" : "ManageReward",
					"type" : "button",
					"tooltip_text" : "Informatii recompense",

					"x" : 70,
					"y" : 170,

					#"tooltip_text" : "Colecteaza recompensa",

					"default_image" : "d:/ymir work/eventlitere/btn_add_02.tga",
					"over_image" : "d:/ymir work/eventlitere/btn_add_03.tga",
					"down_image" : "d:/ymir work/eventlitere/btn_add_03.tga",
				},


			),
		},
	),
}