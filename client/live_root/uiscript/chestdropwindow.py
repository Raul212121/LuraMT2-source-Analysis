import uiScriptLocale

BUTTON_ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "ChestDropWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float", "animate",),

	"width" : 500-160,
	"height" : 250,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 500-160,
			"height" : 250,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 500 - 12-160,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x": 0, "y":3, "text": uiScriptLocale.CHEST_DROP_VIEW, "horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "prev_button",
					"type" : "button",

					"x" : 422-285,
					"y" : 216-35,

					"default_image" : "d:/ymir work/ui/public/public_page_button/page_first_prev_btn_01.sub",
					"over_image" 	: "d:/ymir work/ui/public/public_page_button/page_first_prev_btn_02.sub",
					"down_image" 	: "d:/ymir work/ui/public/public_page_button/page_first_prev_btn_01.sub",
				},

				{
					"name" : "CurrentPageBack",
					"type" : "thinboard_circle",

					"x" : 440-285,
					"y" : 211-35,

					"width" : 30,
					"height" : 20,

					"children" :
					(
						{
							"name" : "CurrentPage",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"vertical_align" : "center",
							"horizontal_align" : "center",

							"text_vertical_align" : "center",
							"text_horizontal_align" : "center",

							"text" : "1",
						},
					),
				},

				{
					"name" : "next_button",
					"type" : "button",

					"x" : 475-285,
					"y" : 216-35,

					"default_image" : "d:/ymir work/ui/public/public_page_button/page_last_next_btn_01.sub",
					"over_image" 	: "d:/ymir work/ui/public/public_page_button/page_last_next_btn_02.sub",
					"down_image" 	: "d:/ymir work/ui/public/public_page_button/page_last_next_btn_01.sub",
				},
			),
		},
	),
}

