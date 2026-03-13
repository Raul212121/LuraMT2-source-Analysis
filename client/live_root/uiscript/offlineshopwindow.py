import localeInfo
import app

ROOT = "offlineshop/loading/"

WINDOW_WIDTH	= 624
WINDOW_HEIGHT	= 572

window = {
	"name" : "OfflineshopBoard",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2  - WINDOW_WIDTH/2,
	"y" : SCREEN_HEIGHT/2  - WINDOW_HEIGHT/2,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "MainBoard",
			"type" : "board",

			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" 	: WINDOW_WIDTH,
			"height" 	: WINDOW_HEIGHT,

			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",

					"x" : 8,
					"y" : 7,

					"width"  : WINDOW_WIDTH - 16,
					"color"  : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":"", "all_align":"center" },
					),
				},

				{
					"name" : "MyShopBoardNoShop",
					"type" : "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name" : "BackGroundCreate",
							"type" : "image",

							"x" : 0, "y" : 0,
							"image": "offlineshop/createshop/base_image_1.png",

						},

						{
							"name" : "ShopNameInput",
							"type" : "editline",

							"width" : 217 , "height" : 15 ,

							"input_limit" : 35,
							"x" : 205, "y" : 34,
						},

						{
							"name" : "DaysCountText",
							"type" : "text",

							"text" : "0",
							"text_horizontal_align" : "center",
							"x" : 255, "y" :89,
						},

						{
							"name" : "HoursCountText",
							"type" : "text",

							"text" : "0",
							"text_horizontal_align" : "center",
							"x" : 367, "y" : 89,
						},

						{
							"name" : "IncreaseDaysButton",
							"type" : "button",


							"x" : 291-10,
							"y" : 91,

							"default_image" : "offlineshop/scrollbar/horizontal/button2_default.png",
							"over_image" 	: "offlineshop/scrollbar/horizontal/button2_over.png",
							"down_image" 	: "offlineshop/scrollbar/horizontal/button2_down.png",
						},

						{
							"name" : "DecreaseDaysButton",
							"type" : "button",

							"x" : 218,
							"y" : 91,

							"default_image" : "offlineshop/scrollbar/horizontal/button1_default.png",
							"over_image" 	: "offlineshop/scrollbar/horizontal/button1_over.png",
							"down_image" 	: "offlineshop/scrollbar/horizontal/button1_down.png",
						},

						{
							"name" : "IncreaseHoursButton",
							"type" : "button",

							"x" : 400-8,
							"y" : 91,

							"default_image" : "offlineshop/scrollbar/horizontal/button2_default.png",
							"over_image" 	: "offlineshop/scrollbar/horizontal/button2_over.png",
							"down_image" 	: "offlineshop/scrollbar/horizontal/button2_down.png",
						},

						{
							"name" : "DecreaseHoursButton",
							"type" : "button",

							"x" : 330-3,
							"y" : 91,

							"default_image" : "offlineshop/scrollbar/horizontal/button1_default.png",
							"over_image" 	: "offlineshop/scrollbar/horizontal/button1_over.png",
							"down_image" 	: "offlineshop/scrollbar/horizontal/button1_down.png",
						},

						{
							"name" : "CreateShopButton",
							"type" : "button",

							"x" : 249 + 40,
							"y" : 482 - 8,

							"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CREATE_TEXT,
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 298,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 291,
							"y" : 53,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 244,
							"y" : 70,

							"text" : localeInfo.OFFLINESHOP_DAYS_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 352,
							"y" : 70,

							"text" : localeInfo.OFFLINESHOP_HOURS_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 262,
							"y" : 455,

							"text" : localeInfo.OFFLINESHOP_MAX_DURATION_TEXT,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_MYSHOP, "all_align":"center" },
