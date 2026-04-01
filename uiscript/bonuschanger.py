import uiScriptLocale

WINDOW_X = 320
WINDOW_Y = 425

window = {
	"name" : "ChangerWindow", "style" : ("movable", "float", "window_without_alpha"),
	"x" : SCREEN_WIDTH/2, "y" : SCREEN_HEIGHT - 37 - 563,
	"width" : WINDOW_X, "height" : WINDOW_Y,

	"children" :
	(
		{
			"name" : "Board", "type" : "board", "style" : ("attach",), "x" : 0, "y" : 0,
			"width" : WINDOW_X, "height" : WINDOW_Y,

			"children" :
			(
				{
					"name" : "TitleBar", "type" : "titlebar", "style" : ("attach",), "x" : 8, "y" : 7,
					"width" : WINDOW_X-15, "color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x" : 0, "y" : 3, "text": uiScriptLocale.BONUS_CHANGER_TITLE, "text_horizontal_align":"center", "horizontal_align" : "center" },
					),
				},
				{
					"name" : "ChangerBackground", "type" : "window", "style" : ("attach", "ltr",), "x" : 10, "y" : 32,
					"width" : 300, "height" : 215,

					"children" :
					(
						{
							"name" : "pattern_left_top_img", "type" : "image", "style" : ("ltr",), "x" : 0, "y" : 0,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_left_top.tga",
						},
						{
							"name" : "pattern_right_top_img", "type" : "image", "style" : ("ltr",), "x" : 300 - 16, "y" : 0,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_right_top.tga",
						},
						{
							"name" : "pattern_left_bottom_img", "type" : "image", "style" : ("ltr",), "x" : 0, "y" : 215 - 16,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_left_bottom.tga",
						},
						{
							"name" : "pattern_right_bottom_img", "type" : "image", "style" : ("ltr",), "x" : 300 - 16, "y" : 215 - 16,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_right_bottom.tga",
						},
						{
							"name" : "pattern_top_center_img", "type" : "expanded_image", "style" : ("ltr",), "x" : 16, "y" : 0,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_top.tga",
							"rect" : (0.0, 0.0, (300 - 32) / 16, 0),
						},
						{
							"name" : "pattern_left_center_img", "type" : "expanded_image", "style" : ("ltr",), "x" : 0, "y" : 16,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_left.tga",
							"rect" : (0.0, 0.0, 0, (215 - 32) / 16),
						},
						{
							"name" : "pattern_right_center_img", "type" : "expanded_image", "style" : ("ltr",), "x" : 300 - 16, "y" : 16,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_right.tga",
							"rect" : (0.0, 0.0, 0, (215 - 32) / 16),
						},
						{
							"name" : "pattern_bottom_center_img", "type" : "expanded_image", "style" : ("ltr",), "x" : 16, "y" : 215 - 16,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_bottom.tga",
							"rect" : (0.0, 0.0, (300 - 32) / 16, 0),
						},
						{
							"name" : "pattern_center_img", "type" : "expanded_image", "style" : ("ltr",), "x" : 16, "y" : 16,
							"image" : "d:/ymir work/ui/pattern/border_a/border_A_center.tga",
							"rect" : (0.0, 0.0, (300 - 32) / 16, (215 - 32) / 16),
						},
						{
							"name": "BackgroundImage", "type": "image", "x" : 4, "y" : 2,
							"image": "d:/ymir work/ui/changer/background.png",
						},
						{
							"name" : "ItemsSlots", "type" : "slot", "x" : 0, "y" : 0,
							"width" : 290, "height" : 180,

							"slot" :
							(
								{"index" : 0, "x" : 235, "y" : 47, "width" : 32, "height" : 96}, #ITEM
								{"index" : 1, "x" : 42, "y" : 91, "width" : 32, "height" : 32}, #CHANGER
							),
						},
						{
							"name": "ChangeButton", "type": "button", "x": 136, "y": 90,
							"default_image" : "d:/ymir work/ui/changer/change_button_norm.png",
							"over_image" : "d:/ymir work/ui/changer/change_button_hover.png",
							"down_image" : "d:/ymir work/ui/changer/change_button_down.png",
						},
					),
				},
				{
					"name" : "BonusBackground", "type" : "window", "style" : ("attach",), "x" : 10, "y" : 250,
					"width" : 300, "height" : 165,

					"children" :
					(
						{
							"name": "BonusInput1", "type": "image", "x": 6, "y": 5,
							"image" : "d:/ymir work/ui/changer/input.png",

							"children":
							(
								{
									"name": "BonusName1", "type": "text", "x": 5, "y": 5,
									"text": "",
								},
							),
						},
						{
							"name": "BonusInput2", "type": "image", "x": 6, "y": 37,
							"image" : "d:/ymir work/ui/changer/input.png",

							"children":
							(
								{
									"name": "BonusName2", "type": "text", "x": 5, "y": 5,
									"text": "",
								},
							),
						},
						{
							"name": "BonusInput3", "type": "image", "x": 6, "y": 69,
							"image" : "d:/ymir work/ui/changer/input.png",

							"children":
							(
								{
									"name": "BonusName3", "type": "text", "x": 5, "y": 5,
									"text": "",
								},
							),
						},
						{
							"name": "BonusInput4", "type": "image", "x": 6, "y": 101,
							"image" : "d:/ymir work/ui/changer/input.png",

							"children":
							(
								{
									"name": "BonusName4", "type": "text", "x": 5, "y": 5,
									"text": "",
								},
							),
						},
						{
							"name": "BonusInput5", "type": "image", "x": 6, "y": 133,
							"image" : "d:/ymir work/ui/changer/input.png",

							"children":
							(
								{
									"name": "BonusName5", "type": "text", "x": 5, "y": 5,
									"text": "",
								},
							),
						},
					),
				},
			),
		},
	),
}