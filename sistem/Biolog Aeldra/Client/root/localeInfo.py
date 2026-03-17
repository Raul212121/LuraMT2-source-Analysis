
# ADD

# Convert seconds to Hours-Minutes Seconds
def SecondToHMS(time):
	try:
		time = int(time)
	except ValueError:
		return "0 " + SECOND

	if int(time) <= 0:
		return "0 " + SECOND

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60)

	text = ""

	if hour > 0:
		text += str(hour) + HOUR
		if minute > 0:
			text += " "

	if minute > 0:
		text += str(minute) + MINUTE
		if second > 0:
			text += " "

	if second > 0:
		text += str(second) + " " + SECOND

	return text
    