## END
					),
				},

				{
					"name" : "MyShopBoard",
					"type" : "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name" : "BackgroundMySHop",
							"type" : "image",

							"x" : 0, "y" : 0,

							"image" : "offlineshop/myshop/base_image_0.png",
						},

						{
							"name" : "MyShopShopTitle",
							"type" : "text",

							"x" : 310, "y" : 3,

							"text" : "title",
							"text_horizontal_align" : "center",
						},

						{
							"name" : "MyShopEditTitleButton",
							"type" : "button",

							"x" : 425, "y" : 9,

							"tooltip_text"	: localeInfo.OFFLINESHOP_EDIT_SHOPNAME_TOOLTIP,

							"default_image" : "offlineshop/myshop/editname_default.png",
							"over_image" 	: "offlineshop/myshop/editname_over.png",
							"down_image" 	: "offlineshop/myshop/editname_down.png",
						},

						{
							"name" : "MyShopShopDuration",
							"type" : "text",

							"x" : 310, "y" : 24,

							"text" : "99 days",
							"text_horizontal_align" : "center",
						},

						{
							"name" : "MyShopCloseButton",
							"type" : "button",

							"x" : 15, "y" : 5,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CLOSE_SHOP_TEXT,
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 150,
							"y" : 2,

							"text" : localeInfo.OFFLINESHOP_TITLE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 150,
							"y" : 21,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 65,
							"y" : 377,

							"text" : localeInfo.OFFLINESHOP_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 245,
							"y" : 377,

							"text" : localeInfo.OFFLINESHOP_ITEM_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 410,
							"y" : 377,

							"text" : localeInfo.OFFLINESHOP_OFFER_TEXT,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_MYSHOP, "all_align":"center" },
## END

					),
				},

				{
					"name" : "ListOfShop_OpenShop",
					"type" : "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name" : "BackgroundShopListOpen",
							"type" : "image",

							"x" : 0, "y" : 0,

							"image" : "offlineshop/shoplist/base_image_open.png",
						},

						{
							"name" : "OpenShopShopTitle",
							"type" : "text",

							"x" : 310, "y" : 3,

							"text_horizontal_align" : "center",
							"text" : "title",
						},

						{
							"name" : "OpenShopShopDuration",
							"type" : "text",

							"x" : 310, "y" : 24,

							"text_horizontal_align" : "center",
							"text" : "99 days",
						},

## FLR_CHANGES
						{
							"name" : "OpenShopBackToListButton",
							"type" : "button",

							"x" : 15, "y" : 5,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_BACK_TO_LIST_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 150,
							"y" : 2,

							"text" : localeInfo.OFFLINESHOP_TITLE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 150,
							"y" : 21,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_LIST_OF_SHOPS, "all_align":"center" },
