import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"

TEMPORARY_X = +13
BUTTON_TEMPORARY_X = 5
PVP_X = -10

LINE_LABEL_X 	= 30
LINE_DATA_X 	= 90
LINE_STEP	= 25
LINE_BEGIN	= 90
SMALL_BUTTON_WIDTH 	= 45
MIDDLE_BUTTON_WIDTH 	= 65

window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float","animate",),

	"x" : 0,
	"y" : 0,

	"width" : 300,
	"height" : 380,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 300,
			"height" : 380,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 284,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3,
						"text" : uiScriptLocale.GAMEOPTION_TITLE,
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "name_color",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 40+2,

					"text" : uiScriptLocale.OPTION_NAME_COLOR,
				},
				{
					"name" : "name_color_normal",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 40,

					"text" : uiScriptLocale.OPTION_NAME_COLOR_NORMAL,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "name_color_empire",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 40,

					"text" : uiScriptLocale.OPTION_NAME_COLOR_EMPIRE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				{
					"name" : "target_board",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 65+2,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD,
				},
				{
					"name" : "target_board_no_view",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 65,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD_NO_VIEW,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "target_board_view",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 65,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD_VIEW,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},


				## PvP Mode
				{
					"name" : "pvp_mode",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 90+2,

					"text" : uiScriptLocale.OPTION_PVPMODE,
				},
				{
					"name" : "pvp_peace",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*0,
					"y" : 90,

					"text" : uiScriptLocale.OPTION_PVPMODE_PEACE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_PEACE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_revenge",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*1,
					"y" : 90,

					"text" : uiScriptLocale.OPTION_PVPMODE_REVENGE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_REVENGE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_guild",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*2,
					"y" : 90,

					"text" : uiScriptLocale.OPTION_PVPMODE_GUILD,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_GUILD_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_free",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*3,
					"y" : 90,

					"text" : uiScriptLocale.OPTION_PVPMODE_FREE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_FREE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

				## Block
				{
					"name" : "block",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 115+2,

					"text" : uiScriptLocale.OPTION_BLOCK,
				},
				{
					"name" : "block_exchange_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 115,

					"text" : uiScriptLocale.OPTION_BLOCK_EXCHANGE,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_party_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 115,

					"text" : uiScriptLocale.OPTION_BLOCK_PARTY,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_guild_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 115,

					"text" : uiScriptLocale.OPTION_BLOCK_GUILD,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_whisper_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 140,

					"text" : uiScriptLocale.OPTION_BLOCK_WHISPER,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_friend_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 140,

					"text" : uiScriptLocale.OPTION_BLOCK_FRIEND,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_party_request_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 140,

					"text" : uiScriptLocale.OPTION_BLOCK_PARTY_REQUEST,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Chat
				{
					"name" : "chat",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 165+2,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT,
				},
				{
					"name" : "view_chat_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 165,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "view_chat_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 165,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Always Show Name
				{
					"name" : "always_show_name",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 190+2,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME,
				},
				{
					"name" : "always_show_name_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 190,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "always_show_name_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 190,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Effect On/Off
				{
					"name" : "effect_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 215+2,

					"text" : uiScriptLocale.OPTION_EFFECT,
				},
				{
					"name" : "show_damage_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 215,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "show_damage_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 215,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				{
					"name" : "salestext_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 240+2,

					"text" : uiScriptLocale.OPTION_SALESTEXT,
				},
				{
					"name" : "salestext_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 240,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "salestext_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 240,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Chat Filter
				{
					"name" : "chat_filter",
					"type" : "text",

					# "multi_line" : 1,

					"x" : LINE_LABEL_X,
					"y" : 265,

					"text" : uiScriptLocale.CHAT_FILTER,
				},
				{
					"name" : "chat_filter_dice",
					"type" : "toggle_button",

					"x" : LINE_DATA_X,
					"y" : 265,

					"text" : uiScriptLocale.CHAT_FILTER_DICE,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				{
					"name" : "chat_filter_gold",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 265,

					"text" : uiScriptLocale.CHAT_FILTER_YANG,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				{
					"name" : "offline_shop_filter",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH+65,
					"y" : 265,

					"text" : uiScriptLocale.CHAT_FILTER_SHOPS,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				{
					"name" : "show_companions_pets_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 290,

					"text" : uiScriptLocale.CHAT_FILTER_PETS,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				{
					"name" : "show_companions_mounts_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 290,

					"text" : uiScriptLocale.CHAT_FILTER_MOUNTS,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "option_frames",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH+65,
					"y" : 290,

					"text" : uiScriptLocale.CHAT_FILTER_FPS,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
			),
		},
	),
}

CUR_LINE_Y = LINE_BEGIN + LINE_STEP * 8

CUR_LINE_Y += LINE_STEP
window["height"] = window["height"] + 25
window["children"][0]["height"] = window["children"][0]["height"] + 25
window["children"][0]["children"] = window["children"][0]["children"] + (

					{
						"name": "drops_ignore",
						"type": "text",

						"multi_line" : 1,

						"x": LINE_LABEL_X,
						"y": CUR_LINE_Y+2,

						"text": uiScriptLocale.EXTENDED_PICKUP_IGNORE_LABEL,
					},


					{
						"name" : "drops_ignore_weapon",
						"type" : "toggle_button",

						"x" : LINE_DATA_X,
						"y" : CUR_LINE_Y,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_WEAPON_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},

					{
						"name" : "drops_ignore_armor",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
						"y" : CUR_LINE_Y,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_ARMOR_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},

					{
						"name" : "drops_ignore_head",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH+65,
						"y" : CUR_LINE_Y,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_HEAD_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "drops_ignore_wrist",
						"type" : "toggle_button",

						"x" : LINE_DATA_X,
						"y" : CUR_LINE_Y+25,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_WRIST_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "drops_ignore_foots",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
						"y" : CUR_LINE_Y+25,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_FOOTS_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},

					{
						"name" : "drops_ignore_neck",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH+65,
						"y" : CUR_LINE_Y+25,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_NECK_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},

					{
						"name" : "drops_ignore_ear",
						"type" : "toggle_button",

						"x" : LINE_DATA_X,
						"y" : CUR_LINE_Y+50,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_EAR_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "drops_ignore_shield",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
						"y" : CUR_LINE_Y+50,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_SHIELD_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "drops_ignore_etc",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH+65,
						"y" : CUR_LINE_Y+50,

						"text" : uiScriptLocale.EXTENDED_PICKUP_IGNORE_ETC_LABEL,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},)
