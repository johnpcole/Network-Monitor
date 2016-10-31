from ....common_components import MacAddress
from ....common_components import IPAddress
from ....common_components import DateTime



# ===========================================================================================================
# This class captures each port on devices.
# ===========================================================================================================

class MonitoredPort:

	def __init__(self, macaddressobject, porttypestring):
		
		# The MAC Address of the port (stored as an object)
		self.macaddress = MacAddress.createfromstring("00:00:00:00:00:00")
		self.macaddress.setfromobject(macaddressobject)

		# The last known IP Address of the port (stored as an object)
		self.lastipaddress = IPAddress.createfromstring("0.0.0.0")

		# The last time the port was seen on the network (stored as an object)
		self.lastseen = DateTime.createfromiso("20000101000000")
		
		# The type of port; Wireless, Wired, Unknown
		self.porttype = ""
		self.setporttype(porttypestring)
	

	
# ===========================================================================================================
# Object Processing
# ===========================================================================================================

# ---------------------------------------------------------
# Sets the port type
# ---------------------------------------------------------

	def setporttype(self, porttypestring):
		
		if porttypestring == "Wireless":
			self.porttype = "Wireless"
		elif porttypestring == "Wired":
			self.porttype = "Wired"
		else:
			self.porttype = "Unknown"

			
			
# ---------------------------------------------------------
# This updates the IP Address and Last Seen Date based on
# scan results
# ---------------------------------------------------------

	def updateport(self, seentimeobject, seenipaddressobject):

		self.lastipaddress.setfromobject(seenipaddressobject)
		self.lastseen.setfromobject(seentimeobject)



# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# This returns true/false on whether the port
# has been seen since the specified snapshot time
# ---------------------------------------------------------

	def seensince(self, baselinetimedateobject):
		if DateTime.isfirstlaterthansecond(baselinetimedateobject, self.lastseen) == True:
			outcome = False
		else:
			outcome = True

		return outcome

	
	
# ---------------------------------------------------------
# This returns the port type if connected, and
# "Not Connected" if not connected
# ---------------------------------------------------------

	def porttypeseensince(self, baselinetimedateobject):
		
		if self.seensince(baselinetimedateobject) == True:
			outcome = self.porttype
		else:
			outcome = "Not Connected"
			
		return outcome

		
		
# ---------------------------------------------------------
# This true/false on whether the port has the specified
# MAC Address
# ---------------------------------------------------------
	
	def matchportbymacaddress(self, macaddressobject):
		
		return MacAddress.compare(self.macaddress, macaddressobject)



# ---------------------------------------------------------
# This returns the datetime the port was last seen
# ---------------------------------------------------------

	def getdatetimelastseen(self):
		return self.lastseen



