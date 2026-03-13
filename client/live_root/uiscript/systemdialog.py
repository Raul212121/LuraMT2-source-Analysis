import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "SystemDialog",
	"style" : ("float","animate",),

	"x" : (SCREEN_WIDTH  - 200) /2,
	"y" : (SCREEN_HEIGHT - 253) /2,

	"width" : 200,
	"height" : 255,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : 200,
			"height" : 255,

			"children" :
			(
				# {
					# "name" : "version",
					# "type" : "button",

					# "x" : 10,
					# "y" : 17,

					# "text" : localeInfo.FormatVersion(app.VERSION),
					# "text_color" : 0xffF8BF24,
					# "tooltip_text" : localeInfo.TOOLTIP_VERSION_INFO,

					# "default_image" : ROOT + "XLarge_Button_01.sub",
					# "over_image" : ROOT + "XLarge_Button_02.sub",
					# "down_image" : ROOT + "XLarge_Button_03.sub",
				# },

				# {
					# "name" : "version",
					# "type" : "text",

					# "x" : 0,
					# "y" : 17+40,
					# "horizontal_align": "center",
					# "text_horizontal_align": "center",

					# "text" : localeInfo.FormatVersion(app.VERSION),

				# },

				
				{
					"name" : "movechannel_button",
					"type" : "button",

					"x" : 10,
					"y" : 20,

					"text" : uiScriptLocale.SYSTEM_MOVE_CHANNEL,
					# "text_color" : 0xffF8BF24,

					"default_image" : ROOT + "XLarge_Button_02.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_02.sub",
				},


				{
					"name" : "system_option_button",
					"type" : "button",

					"x" : 10,
					"y" : 30+20,

					"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "game_option_button",
					"type" : "button",

					"x" : 10,
					"y" : 60+20,

					"text" : uiScriptLocale.GAMEOPTION_TITLE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "change_button",
					"type" : "button",

					"x" : 10,
					"y" : 90+20,

					"text" : uiScriptLocale.SYSTEM_CHANGE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "logout_button",
					"type" : "button",

					"x" : 10,
					"y" : 120+20,

					"text" : uiScriptLocale.SYSTEM_LOGOUT,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "exit_button",
					"type" : "button",

					"x" : 10,
					"y" : 150+20,

					"text" : uiScriptLocale.SYSTEM_EXIT,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 10,
					"y" : 190+20,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
			),
		},
	),
}
