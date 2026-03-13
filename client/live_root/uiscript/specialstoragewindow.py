import uiScriptLocale
import app

window = {
	"name" : "SpecialStorageWindow",

	"x" : SCREEN_WIDTH - 400,
	"y" : 10,

	"style" : ("movable", "float", "animate",),

	"width" : 184,
	"height" : 328+32+40,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 184,
			"height" : 328+32+40,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 46,
					"y" : 8,

					"width" : 131,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":62, "y":4, "text":"Depozit Special", "text_horizontal_align":"center" },
					),
				},

				{
					"name": "SortSpecialButton",
					"type": "button",

					"x": 8,
					"y": 7,

					"default_image": "d:/ymir work/ui/game/sort_inventory/default.sub",
					"over_image": "d:/ymir work/ui/game/sort_inventory/over.sub",
					"down_image": "d:/ymir work/ui/game/sort_inventory/down.sub"
				},

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 12,
					"y" : 34,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				{

					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 14,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},

				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 14 + 52,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},


				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 14 + 52 + 52,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},

				{
					"name" : "Category_Tab_01",
					"type" : "radio_button",

					"x" : 14,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/game/special_storage/Upgrade_apasat.tga",
					"over_image" : "d:/ymir work/ui/game/special_storage/Upgrade_apasat.tga",
					"down_image" : "d:/ymir work/ui/game/special_storage/Upgrade_neapasat.tga",


				},

				{
					"name" : "Category_Tab_02",
					"type" : "radio_button",

					"x" : 14+42,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/game/special_storage/licoare_neapasat.tga",
					"over_image" : "d:/ymir work/ui/game/special_storage/licoare_neapasat.tga",
					"down_image" : "d:/ymir work/ui/game/special_storage/licoare_apasat.tga",
				},

				{
					"name" : "Category_Tab_03",
					"type" : "radio_button",

					"x" : 14+42+42,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/game/special_storage/schimba_neapasat.tga",
					"over_image" : "d:/ymir work/ui/game/special_storage/schimba_neapasat.tga",
					"down_image" : "d:/ymir work/ui/game/special_storage/schimba_apasat.tga",
				},

				{
					"name" : "Category_Tab_04",
					"type" : "radio_button",

					"x" : 14+42+42+42,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/game/special_storage/cufere_apasat.tga",
					"over_image" : "d:/ymir work/ui/game/special_storage/cufere_apasat.tga",
					"down_image" : "d:/ymir work/ui/game/special_storage/cufere_neapasat.tga",
				},
			),
		},
	),
}