import app
BG_PATH = "%s/ui/new/select_empire/" % app.GetLocalePath()
ROOT_PATH = "%s/ui/new/create/" % app.GetLocalePath()

RENDER_X = 927 if SCREEN_WIDTH < 1920 else 900

window = {
	"name" : "CreateCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround", "type" : "ani_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"images": (BG_PATH + "background/%03d.dds" % i for i in xrange(200)),
			"delay": 2,

			"children": (
				{
					"name": "render",
					"type": "expanded_image",

					"x": RENDER_X * ((float(SCREEN_WIDTH) / 1920.0) ** 1),
					"y": 827 * ((float(SCREEN_HEIGHT) / 1080.0) ** 1),

					"image": BG_PATH + "render.tga",
					"x_scale": float(SCREEN_WIDTH) / 1920.0, "y_scale": float(SCREEN_HEIGHT) / 1080.0,
				},
			),
		},
		{
			"name" : "character_board",
			"type" : "window",

			"x" : 191 * (float(SCREEN_WIDTH) / 1920.0) ** 3,
			"y" : ((SCREEN_HEIGHT - 608) / 2),

			"width" : 479,
			"height" : 608,

			"children" : (
				{
					"name": "logo",
					"type": "expanded_image",

					"x": 70 * float(SCREEN_WIDTH) / 1920.0,
					"y": -194 * (float(SCREEN_HEIGHT) / 1080.0) ** 2,

					"image": BG_PATH + "logo2.tga",
					"x_scale": float(SCREEN_WIDTH) / 1920.0, "y_scale": float(SCREEN_HEIGHT) / 1080.0,

					"horizontal_align" : "center",
				},
				{
					"name": "login_header",
					"type": "image",

					"x": 0,
					"y": 0,

					"horizontal_align": "center",

					"image": ROOT_PATH + "info_header.tga",
				},
				{
					"name": "character_details",
					"type": "image",

					"x": 0,
					"y": 296,

					"horizontal_align": "center",

					"image": ROOT_PATH + "character_details.tga",
				},
				{
					"name": "character_name_slot",
					"type": "image",

					"x": 0,
					"y": 340,

					"horizontal_align": "center",

					"image": ROOT_PATH + "input_slot.tga",

					"children": (
						{
							"name": "character_name_text",
							"type": "image",

							"x": 44,
							"y": 10,

							"image": ROOT_PATH + "character_name_text.tga",
						},
						{
							"name": "character_name_value",
							"type": "editline",

							"x": 44,
							"y": 8,

							"width": 217,
							"height": 36,

							"input_limit": 12,
							"color" : 0xff7a807a,
						},
					),
				},
				{
					"name" : "gender_button_01",
					"type" : "radio_button",

					"x" : 101,
					"y" : 375,

					"default_image": ROOT_PATH + "gender_man_button_01.tga",
					"over_image": ROOT_PATH + "gender_man_button_02.tga",
					"down_image": ROOT_PATH + "gender_man_button_03.tga",
				},

				{
					"name" : "gender_button_02",
					"type" : "radio_button",

					"x" : 220,
					"y" : 375,

					"default_image": ROOT_PATH + "gender_woman_button_01.tga",
					"over_image": ROOT_PATH + "gender_woman_button_02.tga",
					"down_image": ROOT_PATH + "gender_woman_button_03.tga",
				},
				{
					"name" : "shape_button_01",
					"type" : "radio_button",

					"x" : 101,
					"y" : 430,

					"default_image": ROOT_PATH + "shape1_button_01.tga",
					"over_image": ROOT_PATH + "shape1_button_02.tga",
					"down_image": ROOT_PATH + "shape1_button_03.tga",
				},

				{
					"name" : "shape_button_02",
					"type" : "radio_button",

					"x" : 220,
					"y" : 430,

					"default_image": ROOT_PATH + "shape2_button_01.tga",
					"over_image": ROOT_PATH + "shape2_button_02.tga",
					"down_image": ROOT_PATH + "shape2_button_03.tga",
				},
				{
					"name": "create_button",
					"type": "button",

					"x": 0,
					"y": 551,

					"horizontal_align": "center",

					"default_image": ROOT_PATH + "create_button_01.tga",
					"over_image": ROOT_PATH + "create_button_02.tga",
					"down_image": ROOT_PATH + "create_button_02.tga",
				},
			),
		},
		## Buttons
		{
			"name": "cancel_button",
			"type": "button",

			"x": SCREEN_WIDTH - 25 - 20 - 30,
			"y": 20,

			"default_image": ROOT_PATH + "close_button_01.tga",
			"over_image": ROOT_PATH + "close_button_02.tga",
			"down_image": ROOT_PATH + "close_button_02.tga",

		},
		{
			"name": "left_button",
			"type": "button",

			"x": SCREEN_WIDTH * (450 - 22 * 5) / 800,
			"y": SCREEN_HEIGHT / 2,

			"default_image": ROOT_PATH + "arrow_left_01.tga",
			"over_image": ROOT_PATH + "arrow_left_02.tga",
			"down_image": ROOT_PATH + "arrow_left_02.tga",
		},
		{
			"name": "right_button",
			"type": "button",

			"x": SCREEN_WIDTH * (580 - 22) / 800,
			"y": SCREEN_HEIGHT / 2,

			"default_image": ROOT_PATH + "arrow_right_01.tga",
			"over_image": ROOT_PATH + "arrow_right_02.tga",
			"down_image": ROOT_PATH + "arrow_right_02.tga",
		},
	),
}
