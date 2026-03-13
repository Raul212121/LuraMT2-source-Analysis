BUTTON_ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "BookDayEventWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 195,
	"height" : 110 + 75,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 195,
			"height" : 110 + 75,

			"children" :
			(

				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 180,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":  160 / 2 + 9, "y":3, "text": "Eveniment Minute", "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "firstBoard",
					"type" : "border_a",
					"style" : ("attach",),

					"x" : 17,
					"y" : 31,

					"width" : 40*4 + 2,
					"height" : 60,

					"children" :
					(
						{ "name":"First", "type":"text", "x":  77, "y":5, "text": "Target: 20.000 Minute", "text_horizontal_align":"center" },
						{
							"name" : "Slot",
							"type" : "grid_table",

							"x" : 9,
							"y" : 23,

							"start_index" : 0,
							"x_count" : 4,
							"y_count" : 1,
							"x_step" : 36,
							"y_step" : 32,

							"image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
					),
				},

				{
					"name" : "secondBoard",
					"type" : "border_a",
					"style" : ("attach",),

					"x" : 17,
					"y" : 94,

					"width" : 40*4 + 2,
					"height" : 60,

					"children" :
					(
						{ "name":"Second", "type":"text", "x":  80, "y":5, "text": "Urmatorul Target: 50.000 Minute", "text_horizontal_align":"center" },
						{
							"name" : "Slot2",
							"type" : "grid_table",

							"x" : 9,
							"y" : 23,

							"start_index" : 0,
							"x_count" : 4,
							"y_count" : 1,
							"x_step" : 36,
							"y_step" : 32,

							"image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
					),
				},

				## noraml donate button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : 50,
					"y" : 155,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : "Colecteaza",
				},

			),
		},
	),
}

