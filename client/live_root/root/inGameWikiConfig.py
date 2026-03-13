import localeInfo, app, player

#/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\
#/!\/!\/!\ CATEGORIES && SUB CATEGORIES MANAGEMENTS /!\/!\/!\
dictMobs =  {
	2206 : 'Tara de Foc',
	2191 : 'Desertul Yongbi',
	2091 : 'Temnita Paianjenilor 1',
	1901 : 'Muntele Sohan',
	1191 : 'Grota Exilului 3',
	792 : 'Templul Hwang (Turnul Demonilor)',
	693 : 'Pestera Malefica',
	691 : 'Valea Seungryong',
	591 : 'Satul II Jinno, Chunjo si Shinsoo',
	61009 : 'Barlogul lui Alastor',
	2598 : 'Catacomba Diavolului',
	2493 : 'Camera lui Beran Setaou',
	1093 : 'Turnul Demonilor',
	6191 : 'Turnul lui Nemere',
	6091 : 'Purgatoriul Iadului',
	3791 : 'Mapele Beta, Thunder',
	3790 : 'Mapele Beta, Thunder',
	3691 : 'Mapele Beta, Peninsula',
	3690 : 'Mapele Beta, Nephrite',
	3491 : 'Mapele Beta, Nephrite',
	3391 : 'Mapele Beta, Guatama',
	3390 : 'Mapele Beta, Guatama',
	3291 : 'Mapele Beta, Peninsula',
	3290 : 'Mapele Beta, Peninsula',
	3191 : 'Mapele Beta, Thunder',
	3090 : 'Mapele Beta, Peninsula',
	8024 : 'Tara Gigantilor',
	8014 : 'Tara de Foc, Turnul Demonilor',
	8018 : 'Muntele Sohan, Turnul Demonilor',
	8012 : 'Templul Hwang, Turnul Demonilor',
	8011 : 'Muntele Sohan, Turnul Demonilor',
	8015 : 'Desertul Yongbi',
	8009 : 'Desertul Yongbi, Valea Seungryong',
	8008 : 'Desertul Yongbi',
	8007 : 'Satul II Jinno, Chunjo si Shinsoo',
	8006 : 'Satul II Jinno, Chunjo si Shinsoo',
	8005 : 'Satul I si II Jinno, Chunjo si Shinsoo',
	8004 : 'Satul I Jinno, Chunjo si Shinsoo',
	8003 : 'Satul I Jinno, Chunjo si Shinsoo',
	8002 : 'Satul I Jinno, Chunjo si Shinsoo',
	8001 : 'Satul I Jinno, Chunjo si Shinsoo',
	8051 : 'Mapele Beta, Peninsula',
	8027 : 'Padurea Rosie',
	8026 : 'Padurea Rosie',
	8025 : 'Padurea Fantomelor, Tara Gigantilor',
	8056 : 'Mapele Beta, Guatama',
	8055 : 'Mapele Beta, Thunder',
	8054 : 'Mapele Beta, Guatama',
	8053 : 'Mapele Beta, Nephrite',
	8013 : 'Muntele Sohan, Turnul Demonilor',
	8010 : 'Muntele Sohan, Turnul Demonilor',
	1304 : 'Templul Hwang',
	2492 : 'Grota Exilului 4',
	2092 : 'Barlogul Baronesei',
	491 : 'Satul II Jinno, Chunjo si Shinsoo',
	492 : 'Satul II Jinno, Chunjo si Shinsoo',
	493 : 'Satul II Jinno, Chunjo si Shinsoo',
	494 : 'Satul II Jinno, Chunjo si Shinsoo',
	5163 : 'Temnita Maimutelor Expert',
	3891 : "Mapele Beta, Guatama",
}


