import uiScriptLocale

WINDOW_WIDTH = 543
WINDOW_HEIGHT = 285
def lang(lang):
	return lang

window = {
	"name": "RankingWindow",
	
	"x": 0,
	"y": 0,
	
	"style": ("movable", "float",),
	
	"width": WINDOW_WIDTH,
	"height": WINDOW_HEIGHT,
	
	"children":
	(
		{
			"name": "background",
			"type": "expanded_image",
			
			"x": 0,
			"y": 0,
			
			"style": ("not_pick",),
			
			"image": "d:/ymir work/ui/cw/ranking/board_ranking.tga",
		},

		{
			"name" : "TitleBar",
			"type" : "titlebar",
			"style" : ("attach",),

			"x" : 6,
			"y" : 6,

			"width" : 533,					
			"color" : "yellow",

			"children" :
			(
				{ "name":"TitleName", "type":"text", "x": 533 / 2, "y":3, "text": "Ranking", "text_horizontal_align":"center" },
			),
		},

		{
			"name": "category_list",
			"type": "listboxex",
			
			"x": 5,
			"y": 40,
			
			"horizontal_align" : "left",
			"vertical_align" : "top",
			
			"width": 40,
			"height": 360,
			
			"itemsize_x": 161,
			"itemsize_y": 39,
			
			"itemstep": 36,
			
			"viewcount": 6,
			
		},

				{
					"name": "rank",
					"type": "text",
					
					"x": 250 - 61,
					"y": 43,
					
					"text": lang("R"),
				},
				
				{
					"name": "name",
					"type": "text",
					
					"x": 215,
					"y": 43,
					
					"text": lang("Name"),
				},
				
				{
					"name": "guild",
					"type": "text",
					
					"x": 300,
					"y": 43,
					
					"text": lang("Guild"),
				},
				
				{
					"name": "empire",
					"type": "text",
					
					"x": 375,
					"y": 43,
					
					"text": lang("Empire"),
				},
				
				{
					"name": "count",
					"type": "text",
					
					"x": 470,
					"y": 43,
					
					"text": lang("Count"),
				},

		{
			"name": "rank_list",
			"type": "listboxex",
			
			"x": 175,
			"y": 60,
			
			"horizontal_align" : "left",
			"vertical_align" : "top",
			
			"width": 305,
			"height": 350,
			
			#"itemsize_x": 423,
			#"itemsize_y": 28,
			
			"itemstep": 18,
			
			"viewcount": 10,
			
		},

		{
			"name" : "category_scroll",
			"type" : "scrollbar_new",

			"x" : 161,
			"y" : 42,
			
			"horizontal_align" : "left",
			"vertical_align" : "top",
			
			"bg_image": "d:/ymir work/ui/cw/ranking/scrollbar_bg.png",

			"size" : 229,
		},

		{
			"name": "player_rank",
			"type": "expanded_image",
			
			"x": 174,
			"y": 248,
			
			"style": ("not_pick",),
			
			"horizontal_align" : "left",
			"vertical_align" : "top",
			
			"image": "d:/ymir work/ui/cw/ranking/personal.tga",
			
			"children":(
				{
					"name": "rankPlayer",
					"type": "text",
					
					"x": 17,
					"y": -7,
					
					"horizontal_align" : "left",
					"vertical_align" : "center",
					
					"text": lang("-"),
				},
				
				{
					"name": "namePlayer",
					"type": "text",
					
					"x": 37,
					"y": -7,
					
					"horizontal_align" : "left",
					"vertical_align" : "center",
					
					"text": lang("-"),
				},
				
				{
					"name": "guildPlayer",
					"type": "text",
					
					"x": 132,
					"y": -7,
					
					"horizontal_align" : "left",
					"vertical_align" : "center",
					
					"text": lang("-"),
				},
				
				{
					"name": "empirePlayer",
					"type": "expanded_image",
					
					"x": 205,
					"y": 2,
					
					"horizontal_align" : "left",
					"vertical_align" : "center",
					
					"image": ("d:/ymir work/ui/cw/ranking/table/1.png"),
				},
				
				{
					"name": "countPlayer",
					"type": "text",
					
					"x": 344,
					"y": 0,
					"text": lang("-"),
				},
				
			),
		},
	)
}
