import datetime

#How far back in hours to go?
hours = 150

def getCurrentTimeFormatted():
	now = datetime.datetime.now()
	return now.strftime("%Y-%m-%dT%H:%M:%S")

def getCurrentTime():
	return datetime.datetime.now()

def getTimeDelta(currentTime, delta):
	shiftedTime = currentTime - datetime.timedelta(hours=delta)
	return shiftedTime.strftime("%Y-%m-%dT%H:%M:%S")

print "Current TimeF:", getCurrentTimeFormatted()
print "Delta Shift:", hours, "hours"
print "Delta Time:", getTimeDelta(getCurrentTime(), hours)