dictItems =  {
	50130 : 'Toti bossii mici incepand cu Orc Sef',
	50128 : 'Azrael, Dragonul Albastru, Alastor, Razador, Nemere, Regina Paianjenilor',
	38052 : 'Razador, Nemere, Orc Malefic',
	30895 : 'Dungeon-ul de Craciun',
	50249 : 'Evenimentul OX',
	25364 : 'Evenimentul de Pescuit',
	25365 : 'Evenimentul de Pescuit',
	25366 : 'Evenimentul de Pescuit',
	50117 : 'Dungeon-ul de Paste',
	25622 : 'Dungeon-ul de Vara',
	50215 : 'Evenimentul de Halloween',
	30896 : 'Dungeon-ul de Craciun',
	30893 : 'Dungeon-ul de Craciun',
	50011 : 'Evenimentul Cuferelor Lumina Lunii',
	50125 : 'Toate Pietrele Metin',
	50131 : 'Toate Pietrele Metin',
	50127 : 'Toate Pietrele Metin',
	50109 : 'Completare I misiune a Biologului',
	50110 : 'Completare a II-a misiune a Biologului',
	50111 : 'Completare a III-a misiune a Biologului',
	50112 : 'Completare a IV-a misiune a Biologului',
	50113 : 'Completare a V-a misiune a Biologului',
	50114 : 'Completare a VI-a misiune a Biologului',
	38050 : 'Evenimentul de Craciun',
}
BOSS_CHEST_VNUMS = [50130, 50128, 38052]
EVENT_CHEST_VNUMS = [38050, 30895, 50249, 25364, 25365, 25366, 50117, 25622, 50215, 30896, 30893, 50011, 50124]
ALT_CHEST_VNUMS = [50125, 50131, 50127, 50131, 50109, 50110, 50111, range(50112, 50115)]
COSTUME_WEAPON_VNUMS = [24420, 24421, 24422, 24423, 24424, 24425, 25303, 25304, 25305, 25306, 25307, 25308, 25309, 25408, 25409, 25251, 25252, 25253, 25254, 25255, 25256, 25257, 42000, 42001, 42002, 42003, 42004, 42005, 42006, 42010, 42011, 42012, 42013, 42014, 42015, 42016, 42030, 42031, 42032, 42033, 42034, 42035, 42036, 42040, 42041, 42042, 42043, 42044, 42045, 42046, 42050, 42051, 42052, 42053, 42054, 42055, 42056, 42100, 42101, 42102, 42103, 42104, 42105, 42106, 42107]
COSTUME_ARMOR_VNUMS = [25746, 25747, 25596, 25597, 25276, 25280, 25537, 25538, 25505, 25506, 25549, 25548, 24521, 24522, 25281, 25282, 25292, 25293, 25404, 25405, 24408, 24409, 25393, 25394, 24408, 24409, 24406, 24407, 25329, 25330, 25325, 25326, 25353, 25354, 25193, 25194, 25167, 25168, 25175, 25176, 25169, 25170, 25128, 25129, 25229, 25230, 25189, 25190, 25137, 25138, 25124, 25125, 25008, 25009, 25029, 25030, 25004, 25005, 41307, 41308, 41324, 41325, 41311, 41312, 41203, 41204, 25000, 25001, 25106, 25107, 41315, 41316, 25237, 25238]
COSTUME_HAIR_VNUMS = [25748, 25749, 25539, 25540, 25507, 25508, 25556, 25557, 24523, 24524, 25283, 25284, 25294, 25295, 25406, 25407, 25395, 25396, 24412, 24413, 24410, 24411, 25331, 25332, 25327, 25328, 25355, 25356, 25195, 25196, 25171, 25172, 25177, 25178, 25173, 25174, 25130, 25131, 25231, 25232, 25191, 25192, 25139, 25140, 25127, 25126, 25025, 25026, 45061, 45062, 25014, 25015, 45135, 45136, 45160, 45161, 45147, 45148, 45055, 45056, 25031, 25032, 45151, 45152, 45009, 45014, 25241, 25242]
COSTUME_PET_VNUMS = [25623, 25624, 24434, 24435, 25420, 25372, 25373, 30898, 30897, 53031, 53030, 53021, 53020, 53018, 53019, 53017, 53003, 53001, 38201, 53006, 53008, 53518, 53010]
COSTUME_MOUNT_VNUMS = [25625, 25626, 24436, 25421, 25371, 25370, 25220, 25221, 71193, 71192, 71172, 71124, 71128, 71125]

