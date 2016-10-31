from ..common_components import Vector
import narrowtile_privatefunctions as NarrowTileFunction
import widetile_privatefunctions as WideTileFunction
from ..common_components import DateTime



def bannercolour(alerttype):

	return alerttype



def devicecolour(devicecategory, connectionstatus):

	if connectionstatus == True:
		prefix = " - Connected"
	else:
		prefix = " - Disconnected"

	return devicecategory + prefix



def deviceshade(highlightmode):

	if highlightmode == True:
		outcome = " - Bright"
	else:
		outcome = " - Dark"

	return outcome





# -------------------------------------------------------------------
# Returns the coordinates of banner items
# -------------------------------------------------------------------

def bannerposition(positioninteger, componentinteger):

	hor = 480 - int(positioninteger / 10)

	if componentinteger == 1:
		hor = hor + 78
		ver = -2
	elif componentinteger == -1:
		hor = 240
		ver = 0
	else:
		ver = 10

	return Vector.createfromvalues(hor, ver)



# -------------------------------------------------------------------
# Returns the coordinates of items
# -------------------------------------------------------------------

def itemposition(tiletypestring, positioninteger, subpositioninteger, itemcountinteger):

	if tiletypestring == "Wide":
		tileposition = WideTileFunction.getposition(positioninteger) # itemcountinteger isn't used
		itemoffset = WideTileFunction.getoffset(subpositioninteger)
	elif tiletypestring == "Narrow":
		tileposition = NarrowTileFunction.getposition(positioninteger, itemcountinteger)
		itemoffset = NarrowTileFunction.getoffset(subpositioninteger)
	else:
		print "Invalid Tile Type - ", tiletypestring
		tileposition = Vector.createfromvalues(0, 0)
		itemoffset = Vector.createfromvalues(0, 0)

	return Vector.add(tileposition, itemoffset)

	

# -------------------------------------------------------------------
# Returns the type of tile used for device type
# -------------------------------------------------------------------

def tiletype(devicetype):
	
	if devicetype == "Unknown":
		outcome = "Wide"
	else:
		outcome = "Narrow"

	return outcome
	
	
	
# -------------------------------------------------------------------
# Returns the dimensions of the alert box
# -------------------------------------------------------------------

def alertboxdimensions(tiletypestring):

	if tiletypestring == "Wide":
		outcome = WideTileFunction.getalertdimensions()
	elif tiletypestring == "Narrow":
		outcome = NarrowTileFunction.getalertdimensions()
	else:
		print "Invalid Tile Type - ", tiletypestring
		outcome = Vector.createfromvalues(0, 0)

	return outcome

	

# -------------------------------------------------------------------
# Returns whether the alert box should be displayed
# -------------------------------------------------------------------

# def alertboxflash(enableflag):
#
# 	outcome = False
#
# 	if enableflag == True:
# 		currentdatetime = DateTime.getnow()
# 		years, months, days, hours, minutes, seconds = currentdatetime.getsextuplet()
# 		if (seconds % 2) == 0:
# 			outcome = True
#
# 	return outcome


# -------------------------------------------------------------------
# Returns the alert box colour
# -------------------------------------------------------------------

def alertboxflash(tilecolour, deadcolour):

	currentdatetime = DateTime.getnowfraction(True) % 240
	currentfraction = min(100.0, abs(currentdatetime - 120.0)) / 100.0
	outcome = "mix " + tilecolour + "/" + str(currentfraction) + "/" + deadcolour

	return outcome





def issafetodelertcurrentmessage(position):
	if position == 0:
		outcome = True
	else:
		outcome = False

	return outcome



def getgreyshade(lightness):
	s = "000" + str(int(lightness))
	s = s[-3:]
	return "rgb " + s + " " + s + " " + s