## END
					),
				},

				{
					"name" : "ListOfShop_List",
					"type" : "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,
					"children":
					(
						{
							"name" : "BackgroundShopList",
							"type" : "image",

							"x" : 0, "y" : 0,

							"image" : "offlineshop/shoplist/base_image_list.png",
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 45,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_OWNER_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 196,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_SHOPS_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 362,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 480,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_ITEMS_COUNT_TEXT_1,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_LIST_OF_SHOPS, "all_align":"center" },
## END

					),
				},

				{
					"name" : "SearchHistoryBoard",
					"type" : "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,
					"children":
					(
						{
							"name" : "BackgroundSearchHistory",
							"type" : "image",

							"x" : 0, "y" : 0,

							"image" : "offlineshop/searchhistory/base_image.png",
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 92,
							"y" : 16,

							"text" : localeInfo.OFFLINESHOP_DATE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 282,
							"y" : 16,

							"text" : localeInfo.OFFLINESHOP_TIME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 473,
							"y" : 16,

							"text" : localeInfo.OFFLINESHOP_ITEMS_COUNT_TEXT_1,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_SEARCH_HISTORY, "all_align":"center" },
## END

					),
				},

				{
					"name" : "MyPatternsBoard",
					"type" : "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,
					"children":
					(
						{
							"name" : "BackgroundMyPatterns",
							"type" : "image",

							"x" : 0, "y" : 0,

							"image" : "offlineshop/mypatterns/base_image.png",
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 35,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 393,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_LAST_USE_TEXT,
						},


## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_MY_PATTERNS, "all_align":"center" },
## END

					),
				},

				{
					"name" : "SearchFilterBoard",
					"type" : "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,
					"children":
					(
						{
							"name" : "BackgroundSearchFilter",
							"type" : "image",

							"x" : 0, "y" : 0,

							"image" : "offlineshop/searchfilter/base_image.png",
						},

						{
							"name" : "SearchFilterItemNameInput",
							"type" : "editline",

							"width" : 150, "height" : 15,

							"input_limit" : 24,
							"x" : 80, "y" : 31,
						},

						{
							"name" : "SearchFilterItemLevelStart",
							"type" : "editline",

							"width" : 43, "height" : 14,

							"input_limit" : 3,
							"only_number" : 1,
							"x" : 363, "y" : 32,
						},

						{
							"name" : "SearchFilterItemLevelEnd",
							"type" : "editline",

							"width" : 43, "height" : 14,

							"input_limit" : 3,
							"only_number" : 1,
							"x" : 363, "y" : 52,
						},

						{
							"name" : "SearchFilterItemYangMin",
							"type" : "editline",

							"width" : 130, "height" : 15,

							"input_limit" : len("999999999999999999"),
							"only_number" : 1,
							"x" : 258, "y" : 103,
						},



						{
							"name" : "SearchFilterItemYangMax",
							"type" : "editline",

							"width" : 130, "height" : 15,

							"input_limit" : len("999999999999999999"),
							"only_number" : 1,
							"x" : 258, "y" : 127,
						},

						{
							"name" : "SearchFilterResetFilterButton",
							"type" : "button",

							"x" : 400, "y" : 487,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_RESET_FILTER_TEXT,
						},

						{
							"name" : "SearchFilterSavePatternButton",
							"type" : "button",

							"x" : 139, "y" : 487,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_SAVE_AS_PATTERN_TEXT,
						},

						{
							"name" : "SearchFilterStartSearch",
							"type" : "button",

							"x" : 268, "y" : 487,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_START_SEARCH_TEXT,
						},

						{
							"name" : "SearchFilterAttributeButton1",
							"type" : "button",

							"x" : 406, "y" : 35,

							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},

						{
							"name" : "SearchFilterAttributeButton2",
							"type" : "button",

							"x" : 406, "y" : 35+22,

							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},

						{
							"name" : "SearchFilterAttributeButton3",
							"type" : "button",

							"x" : 406, "y" : 35+22*2,

							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},

						{
							"name" : "SearchFilterAttributeButton4",
							"type" : "button",

							"x" : 406, "y" : 35+22*3,

							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},

						{
							"name" : "SearchFilterAttributeButton5",
							"type" : "button",

							"x" : 406, "y" : 35+22*4,

							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 37,
							"y" : 10,

							"text" : localeInfo.OFFLINESHOP_ITEM_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 238,
							"y" : 10,

							"text" : localeInfo.OFFLINESHOP_TYPE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 355,
							"y" : 10,

							"text" : "Level:",
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 421,
							"y" : 10,

							"text" : localeInfo.OFFLINESHOP_ATTR_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 17,
							"y" : 31,

							"text" : localeInfo.OFFLINESHOP_INPUT_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 17,
							"y" : 52,

							"text" : localeInfo.OFFLINESHOP_SUGGESTIONS_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 37,
							"y" : 84,

							"text" : localeInfo.OFFLINESHOP_RACE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 110,
							"y" : 94,

							"text" : "Warrior",
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 110 + 63,
							"y" : 94,

							"text" : "Sura",
						},

#						{
#							"name" : "FlrText",
#							"type" : "text",
#
#							"x" : 110 - 66,
#							"y" : 94 + 26,
#
#							"text" : "Wolfman",
#						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 111,
							"y" : 94 + 26,

							"text" : "Ninja",
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 110 + 63,
							"y" : 94 + 26,

							"text" : "Shaman",
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 241,
							"y" : 84,

							"text" : localeInfo.OFFLINESHOP_PRICE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 110 + 117,
							"y" : 103,

							"text" : "Min:",
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 110 + 117,
							"y" : 103 + 23,

							"text" : "Max:",
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_SEARCH, "all_align":"center" },
## END

					),
				},

				{
					"name": "ShopSafeboxPage",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,
					"children":
					(
						{
							"name": "BackgroundShopSafeboxPage",
							"type": "image",

							"x": 0, "y": 0,

							"image": "offlineshop/safebox/safebox_base_image.png",
						},

						{
							"name" : "ShopSafeboxWithdrawYangButton",
							"type" : "button",

							"x" : 447-205,
							"y" : 16-4,

							"default_image" : "offlineshop/safebox/withdrawyang_default.png",
							"over_image" 	: "offlineshop/safebox/withdrawyang_over.png",
							"down_image" 	: "offlineshop/safebox/withdrawyang_down.png",
						},

						{
							"name" : "ShopSafeboxValuteText",
							"type" : "text",

							"x" : 468-154,
							"y" : 22-8,

							"text_horizontal_align" : "center",
							"text" : "000000",
						},
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_SAFEBOX, "all_align":"center" },
## END
					),
				},

				{
					"name": "MyOffersPage",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name": "BackgroundMyOffersPage",
							"type": "image",

							"x": 0, "y": 0,

							"image": "offlineshop/myoffers/base_image.png",
						},
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_MY_OFFERS, "all_align":"center" },
## END
					),
				},

				{
					"name": "MyAuction",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name": "BackgroundMyAuctionPage",
							"type": "image",

							"x": 0, "y": 0,

							"image": "offlineshop/myauction/base_image.png",
						},

						{
							"name" : "MyAuction_OwnerName",
							"type" : "text",

							"x" : 235+67, "y" : 100-70,
							"text_horizontal_align" : "center",
							"text" : " noname ",
						},

						{
							"name" : "MyAuction_Duration",
							"type" : "text",

							"x" : 235+67, "y" : 145-91,
							"text_horizontal_align" : "center",
							"text" : " noname ",
						},

						{
							"name" : "MyAuction_BestOffer",
							"type" : "text",

							"x" : 235+67, "y" : 197-123,
							"text_horizontal_align" : "center",
							"text" : " noname ",
						},

						{
							"name": "MyAuction_MinRaise",
							"type": "text",

							"x": 235+67, "y": 243-147,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 29,

							"text" : localeInfo.OFFLINESHOP_OWNER_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 25 + 27,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 25 + 49,

							"text" : localeInfo.OFFLINESHOP_BEST_OFFER_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 25 + 72,
							"text" : localeInfo.OFFLINESHOP_MIN_RAISE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 191,
							"y" : 145,

							"text" : localeInfo.OFFLINESHOP_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 410,
							"y" : 145,

							"text" : localeInfo.OFFLINESHOP_OFFER_TEXT,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_MY_AUCTION, "all_align":"center" },
