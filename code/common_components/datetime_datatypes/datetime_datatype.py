import datetime_class as DateTimeClass
import duration_datatype as Duration
from date_subcomponent import Date
from time_subcomponent import Time


# ---------------------------------------------------------
# Creates a datetime using an existing datetime object
# ---------------------------------------------------------

def createfromobject(datetimeobject):

	newdatetime = DateTimeClass.DefineDateTime()
	newdatetime.setfromobject(datetimeobject)
	return newdatetime



# ---------------------------------------------------------
# Creates a datetime using a
# Day-Month-Year-Hour-Minute-Second sextuplet of integers
# ---------------------------------------------------------

def createfromsextuplet(day, month, year, hour, minute, second):

	newdatetime = DateTimeClass.DefineDateTime()
	newdatetime.setfromsextuplet(day, month, year, hour, minute, second)
	return newdatetime



# ---------------------------------------------------------
# Creates a datetime using a YYYYMMDDHHMMSS string
# ---------------------------------------------------------

def createfromiso(isostring):

	newdatetime = DateTimeClass.DefineDateTime()
	newdatetime.setfromiso(isostring)
	return newdatetime



# ---------------------------------------------------------
# Returns the difference, in seconds, between this datetime
# and the datetime (object) passed in
# ---------------------------------------------------------

def secondsdifference(first, second):

	datedifference = Duration.createfromvalues(
											Date.daysdifference(first.getdatecomponent(), second.getdatecomponent()),
																										"Days")

	timedifference = Duration.createfromvalues(
											Time.secondsdifference(first.gettimecomponent(), second.gettimecomponent()),
																										"Seconds")

	return Duration.add(datedifference, timedifference)



# ---------------------------------------------------------
# Returns whether the first is later than the second
# ---------------------------------------------------------

def isfirstlaterthansecond(first, second):

	differenceduration = secondsdifference(first, second)

	if differenceduration.getsecondsvalue() > 0:
		outcome = True
	else:
		outcome = False

	return outcome



# ---------------------------------------------------------
# Returns whether the first is identical to the second
# ---------------------------------------------------------

def areidentical(first, second):

	differenceduration = secondsdifference(first, second)

	if differenceduration.getsecondsvalue() == 0:
		outcome = True
	else:
		outcome = False

	return outcome



# ---------------------------------------------------------
# Get Now
# ---------------------------------------------------------

def getnow():
	
	newdatetime = DateTimeClass.DefineDateTime()
	newdatetime.settonow()
	return newdatetime
	