if app.INGAME_WIKI_WOLFMAN:
	COSTUME_WEAPON_VNUMS.extend([40107])

WIKI_CATEGORIES = [
	[
		localeInfo.WIKI_CATEGORY_EQUIPEMENT,
		[
			[localeInfo.WIKI_SUBCATEGORY_WEAPONS, (0,), "d:/ymir work/ui/wiki/banners/banner_weapons.tga"],
			[localeInfo.WIKI_SUBCATEGORY_ARMOR, (1,), "d:/ymir work/ui/wiki/banners/armor.tga"],
			[localeInfo.WIKI_SUBCATEGORY_HELMET, (4,), "d:/ymir work/ui/wiki/banners/helmets.tga"],
			[localeInfo.WIKI_SUBCATEGORY_SHIELD, (6,), "d:/ymir work/ui/wiki/banners/shield.tga"],
			[localeInfo.WIKI_SUBCATEGORY_EARRINGS, (2,), "d:/ymir work/ui/wiki/banners/earrings.tga"],
			[localeInfo.WIKI_SUBCATEGORY_BRACELET, (7,), "d:/ymir work/ui/wiki/banners/bracelests.tga"],
			[localeInfo.WIKI_SUBCATEGORY_NECKLACE, (5,), "d:/ymir work/ui/wiki/banners/neck.tga"],
			[localeInfo.WIKI_SUBCATEGORY_SHOES, (3,), "d:/ymir work/ui/wiki/banners/shoes.tga"],
			[localeInfo.WIKI_SUBCATEGORY_BELTS, (9,), "d:/ymir work/ui/wiki/banners/belts.tga"],
		]
	],
	[
		localeInfo.WIKI_CATEGORY_CHESTS,
		[
			[localeInfo.WIKI_SUBCATEGORY_CHESTS, (BOSS_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/bosschests.tga"],
			[localeInfo.WIKI_SUBCATEGORY_EVENT_CHESTS, (EVENT_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/eventchests.tga"],
			[localeInfo.WIKI_SUBCATEGORY_ALTERNATIVE_CHESTS, (ALT_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/altchests.tga"]
		]
	],
	[
		localeInfo.WIKI_CATEGORY_BOSSES,
		[
			[localeInfo.WIKI_SUBCATEGORY_LV1_75, (0, 1, 76), "d:/ymir work/ui/wiki/banners/bosses.tga"],
			[localeInfo.WIKI_SUBCATEGORY_LV76_100, (0, 76, 100), "d:/ymir work/ui/wiki/banners/bosses.tga"],
			[localeInfo.WIKI_SUBCATEGORY_LV100, (0, 100, 255), "d:/ymir work/ui/wiki/banners/bosses.tga"]
		]
	],
	[
		localeInfo.WIKI_CATEGORY_MONSTERS,
		[
			[localeInfo.WIKI_SUBCATEGORY_LV1_75, (1, 1, 76), "d:/ymir work/ui/wiki/banners/monster.tga"],
			[localeInfo.WIKI_SUBCATEGORY_LV76_100, (1, 76, 100), "d:/ymir work/ui/wiki/banners/monster.tga"],
			[localeInfo.WIKI_SUBCATEGORY_LV100, (1, 100, 255), "d:/ymir work/ui/wiki/banners/monster.tga"]
		]
	],
	[
		localeInfo.WIKI_CATEGORY_METINSTONES,
		[
			[localeInfo.WIKI_SUBCATEGORY_LV1_75, (2, 1, 76), "d:/ymir work/ui/wiki/banners/metin.tga"],
			[localeInfo.WIKI_SUBCATEGORY_LV76_100, (2, 76, 100), "d:/ymir work/ui/wiki/banners/metin.tga"],
			[localeInfo.WIKI_SUBCATEGORY_LV100, (2, 100, 255), "d:/ymir work/ui/wiki/banners/metin.tga"]
		]
	],
	# [
	# 	localeInfo.WIKI_CATEGORY_SYSTEMS,
	# 	[
	# 		[localeInfo.WIKI_SUBCATEGORY_BATTLEPASS, ("systems/battlepass.txt",)],
	# 		[localeInfo.WIKI_SUBCATEGORY_COSTUMES, ("systems/costumes.txt",)],
	# 	]
	# ],
	[
		localeInfo.WIKI_CATEGORY_DUNGEONS,
		[
			[localeInfo.WIKI_SUBCATEGORY_SPIDER_BARONESS, ("dungeons/spider_baroness.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_DEMONTOWER, ("dungeons/demontower.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_AZRAEL, ("dungeons/azrael.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_BERAN_SETAOU, ("dungeons/beran_setaou.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_RAZADOR, ("dungeons/razador.txt",), "d:/ymir work/ui/wiki/banners/razador.tga"],
			[localeInfo.WIKI_SUBCATEGORY_NEMERE, ("dungeons/nemere.txt",), "d:/ymir work/ui/wiki/banners/nemere.tga"],
		]
	],
	[
		localeInfo.WIKI_CATEGORY_WORLDBOSSES,
		[
			[localeInfo.WIKI_SUBCATEGORY_ALASTOR, ("dungeons/alastor.txt",), "d:/ymir work/ui/wiki/banners/alastor.tga"],
			[localeInfo.WIKI_SUBCATEGORY_ORC_MALEFIC, ("dungeons/orc_malefic.txt",), "d:/ymir work/ui/wiki/banners/evilcave.tga"],
		]
	],
	[
		localeInfo.WIKI_CATEGORY_COSTUMES,
		[
			[localeInfo.WIKI_SUBCATEGORY_ARMOR, (COSTUME_ARMOR_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_armor.tga"],
			[localeInfo.WIKI_SUBCATEGORY_HAIRSTYLES, (COSTUME_HAIR_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_hairstyle.tga"],
			[localeInfo.WIKI_SUBCATEGORY_WEAPONS, (COSTUME_WEAPON_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_weapon.tga"],
			[localeInfo.WIKI_SUBCATEGORY_PET, (COSTUME_PET_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_pet.tga"],
			[localeInfo.WIKI_SUBCATEGORY_MOUNT, (COSTUME_MOUNT_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_mount.tga"],
		]
	],
	[
		localeInfo.WIKI_CATEGORY_EVENTS,
		[
			[localeInfo.WIKI_SUBCATEGORY_BOSS_HUNT, ("events/boss_hunt.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_MOONLIGHT_CHESTS, ("events/moonlight_chests.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_HEXAGONAL_CHESTS, ("events/hexagonal_chests.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_PVP_TOURNAMENT, ("events/pvp_tournament.txt",)],
		]
	],
	[
		localeInfo.WIKI_CATEGORY_GUIDES,
		[
			[localeInfo.WIKI_SUBCATEGORY_THE_START, ("guides/the_start.txt",)],
			[localeInfo.WIKI_SUBCATEGORY_105_AND_NOW, ("guides/105_and_now.txt",)]
		]
	],
]

#/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\
#/!\/!\/!\ OTHER STUFF /!\/!\/!\

ITEM_BLACKLIST = [range(12050, 12099), range(9810, 9879), range(13609, 13619), range(3310, 3319), range(200, 219), 
				range(220, 239), range(3170, 3179), range(3180, 3189), 
				range(3200, 3209), range(13630, 13639), range(2190, 2199), range(7200, 7209), range(4030, 4039), range(1140, 1169), range(5130, 5159), range(7170, 7189),
				range(13640, 13649), range(13600, 13609), range(12000, 12009), 13620, 13660, 13160, 13200, 13190, 13180, 14560, 14540, 14520, 14500, 16560, 16540, 16520, 16500, 15430, 15390, 15370, 15240, 18000, 260 ]
MOB_BLACKLIST = [8730, 1091, 1092, 1096, 8731, 8729, 8728, 8726, 8727, 8715, 8714, 8028, 8030, 8029, 8461, 8462, 8463, 8059, 4096, 4101, 4476, 4097, 4098, 4099, 4100, 4469, 4470, 4471, 4472, 1107, 4474, 4475, 4550, 4551, 4552, 4553, 4554, 4555, 4556, 3091, 3190, 3490, 4102, 4103, 4561, 4560, 1192, 2591, 2594, 2593, 2592, 2595, 2596, 2597, 4477, 4479, 4478, 9510, 4557, 4558, 791, 2094, 5115, 7005, 5161, 5162, 60004,35035, range(6443, 6470),6394,6393,6392,6391,6322,6321,6193,6207,6151,3964,3963,3962,3961,3960,3959,3958,3957,3956,3913,3912,3911,3910,3906,3905,3903,3901,3890,3596,3595,3591,3590,949,948,765,3902,8615,8613,8611,8603,8607,8605,8601,7124,2495,2307,2306,2192,2093,1906,1903,1310,1307,1095,1094,796,795,60010,60009,8614,8612,8610,8606,8604,8602,8600,5002,5001,2207,2095,1905,1904,1902,1309,1308,993,794,793,692,20500,20432,20422,20399,8062,8061,8058,8057,6529,6209,8429,8428,8050,8049,8048,8038,8036,7112,7111,7110,7109,7108,7107,6118,20482,20481,20480,20479,20478,20477,20476,20475,20474,20473,20472,20471,8204,8203,8201,8200,8116,8115,8114,8113,8112,8111,8110,8109,8108,8107,8106,8105,8104,8103,8102,8101,8060,8047,8046,8045,8044,8043,8042,8041,8040,8039,8037,8035,8033,8034,8032,8031,8023,8022,8021,8020,8019,8018,8017,8016,8015,60005,12022,12018,11111,11110,11109,11108,11107,11106,11105,11104,11103,11102,11101,11100,8619,8618,8616,8617,7122,7121,7120,7116,7115,7114,7113,60007,11117,11116,11115,11114,11113,11112,8622,8621,7119,7118,60008,11510,11509,11508,11507,11506,11505,8623,7106,7105,7104,7103,7102,7101]
MOB_BLACKLIST.extend([[18019, 2291, 1334, 1306, 1307, 8052, 8609, 8608, 4559, 8608, 8609, 4559, 4562, 8508,8509,8510,8511,8505,8506,8507,8504,8503,7092,7093,8501,8502,7090,7091,7088,7089,7086,7087,7080,7079,7077,7078,7075,7076,7074,7073,7072,7071,7062,7063,7061,7060,7057,7058,7059,7052,7053,7054,7055,7051,7042,7050,7041,7036,7037,7038,7039,7040,7033,7034,7035,7032,7029,7030,7031,7028,7027,7026,7024,7025,7023,7022,7021,7020,7018,7019,7017,7015,7016,7014,7012,7013,7009,7010,7004,7006,7007,7008,5207,5208,5209,7001,7002,5206,5205,5204,5202,5203,5201,5146,5145,5144,5142,5143,5141,5133,5134,5132,5127,5131,5116,2311,5003,2302,2301,2234,2235,2233,2231,2232,2157,2158,2154,2155,2156,2153,2151,2152,2101,2054,2055,2053,2052,2051,2032,2031,2001,2002,1335,1174,1175,1176,1177,1067,1066,1061,1062,1031,1032,1033,1034,1035,1001,991,992,933,934,935,936,937,931,903,775,776,777,773,774,755,756,757,771,772,753,754,735,751,731,732,733,705,698,697,695,696,655,656,657,652,653,654,651,635,595,554,552,553,551,501,454,455,456,451,452,453,402,403,397,398,354,391,392,393,394,180,181,182,183,178,179,177,171,172,173,174,175,144,140,141,142,143,138,139,137,135,136,132,133,134,115,131,114,113,111,112,110,109,108,107,105,106,104,102,103,101,176,184,185,301,302,303,304,331,332,333,334,351,352,353,395,396,752,932,1036,1037,1038,1039,1040,1151,1152,1153,1154,1155,1156,1157,1171,1172,1173,1331,7003,7056,7085,7094,7095,7096,7083,7084,7082,7081,7070,7069,7068,7067,7066,7065,7064,7049,7048,7047,7046,7045,7044,7043,6519,6518,6517,6516,6514,6515,6513,6499,6497,6496,6495,6494,6492,6493,6491,6490,6487,6488,6489,6486,6484,6485,6481,6482,6483,6480,6479,6478,6477,6476,6475,6474,6473,6471,6472,6470,6302,6203,6301,6117,6201,6202,4022,6001,6002,6101,4016,4017,4018,4019,4020,3704,3705,3801,3802,3803,3305,3401,3304,3202,3204,3205,3301,3005,3101,2510,2511,2512,2513,2514,2312,767,761,762,763,764,2415,2491,2494,2501,2541,2542,2543,2544,3104,3405,3501,3804,3805,3904,3907,3908,3909,4012,4013,4014,4015,4021,6102,3604,3605,3001,9480,9481,9710,9711,9479,9478,9476,9477,9474,9475,9473,9467,9468,9465,9466,9464,9463,9461,9462,6511,6512,9460,6503,6504,6505,6506,6507,6436,6437,6438,6439,6440,6419,6420,6421,6422,6304,6305,6306,6307,6206,6303,6112,6113,6114,6115,6204,6110,6111,6109,5153,5154,5155,5156,5152,3955,5151,1601,1602,1603,3950,3951,1403,1501,1502,1503,972,973,974,975,966,967,968,969,941,942,943,944,670,671,672,673,674,675,6205,6405,6406,6409,6410,6510,6435,6434,6433,6427,6428,6429,6430,6431,6108,5157,6003,6004,3952,3953,3954,1401,1402,970,971,946,947,965,940,945,976,977,978,979,6005,6006,6007,6008,6308,6309,6310,6401,6402,6403,6404,6411,6412,6413,6414,6423,6424,6425,6426,6432,6441,6442,6501,6502,6508,6106,6107,6009,983,984,36079,36096,9705,9702,9703,9704,9141,9142,9700,9701,4023,4024,988,985,986,987,676,9139,9140,8416,8417,8418,8421,8441,35071,36097,35074,35073,35072,8443,8442]])

HAIRSTYLE_CAMERA_CFG = {
	player.MAIN_RACE_WARRIOR_M : ([311.4753, -16.3934, 150.0000], [0.0000, 0.0000, 152.3934]),
	player.MAIN_RACE_ASSASSIN_W : ([344.2622, -16.3934, 150.0000], [0.0000, 0.0000, 147.3934]),
	player.MAIN_RACE_SURA_M : ([311.4753, -16.3934, 150.0000], [0.0000, 0.0000, 172.1804]),
	player.MAIN_RACE_SHAMAN_W : ([344.2622, -16.3934, 150.0000], [0.0000, 0.0000, 147.3934]),
	player.MAIN_RACE_WARRIOR_W : ([344.2622, -16.3934, 150.0000], [0.0000, 0.0000, 147.3934]),
	player.MAIN_RACE_ASSASSIN_M : ([344.2622, -16.3934, 150.0000], [0.0000, 0.0000, 156.7869]),
	player.MAIN_RACE_SURA_W : ([311.4753, -16.3934, 150.0000], [0.0000, 0.0000, 156.7869]),
	player.MAIN_RACE_SHAMAN_M : ([377.0492, -16.3934, 150.0000], [0.0000, 0.0000, 163.7869])
}

if app.INGAME_WIKI_WOLFMAN:
	LYCAN_HAIRSTYLE_CAMERA_CFG = {
		player.MAIN_RACE_WOLFMAN_M : ([311.4753, -16.3934, 150.0000], [0.0000, 0.0000, 192.1804]),
	}
	HAIRSTYLE_CAMERA_CFG.update(LYCAN_HAIRSTYLE_CAMERA_CFG)
