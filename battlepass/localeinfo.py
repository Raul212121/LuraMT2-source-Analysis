"""
localeinfo.py

darunter 	
	def CutNumberExperienceString(n) :
		if n <= 0 :
			return "0"

		return "%s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]))

hinzufügen : 
"""

	if app.ENABLE_BATTLE_PASS_SYSTEM:
		def AddPointToNumberString(n) :
			if n <= 0 :
				return "0"

			return "%s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]))