import app
ROOT_PATH = "%s/ui/new/loading/" % app.GetLocalePath()

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
			"name" : "BackGround",
			"type" : "ani_image",

			"x" : 0,
			"y" : 0,

			"images": ("%s%03d.dds" % (ROOT_PATH, i) for i in xrange(120)),
			"delay": 1,

			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
		},
	),
}
