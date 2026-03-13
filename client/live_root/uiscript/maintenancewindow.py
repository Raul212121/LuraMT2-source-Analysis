import uiScriptLocale

window = {
	"name" : "MaintenanceWindow",

	"x" : 390,
	"y" : 3,

	"style" : ("float",),

	"width" : 150,
	"height" : 3,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 390,
			"y" : 3,

			"width" : 390,
			"height" : 3,
			"horizontal_align" : "center",

			"children" :
			(
				{
					"name" : "desc",
					"type" : "extended_text",

					"x" : 0,
					"y" : 5,

					"horizontal_align" : "center",
				},
			),
		},
	),
}
