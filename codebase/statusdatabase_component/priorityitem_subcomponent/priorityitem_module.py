from . import priorityitem_class as PriorityItemClass



# ---------------------------------------------
# Builds the display object
# ---------------------------------------------

def createitem(devicename, integersecondssincelastchanged):
	return PriorityItemClass.DefinePriorityItem(devicename, integersecondssincelastchanged)

