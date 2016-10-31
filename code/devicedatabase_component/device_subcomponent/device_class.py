from port_subcomponent import MonitoredPort
from ...common_components import DateTime



# ===========================================================================================================
# This class captures each device and its ports within a single object.
# ===========================================================================================================

class Device:

	def __init__(self, devicenamestring):
		
		# The name of the device
		self.devicename = devicenamestring
		
		# The library of ports (which start empty)
		self.ports = []
		

	
# ===========================================================================================================
# Object Processing
# ===========================================================================================================
	
# ---------------------------------------------------------
# This method adds a port to the device, with the
# specified MAC Address (as object) and port type
# Returns success/failure outcome
# ---------------------------------------------------------

	def addport(self, macaddressobject, porttypestring):
		
		# Look for any existing port_subcomponent with the specified MAC Address
		# If there is no existing port, add one to the device
		if self.matchdevicebymacaddress(macaddressobject) == False:
			self.ports.append(MonitoredPort(macaddressobject, porttypestring))
			outcome = True
		
		# If there is an existing port, print an error
		else:
			print "Cannot add port with duplicate Mac Address - ", macaddressobject.getvalue()
			outcome = False
		
		return outcome

			
			
# ---------------------------------------------------------
# This refreshes the port details
# (IP Address and datetime last seen)
# Returns success/failure outcome
# ---------------------------------------------------------
			
	def refreshport(self, macaddressobject, seentimeobject, seenipaddressobject):
	
		# Look for any port that has the specified MAC Address
		port = self.getportbymacaddress(macaddressobject)
		
		# If there is a port, update it
		if port is not None:
			port.updateport(seentimeobject, seenipaddressobject)
			outcome = True
		
		# If there is no port, print an error
		else:
			outcome = False
			print "Cannot find port to update - ", macaddressobject.getvalue()
		
		return outcome


				
# ---------------------------------------------------------
# This returns connection status for each port type
# (Wired, Wireless, Unknown)
# ---------------------------------------------------------

	def porttypeseensince(self, baselinetimedateobject, porttypestring):

		# Default to zero connections
		outcome = False

		# Loop over all port_subcomponent on the device
		for port in self.ports:

			# If the port is connected AND of the correct type,
			# increase the connection count
			if port.porttypeseensince(baselinetimedateobject) == porttypestring:
				outcome = True

		return outcome

		
# ---------------------------------------------------------
# This returns true/false on whether at least one port
# is connected, thereby defining the device as connected
# ---------------------------------------------------------

	def seensince(self, baselinetimedateobject):

		# Default to the device not being connected
		outcome = False

		# Loop over all port_subcomponent on the device
		for port in self.ports:

			# If the port is connected, mark the device as connected
			if port.seensince(baselinetimedateobject) == True:
				outcome = True

		return outcome
	
	

# ---------------------------------------------------------
# This true/false on whether the device has the specified
# MAC Address
# ---------------------------------------------------------
	
	def matchdevicebymacaddress(self, macaddressobject):
		
		if self.getportbymacaddress(macaddressobject) is None:
			outcome = False
		else:
			outcome = True
		
		return outcome
	

	
# ---------------------------------------------------------
# This returns the port object with the specified
# MAC Address, if it exists
# ---------------------------------------------------------

	def getportbymacaddress(self, macaddressobject):
		
		# Default to no port returned
		outcome = None
		
		# Loop over all port_subcomponent on the device
		for port in self.ports:
			
			# If the port matches the MAC Address object, return the port object
			if port.matchportbymacaddress(macaddressobject) == True:
				outcome = port
		
		return outcome


		
# ---------------------------------------------------------
# This returns the image of the device
# ---------------------------------------------------------

	def getname(self):

		return self.devicename



# ---------------------------------------------------------
# This returns the latest last seen date of all the ports
# ---------------------------------------------------------

	def getlastseen(self):

		devicelastseen = DateTime.createfromiso("20000101000000")

		for port in self.ports:
			portlastseen = port.getdatetimelastseen()
			if DateTime.isfirstlaterthansecond(portlastseen, devicelastseen):
				devicelastseen.setfromobject(portlastseen)

		return devicelastseen


		