## END

					),
				},

				{
					"name": "OpenAuction",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name": "BackgroundOpenAuctionPage",
							"type": "image",

							"x": 0, "y": 0,

							"image": "offlineshop/openauction/base_image.png",
						},

						{
							"name": "OpenAuction_OwnerName",
							"type": "text",

							"x" : 235+67, "y" : 100-70,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

						{
							"name": "OpenAuction_Duration",
							"type": "text",

							"x" : 235+67, "y" : 145-91,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

						{
							"name": "OpenAuction_BestOffer",
							"type": "text",

							"x": 235+67, "y": 197-123,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

						{
							"name": "OpenAuction_MinRaise",
							"type": "text",

							"x": 235+67, "y": 243-147,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 29,

							"text" : localeInfo.OFFLINESHOP_OWNER_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 25 + 27,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 25 + 49,

							"text" : localeInfo.OFFLINESHOP_BEST_OFFER_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 165,
							"y" : 25 + 72,
							"text" : localeInfo.OFFLINESHOP_MIN_RAISE_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 191,
							"y" : 145,

							"text" : localeInfo.OFFLINESHOP_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 410,
							"y" : 145,

							"text" : localeInfo.OFFLINESHOP_OFFER_TEXT,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_AUCTION_LIST, "all_align":"center" },
## END

					),
				},

				{
					"name": "AuctionList",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name": "BackgroundAuctionListPage",
							"type": "image",

							"x": 0, "y": 0,

							"image": "offlineshop/auctionlist/base_image.png",
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 76,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_OWNER_NAME_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 218,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_BEST_OFFER_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 347,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x" : 477,
							"y" : 15,

							"text" : localeInfo.OFFLINESHOP_OFFER_COUNT_TEXT,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_AUCTION_LIST, "all_align":"center" },
## END

					),
				},

				{
					"name": "CreateAuction",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 28,

					"children":
					(
						{
							"name": "BackgroundCreateAuctionPage",
							"type": "image",

							"x": 0, "y": 0,

							"image": "offlineshop/createauction/base_image.png",
						},

						{
							"name": "CreateAuctionDaysInput",
							"type": "text",

							"width": 23, "height": 17,

							"text_horizontal_align" : "center",
							"text" : "0",
							"x": 299, "y": 181,
						},

						{
							"name": "CreateAuctionStartingPriceInput",
							"type": "editline",

							"width": 122, "height": 15,

							"input_limit": 18,
							"only_number": 1,
							"x": 272, "y": 210,
						},

						{
							"name": "CreateAuctionDecreaseDaysButton",
							"type": "button",

							"x": 325,
							"y": 183,

							"default_image": "offlineshop/scrollbar/horizontal/button2_default.png",
							"over_image" : "offlineshop/scrollbar/horizontal/button2_over.png",
							"down_image" 	: "offlineshop/scrollbar/horizontal/button2_down.png",
						},

						{
							"name" : "CreateAuctionIncreaseDaysButton",
							"type" : "button",

							"x" : 267-2,
							"y" : 183,

							"default_image" : "offlineshop/scrollbar/horizontal/button1_default.png",
							"over_image" 	: "offlineshop/scrollbar/horizontal/button1_over.png",
							"down_image" 	: "offlineshop/scrollbar/horizontal/button1_down.png",
						},

						{
							"name" : "CreateAuctionCreateAuctionButton",
							"type" : "button",

							"x" : 211+98, "y" : 267-33,

							"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CREATE_TEXT,
						},

## FLR_CHANGES
						{
							"name" : "FlrText",
							"type" : "text",

							"x": 288, "y": 165,

							"text" : localeInfo.OFFLINESHOP_DAYS_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x": 187, "y": 181,

							"text" : localeInfo.OFFLINESHOP_DURATION_TEXT,
						},

						{
							"name" : "FlrText",
							"type" : "text",

							"x": 187, "y": 208,

							"text" : localeInfo.OFFLINESHOP_STARTING_PRICE_TEXT,
						},
## END
## FLR_CHANGES_BUTTONS
						{
							"name" : "my_shop_btn",
							"type" : "button",

							"x" : 16, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_shop.png",
							"over_image" : "offlineshop/_flr_rework/my_shop1.png",
							"down_image" : "offlineshop/_flr_rework/my_shop1.png",

							"text" : "",
						},

						{
							"name" : "list_of_shops_btn",
							"type" : "button",

							"x" : 15 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/list_of_shops.png",
							"over_image" : "offlineshop/_flr_rework/list_of_shops1.png",
							"down_image" : "offlineshop/_flr_rework/list_of_shops1.png",

							"text" : "",
						},

						{
							"name" : "safebox_btn",
							"type" : "button",

							"x" : 15 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/safebox.png",
							"over_image" : "offlineshop/_flr_rework/safebox1.png",
							"down_image" : "offlineshop/_flr_rework/safebox1.png",

							"text" : "",
						},

						{
							"name" : "my_offers_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_offers.png",
							"over_image" : "offlineshop/_flr_rework/my_offers1.png",
							"down_image" : "offlineshop/_flr_rework/my_offers1.png",

							"text" : "",
						},

						{
							"name" : "search_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/search.png",
							"over_image" : "offlineshop/_flr_rework/search1.png",
							"down_image" : "offlineshop/_flr_rework/search1.png",

							"text" : "",
						},

						{
							"name" : "history_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/history.png",
							"over_image" : "offlineshop/_flr_rework/history1.png",
							"down_image" : "offlineshop/_flr_rework/history1.png",

							"text" : "",
						},

						{
							"name" : "my_patterns_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_patterns.png",
							"over_image" : "offlineshop/_flr_rework/my_patterns1.png",
							"down_image" : "offlineshop/_flr_rework/my_patterns1.png",

							"text" : "",
						},

						{
							"name" : "my_auction_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/my_auction.png",
							"over_image" : "offlineshop/_flr_rework/my_auction1.png",
							"down_image" : "offlineshop/_flr_rework/my_auction1.png",

							"text" : "",
						},

						{
							"name" : "auction_list_btn",
							"type" : "button",

							"x" : 15 + 70 + 70 + 70 + 70 + 70 + 70 + 70 + 70, "y" : 509,

							"default_image" : "offlineshop/_flr_rework/auction_list.png",
							"over_image" : "offlineshop/_flr_rework/auction_list1.png",
							"down_image" : "offlineshop/_flr_rework/auction_list1.png",

							"text" : "",
						},
## END
## FLR_CHANGES_TEXTS
						{ "name":"TitleName", "type":"text", "x":0, "y":-285, "text" : localeInfo.OFFLINESHOP_TITLE_CREATE_AUCTION, "all_align":"center" },
## END
					),
				},

				{
					"name": "Menu",
					"type": "window",

					"x": 0,
					"y": WINDOW_HEIGHT-35,

					"width" : WINDOW_WIDTH,
					"height": 35,
					"children":
					(
						{
							"name": "MyShopButton",
							"type": "button",

							"x": 3, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "ListOfShopButton",
							"type": "button",

							"x": 3 + 78, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "ShopSafeboxButton",
							"type": "button",

							"x": 3 +141, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "MyOffersPageButton",
							"type": "button",

							"x": 3 + 213, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "SearchFilterButton",
							"type": "button",

							"x": 3 + 281, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "SearchHistoryButton",
							"type": "button",

							"x": 3+351, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "MyPatternsButton",
							"type": "button",

							"x": 3+418, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "MyAuctionButton",
							"type": "button",

							"x": 3 + 486, "y": 7,

							"width" : 66,
							"height": 21,
						},

						{
							"name": "ListOfAuctionsButton",
							"type": "button",

							"x": 3 + 555, "y": 7,

							"width" : 66,
							"height": 21,
						},
					),
				},

				{
					"name" : "RefreshSymbol",
					"type" : "ani_image",

					"x" : -27, "y" : -15,

					"vertical_align" : "center",
					"horizontal_align" : "center",

					"delay" : 2.5,

					"images" :
					(
						ROOT + "img0001.png",
						ROOT + "img0002.png",
						ROOT + "img0003.png",
						ROOT + "img0004.png",
						ROOT + "img0005.png",
						ROOT + "img0006.png",
						ROOT + "img0007.png",
						ROOT + "img0008.png",
						ROOT + "img0009.png",
						ROOT + "img0010.png",
						ROOT + "img0011.png",
						ROOT + "img0012.png",
						ROOT + "img0013.png",
						ROOT + "img0014.png",
						ROOT + "img0015.png",
						ROOT + "img0016.png",
						ROOT + "img0017.png",
						ROOT + "img0018.png",
						ROOT + "img0019.png",
						ROOT + "img0020.png",
						ROOT + "img0021.png",
						ROOT + "img0022.png",
						ROOT + "img0023.png",
						ROOT + "img0024.png",
						ROOT + "img0025.png",
						ROOT + "img0026.png",
						ROOT + "img0027.png",
						ROOT + "img0028.png",
						ROOT + "img0029.png",
						ROOT + "img0030.png",
						ROOT + "img0031.png",
					)
				},
			),
		},
	),
}