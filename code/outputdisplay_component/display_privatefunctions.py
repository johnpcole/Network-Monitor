from ..common_components import Vector
import narrowtile_privatefunctions as NarrowTileFunction
import widetile_privatefunctions as WideTileFunction
from ..common_components import DateTime



def devicecolour(devicecategory, connectionstatus):

	if devicecategory == "Expected":
		if connectionstatus == True:
			outcome = "Light Green"
		else:
			outcome = "Red"
	elif devicecategory == "Optional":
		if connectionstatus == True:
			outcome = "Faded Yellow"
		else:
			outcome = "Blue"
	elif devicecategory == "Unexpected":
		if connectionstatus == True:
			outcome = "Orange"
		else:
			outcome = "Grey"
	else:
		print "Unexpected Device Category - ", devicecategory
		outcome = "Black"

	return outcome



# -------------------------------------------------------------------
# Returns the coordinates of banner items
# -------------------------------------------------------------------

def bannerposition(positioninteger):

	ver = 0
	hor = positioninteger
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

def alertboxflash(enableflag):

	outcome = False
	
	if enableflag == True:
		currentdatetime = DateTime.getnow()
		years, months, days, hours, minutes, seconds = currentdatetime.getsextuplet()
		if (seconds % 2) == 0:
			outcome = True

	return outcome

	
	

	