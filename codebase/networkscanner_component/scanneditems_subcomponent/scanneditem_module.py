from . import scanneditem_class as ScannedItemClass



# ---------------------------------------------
# Builds a Scanned Item object
# ---------------------------------------------

def createitem(macaddressstring, ipaddressstring):
	return ScannedItemClass.DefineScannedItem(macaddressstring, ipaddressstring)

