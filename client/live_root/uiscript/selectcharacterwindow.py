import app
BG_PATH = "%s/ui/new/select_empire/" % app.GetLocalePath()
ROOT_PATH = "%s/ui/new/select/" % app.GetLocalePath()

RENDER_X = 927 if SCREEN_WIDTH < 1920 else 900

window = {
	"name" : "SelectCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		{
			"name" : "BackGround", "type" : "ani_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"images": (BG_PATH + "background/%03d.dds" % i for i in xrange(200)),
			"delay": 2,

			"children" : (
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
			"y" : ((SCREEN_HEIGHT - 598) / 2),

			"width" : 479,
			"height" : 598,

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
							"name": "character_name_value",
							"type": "text",

							"x": 0,
							"y": -1,

							"all_align": "center",

						},
					),
				},

				{
					"name": "character_level_slot",
					"type": "image",

					"x": 0,
					"y": 384,

					"horizontal_align": "center",

					"image": ROOT_PATH + "input_slot.tga",

					"children": (
						{
							"name": "character_level_value",
							"type": "text",

							"x": 0,
							"y": -1,

							"all_align" : "center",

						},
					),
				},
				{
					"name": "character_empire_name_slot",
					"type": "image",

					"x": 0,
					"y": 428,

					"horizontal_align": "center",

					"image": ROOT_PATH + "input_slot.tga",

					"children": (
						{
							"name": "character_empire_name_value",
							"type": "text",

							"x": 0,
							"y": -1,

							"all_align": "center",

						},
					),
				},
				{
					"name": "character_guild_slot",
					"type": "image",

					"x": 0,
					"y": 472,

					"horizontal_align": "center",

					"image": ROOT_PATH + "input_slot.tga",

					"children": (
						{
							"name": "character_guild_value",
							"type": "text",

							"x": 0,
							"y": -1,

							"all_align": "center",

						},
					),
				},
				{
					"name": "start_button",
					"type": "button",

					"x": 0,
					"y": 500,

					"horizontal_align": "center",

					"default_image": ROOT_PATH + "login_button_01.tga",
					"over_image": ROOT_PATH + "login_button_02.tga",
					"down_image": ROOT_PATH + "login_button_02.tga",
				},
			),
		},
		{
			"name": "exit_button",
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
		{
			"name": "delete_button",
			"type": "button",

			"x": (float(SCREEN_WIDTH) * 449.0 / 800.0) - 50.0,
			"y": 135 *  float(SCREEN_HEIGHT) / 1080.0,

			"vertical_align" : "bottom",

			"default_image": ROOT_PATH + "delete_button_01.tga",
			"over_image": ROOT_PATH + "delete_button_02.tga",
			"down_image": ROOT_PATH + "delete_button_02.tga",
		},
		{
			"name": "create_button",
			"type": "button",

			"x": (float(SCREEN_WIDTH) * 449.0 / 800.0) - 50.0,
			"y": 135 * float(SCREEN_HEIGHT) / 1080.0,

			"vertical_align": "bottom",

			"default_image": ROOT_PATH + "create_button_01.tga",
			"over_image": ROOT_PATH + "create_button_02.tga",
			"down_image": ROOT_PATH + "create_button_02.tga",
		},
	),
}
