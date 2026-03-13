import app
BG_PATH = "%s/ui/new/select_empire/" % app.GetLocalePath()
ROOT_PATH = "%s/ui/new/select_empire/%s" % (app.GetLocalePath(), "" if SCREEN_WIDTH > 800 else "90_")
X_SCALE = Y_SCALE = 1 if SCREEN_WIDTH > 800 else 0.8

window = {
	"name" : "SelectCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name": "BackGround", "type": "ani_image", "x": 0, "y": 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"images": (BG_PATH + "background/%03d.dds" % (i + 1) for i in xrange(200)),
			"delay": 2,
		},
		{
			"name" : "logo",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : BG_PATH + "logo.tga",
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
		},

		{
			"name" : "empire_window",
			"type" : "window",

			"x" : (SCREEN_WIDTH - (975 * X_SCALE)) / 2,
			"y" : (SCREEN_HEIGHT - (676 * Y_SCALE)) / 2 + 31,

			"width": 975 * X_SCALE,
			"height": 676 * Y_SCALE,

			"children" : (
				{
					"name" : "info_header",
					"type" : "image",

					"x" : 0,
					"y" : 0,

					"horizontal_align": "center",

					"image" : ROOT_PATH + "info_header.tga",
				},
				{
					"name" : "empire_text",
					"type" : "image",

					"x" : 0,
					"y" : 319 * Y_SCALE,

					"horizontal_align": "center",

					"image" : ROOT_PATH + "empire_text.tga",
				},
				{
					"name": "empire_button_B",
					"type": "radio_button",

					"x" : 0,
					"y" : 335 * Y_SCALE,

					"default_image": ROOT_PATH + "empirebutton_b_01.tga",
					"over_image": ROOT_PATH + "empirebutton_b_02.tga",
					"down_image": ROOT_PATH + "empirebutton_b_03.tga",
				},
				{
					"name": "empire_button_C",
					"type": "radio_button",

					"x" : 308 * X_SCALE,
					"y" : 336 * Y_SCALE,

					"default_image": ROOT_PATH + "empirebutton_c_01.tga",
					"over_image": ROOT_PATH + "empirebutton_c_02.tga",
					"down_image": ROOT_PATH + "empirebutton_c_03.tga",
				},
				{
					"name": "empire_button_A",
					"type": "radio_button",

					"x" : 615 * X_SCALE,
					"y" : 335 * Y_SCALE,

					"default_image": ROOT_PATH + "empirebutton_a_01.tga",
					"over_image": ROOT_PATH + "empirebutton_a_02.tga",
					"down_image": ROOT_PATH + "empirebutton_a_03.tga",
				},
				{
					"name" : "select_button",
					"type": "button",

					"x": 0,
					"y": 543 * Y_SCALE,

					"horizontal_align" : "center",

					"default_image": ROOT_PATH + "select_button_01.tga",
					"over_image": ROOT_PATH + "select_button_02.tga",
					"down_image": ROOT_PATH + "select_button_02.tga",
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
	),
}
