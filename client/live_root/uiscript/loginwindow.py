import app
BG_PATH = "%s/ui/new/login/" % app.GetLocalePath()
ROOT_PATH = "%s/ui/new/login/%s" % (app.GetLocalePath(), "" if SCREEN_WIDTH > 800 else "90_")
X_SCALE = Y_SCALE = 1 if SCREEN_WIDTH > 800 else 0.8

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(

		## Board
		{
			"name" : "bg", "type" : "ani_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"images" : (BG_PATH + "background/%03d.dds" % i for i in xrange(300)),
			"delay" : 2,
		},
		{
			"name" : "login_board",
			"type" : "window",

			"x" : 0,
			"y" : 329 * (float(SCREEN_HEIGHT) / 1080.0),

			"width": 611 * X_SCALE,
			"height": 424 * Y_SCALE,

			"horizontal_align" : "center",

			"children" : (
				{
					"name": "channel1_status",
					"type": "window",

					"x": 85 * X_SCALE,
					"y": 174 * Y_SCALE,

					"width": 5,
					"height": 5,

					"children": (
						{
							"name": "channel1_status_off",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_off.tga",
						},
						{
							"name": "channel1_status_on",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_on.tga",
						},
					),
				},
				{
					"name": "channel2_status",
					"type": "window",

					"x": 40 * X_SCALE,
					"y": 246 * Y_SCALE,

					"width": 5,
					"height": 5,

					"children": (
						{
							"name": "channel2_status_off",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_off.tga",
						},
						{
							"name": "channel2_status_on",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_on.tga",
						},
					),
				},
				{
					"name": "channel3_status",
					"type": "window",

					"x": 528 * X_SCALE,
					"y": 174 * Y_SCALE,

					"width": 5,
					"height": 5,

					"children": (
						{
							"name": "channel3_status_off",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_off.tga",
						},
						{
							"name": "channel3_status_on",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_on.tga",
						},
					),
				},
				{
					"name": "channel4_status",
					"type": "window",

					"x": 573 * X_SCALE,
					"y": 246 * Y_SCALE,

					"width": 5,
					"height": 5,

					"children": (
						{
							"name": "channel4_status_off",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_off.tga",
						},
						{
							"name": "channel4_status_on",
							"type": "image",

							"x": 0,
							"y": 0,

							"image": ROOT_PATH + "channel_status_on.tga",
						},
					),
				},
				{
					"name": "channel3_button",
					"type": "radio_button",

					"x": 432 * X_SCALE,
					"y": 133 * Y_SCALE,

					"default_image": ROOT_PATH + "channel3_button_01.tga",
					"over_image": ROOT_PATH + "channel3_button_02.tga",
					"down_image": ROOT_PATH + "channel3_button_02.tga",

				},
				{
					"name": "channel2_button",
					"type": "radio_button",

					"x": 26 * X_SCALE,
					"y": 203 * Y_SCALE,

					"default_image": ROOT_PATH + "channel2_button_01.tga",
					"over_image": ROOT_PATH + "channel2_button_02.tga",
					"down_image": ROOT_PATH + "channel2_button_02.tga",
				},
				{
					"name": "channel1_button",
					"type": "radio_button",

					"x": 72 * X_SCALE,
					"y": 133 * Y_SCALE,

					"default_image": ROOT_PATH + "channel1_button_01.tga",
					"over_image": ROOT_PATH + "channel1_button_02.tga",
					"down_image": ROOT_PATH + "channel1_button_02.tga",

				},
				{
					"name": "channel4_button",
					"type": "radio_button",

					"x": 478 * X_SCALE, 
					"y": 203 * Y_SCALE,

					"default_image": ROOT_PATH + "channel4_button_01.tga",
					"over_image": ROOT_PATH + "channel4_button_02.tga",
					"down_image": ROOT_PATH + "channel4_button_02.tga",

				},
				{
					"name": "login_header",
					"type": "image",

					"x": 0,
					"y": -2,

					"horizontal_align" : "center",

					"image": ROOT_PATH + "login_header.tga",

					"children" : (
						{
							"name": "login_text",
							"type": "image",

							"x": 0,
							"y": 163 * Y_SCALE,

							"horizontal_align" : "center",

							"image": ROOT_PATH + "login_text.tga",
						},
					)
				},
				## login input
				{
					"name": "id_slot",
					"type": "image",

					"x": 0*X_SCALE,
					"y": 207*Y_SCALE,

					"image": ROOT_PATH + "input_slot.tga",

					"horizontal_align" : "center",

					"children" : (
						{
							"name": "id_text",
							"type": "image",

							"x" : 36*X_SCALE,
							"y" : 10*Y_SCALE,

							"image": ROOT_PATH + "id_text.tga",
						},
						{
							"name" : "ID_EditLine",
							"type" : "editline",

							"x" : 36*X_SCALE,
							"y" : 8*Y_SCALE,

							"width" : 217*X_SCALE,
							"height" : 36*Y_SCALE,

							"input_limit" : 16,
							"enable_codepage" : 0,

							"color" : 0xff7a807a,
						},
					),
				},

				## password input

				{
					"name": "password_slot",
					"type": "image",

					"x": 0*X_SCALE,
					"y": 249*Y_SCALE,

					"image": ROOT_PATH + "input_slot.tga",

					"horizontal_align" : "center",

					"children" : (
						{
							"name": "password_text",
							"type": "image",

							"x" : 36*X_SCALE,
							"y" : 10*Y_SCALE,

							"image": ROOT_PATH + "pwd_text.tga",
						},
						{
							"name" : "Password_EditLine",
							"type" : "editline",

							"x" : 36*X_SCALE,
							"y" : 8*Y_SCALE,

							"width" : 217,
							"height" : 36,

							"input_limit": 16,
							"secret_flag": 1,
							"enable_codepage": 0,

							"color" : 0xff7a807a,
						},
					),
				},

				{
					"name": "account_save_button",
					"type": "button",

					"x": 221 * X_SCALE,
					"y": 290 * Y_SCALE,

					"default_image": ROOT_PATH + "account_save_button_01.tga",
					"over_image": ROOT_PATH + "account_save_button_02.tga",
					"down_image": ROOT_PATH + "account_save_button_02.tga",

				},

				{
					"name": "login_button",
					"type": "button",

					"x": 0*X_SCALE,
					"y": 347*Y_SCALE,

					"horizontal_align": "center",

					"default_image": ROOT_PATH + "login_button_01.tga",
					"over_image": ROOT_PATH + "login_button_02.tga",
					"down_image": ROOT_PATH + "login_button_02.tga",

				},
			),
		},
		{
			"name": "account_board",
			"type": "window",

			"x": 0,
			"y": 205 * (float(SCREEN_HEIGHT) / 1080.0),

			"width" : 981 * X_SCALE,
			"height" : 144 * Y_SCALE,

			"horizontal_align" : "center",
			"vertical_align" : "bottom",

			"children": (
				{
					"name": "account1_slot",
					"type": "image",

					"x": 0*X_SCALE,
					"y": 0*Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account1_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name" : "account1_load_button",
							"type" : "button",

							"x" : 177*X_SCALE,
							"y" : 26*Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name" : "account1_delete_button",
							"type" : "button",

							"x" : 202*X_SCALE,
							"y" : 26*Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
				{
					"name": "account2_slot",
					"type": "image",

					"x": 239 * X_SCALE,
					"y": 0 * Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account2_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name": "account2_load_button",
							"type": "button",

							"x": 177 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name": "account2_delete_button",
							"type": "button",

							"x": 202 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
				{
					"name": "account3_slot",
					"type": "image",

					"x": 478 * X_SCALE,
					"y": 0 * Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account3_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name": "account3_load_button",
							"type": "button",

							"x": 177 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name": "account3_delete_button",
							"type": "button",

							"x": 202 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
				{
					"name": "account4_slot",
					"type": "image",

					"x": 717 * X_SCALE,
					"y": 0 * Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account4_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name": "account4_load_button",
							"type": "button",

							"x": 177 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name": "account4_delete_button",
							"type": "button",

							"x": 202 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
				{
					"name": "account5_slot",
					"type": "image",

					"x": 0*X_SCALE,
					"y": 68*Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account5_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name" : "account5_load_button",
							"type" : "button",

							"x" : 177*X_SCALE,
							"y" : 26*Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name" : "account5_delete_button",
							"type" : "button",

							"x" : 202*X_SCALE,
							"y" : 26*Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
				{
					"name": "account6_slot",
					"type": "image",

					"x": 239 * X_SCALE,
					"y": 68 * Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account6_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name": "account6_load_button",
							"type": "button",

							"x": 177 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name": "account6_delete_button",
							"type": "button",

							"x": 202 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
				{
					"name": "account7_slot",
					"type": "image",

					"x": 478 * X_SCALE,
					"y": 68 * Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account7_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name": "account7_load_button",
							"type": "button",

							"x": 177 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name": "account7_delete_button",
							"type": "button",

							"x": 202 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
				{
					"name": "account8_slot",
					"type": "image",

					"x": 717 * X_SCALE,
					"y": 68 * Y_SCALE,

					"image": ROOT_PATH + "account_slot.tga",

					"children": (
						{
							"name": "account8_text",
							"type": "text",

							"x": 44 * X_SCALE,
							"y": 28 * Y_SCALE,

						},
						{
							"name": "account8_load_button",
							"type": "button",

							"x": 177 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_load_button_01.tga",
							"over_image": ROOT_PATH + "account_load_button_02.tga",
							"down_image": ROOT_PATH + "account_load_button_02.tga",
						},
						{
							"name": "account8_delete_button",
							"type": "button",

							"x": 202 * X_SCALE,
							"y": 26 * Y_SCALE,

							"default_image": ROOT_PATH + "account_delete_button_01.tga",
							"over_image": ROOT_PATH + "account_delete_button_02.tga",
							"down_image": ROOT_PATH + "account_delete_button_02.tga",
						},
					),
				},
			),
		},
		{
			"name": "close_button",
			"type": "button",

			"x": SCREEN_WIDTH - 25 - 20 - 30,
			"y": 20,

			"default_image": BG_PATH + "close_button_01.tga",
			"over_image": BG_PATH + "close_button_02.tga",
			"down_image": BG_PATH + "close_button_02.tga",

		},
	),
}
