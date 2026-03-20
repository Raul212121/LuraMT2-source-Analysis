"""
uiaffectshower.py

Suchen "class AffectShower(ui.Window):"

darunter 	
	AFFECT_DATA_DICT[chr.AFFECT_RESEARCHER_ELIXIR] = (localeInfo.TOOLTIP_AFFECT_RESEARCHER_ELIXIR, "d:/ymir work/ui/skill/common/affect/researcher_elixir.sub")


hinzufügen : 
"""

	if app.ENABLE_BATTLE_PASS_SYSTEM:
		AFFECT_DATA_DICT[chr.AFFECT_BATTLE_PASS] = (localeInfo.TOOLTIP_AFFECT_BATTLE_PASS, "d:/ymir work/ui/game/battle_pass/affect_icon.tga")



"""
darunter 	
				self.affectImageDict[affect] = image
				self.__ArrangeImageList()

			except Exception, e:
				print "except Aff auto potion affect ", e
				pass
		else:

hinzufügen : 
"""

			if app.ENABLE_BATTLE_PASS_SYSTEM:
				if affect != chr.AFFECT_BATTLE_PASS and affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY:
					description = description(float(value))


rendu : 

		else:
			if app.ENABLE_BATTLE_PASS_SYSTEM:
				if affect != chr.AFFECT_BATTLE_PASS and affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY:
					description = description(float(value))
			else:
				if affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY:
					description = description(float(value))
