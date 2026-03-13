import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/game/"

window = {
	"name" : "InventoryMenu",

	"style" : ("movable", "float","animate",),

	"x" : SCREEN_WIDTH / 2,
	"y" : SCREEN_HEIGHT /2,

	"width" : 180,
	"height" : 134,

	"children" :
	(

		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 180,
			"height" : 134,
			"title" : uiScriptLocale.INVENTORY_MENU_TITLE,

			"children" :
			(

				{
					"name" : "menue_board",
					"type" : "thinboard_circle",

					"x" : 10,
					"y" : 37,

					"width" : 160,
					"height" : 87,

					"children" :
					(

						{
							"name" : "normal_storage",
							"type" : "button",

							"x" : 6,
							"y" : 4,

							"text" : uiScriptLocale.INVENTORY_MENU_NORMAL,

							"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
							"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
							"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",

						},

						{
							"name" : "itemshop_storage",
							"type" : "button",

							"x" : 6,
							"y" : 4 + 28,

							"text" : uiScriptLocale.INVENTORY_MENU_ITEMSHOP,

							"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
							"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
							"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
						},

						{
							"name" : "special_storage",
							"type" : "button",

							"x" : 6,
							"y" : 4 + 28 + 28,

							"text" : uiScriptLocale.INVENTORY_MENU_SPECIAL,

							"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
							"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
							"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
						},

					)
				},
			),
		},
	)
}
