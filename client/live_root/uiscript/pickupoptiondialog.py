import uiScriptLocale

BOARD_WIDTH = 260
BOARD_HEIGHT = 220

DROPS_LINE_X = 15
DROPS_LINE_X_2 = DROPS_LINE_X + 80
DROPS_LINE_X_3 = DROPS_LINE_X_2 + 80

DEFAULT_BTN_IMAGE = "d:/ymir work/ui/public/middle_button_01.sub"
OVER_BTN_IMAGE = "d:/ymir work/ui/public/middle_button_02.sub"
DOWN_BTN_IMAGE = "d:/ymir work/ui/public/middle_button_03.sub"

window = {
	"name" : "PickupOptionDialog",
	"style" : ["movable", "float",],

	"x" : 0,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : uiScriptLocale.EXTENDED_PICKUP_TITLE,

			"children" :
			(

				{
					"name": "pickup_mode_bar",
					"type":"horizontalbar",

					"x": DROPS_LINE_X,
					"y": 37,

					"width": 230,

					"children" : (
						{
							"name": "pickup_mode",
							"type": "text",

							"x": 0,
							"y": 0,

							"text": uiScriptLocale.EXTENDED_PICKUP_MODE_LABEL,
							"all_align": "center",
						},
					),
				},
				{
					"name" : "pickup_mode_single",
					"type" : "radio_button",

					"x" : DROPS_LINE_X,
					"y" : 61,

					"text" : uiScriptLocale.EXTENDED_PICKUP_MODE_SINGLE_LABEL,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "pickup_mode_all",
					"type" : "radio_button",

					"x" : DROPS_LINE_X_2 + 15,
					"y" : 61,

					"text" : uiScriptLocale.EXTENDED_PICKUP_MODE_ALL_LABEL,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},

				{
					"name": "drops_ignore_bar",
					"type":"horizontalbar",

					"x": DROPS_LINE_X,
					"y": 97,

					"width": 230,

					"children" : (
						{
							"name": "drops_ignore",
							"type": "text",

							"x": 0,
							"y": 0,

							"text": uiScriptLocale.EXTENDED_PICKUP_IGNORE_LABEL,
							"all_align": "center",
						},
					),
				},

				{
					"name" : "drops_ignore_weapon",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X,
					"y" : 122,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_WEAPON_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},

				{
					"name" : "drops_ignore_armor",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X,
					"y" : 152,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_ARMOR_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},
				{
					"name" : "drops_ignore_head",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X,
					"y" : 182,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_HEAD_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},
				{
					"name" : "drops_ignore_wrist",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X_2,
					"y" : 122,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_WRIST_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},
				{
					"name" : "drops_ignore_foots",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X_2,
					"y" : 152,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_FOOTS_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},

				{
					"name" : "drops_ignore_neck",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X_2,
					"y" : 182,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_NECK_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},

				{
					"name" : "drops_ignore_ear",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X_3,
					"y" : 122,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_EAR_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},
				{
					"name" : "drops_ignore_shield",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X_3,
					"y" : 152,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_SHIELD_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},
				{
					"name" : "drops_ignore_etc",
					"type" : "toggle_button",

					"x" : DROPS_LINE_X_3,
					"y" : 182,

					"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_ETC_LABEL,

					"default_image" : DEFAULT_BTN_IMAGE,
					"over_image" : OVER_BTN_IMAGE,
					"down_image" : DOWN_BTN_IMAGE,
				},
			),
		},
	),
}
