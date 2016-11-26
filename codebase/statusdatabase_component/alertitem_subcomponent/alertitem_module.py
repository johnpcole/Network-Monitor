from . import alertitem_class as AlertItemClass



# ---------------------------------------------
# Builds an alert item object
# ---------------------------------------------

def createitem(devicename, changetype, alerttype):
	return AlertItemClass.DefineAlertItem(devicename, changetype, alerttype)

