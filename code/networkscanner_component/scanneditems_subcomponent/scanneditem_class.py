from ...common_components.networkaddress_datatypes import macaddress_module as MacAddress
from ...common_components.networkaddress_datatypes import ipaddress_module as IPAddress

# ===========================================================================================================
# This class captures each item returned from the network scan.
# ===========================================================================================================

class DefineScannedItem:

	def __init__(self, macaddressstring, ipaddressstring):
		
		# MAC Address (as an object)
		self.macaddress = MacAddress.createfromstring(macaddressstring)
		
		# IP Address (as an object)
		self.ipaddress = IPAddress.createfromstring(ipaddressstring)



# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# Returns the MAC Address object
# ---------------------------------------------------------

	def getmacaddress(self):
	
		return self.macaddress



# ---------------------------------------------------------
# Returns the IP Address object
# ---------------------------------------------------------

	def getipaddress(self):

		return self.ipaddress