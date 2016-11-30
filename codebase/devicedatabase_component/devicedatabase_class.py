from device_subcomponent import device_module as Device
from ..common_components.datetime_datatypes import datetime_module as DateTime
from ..common_components.fileprocessing_framework import fileprocessing_module as File
from ..common_components.networkaddress_datatypes import macaddress_module as MacAddress



# ===========================================================================================================
# This class captures all devices and their ports within a single object, along with information about the
# last update time. The database refreshes by being passed a list of addresses resulting from a scan.
# ===========================================================================================================

class DefineDeviceDatabase:
	
	
	
	def __init__(self):
		
		# The last time the ports were updated
		self.lastportsupdate = DateTime.createfromiso("20000101000000")
		
		# The library of device_subcomponent (which starts empty)
		self.devices = []
		
		# Pre-populate the database with known devices
		self.addknowndevices()

		# Keeps track of the number of unknown devices to ensure unique device naming
		self.unknownindex = 0

# ===========================================================================================================
# Object Processing
# ===========================================================================================================

# ---------------------------------------------------------
# RUN DATABASE UPDATE SERVICE
# Can be run every cycle (or just after a scan)
# Returns true if an update was performed
# ---------------------------------------------------------

	def rundatabaseupdateservice(self, networkscanobject):

		# Get the timedate of the last scan
		lastscantimedate = networkscanobject.getscandatetime()

		# If the last update doesn't match the last scan
		if DateTime.areidentical(self.lastportsupdate, lastscantimedate) == False:

			# Update the last time the ports were updated
			self.lastportsupdate.setfromobject(lastscantimedate)
		
			# Perform the update on all existing ports & add new devices
			self.refreshports(networkscanobject.getscanresults())

			outcome = True
		
		else:

			outcome = False
		
		return outcome



# ---------------------------------------------------------
# This method takes a list of networkscanresults and updates
# the device list, either modifying existing device or
# adding new ones if the mac address isn't recognised
# ---------------------------------------------------------
	
	def refreshports(self, networkscanresultslistobject):
		
		# Loop over all items in the scan results list
		for scannedaddress in networkscanresultslistobject:
			
			# Get the MAC Address of the current item
			scannedmacaddressobject = scannedaddress.getmacaddress()
			
			# Identify the device associated with the MAC Address
			# (Creating a new device if necessary)
			device = self.crossreferencedevice(scannedmacaddressobject)
			
			# Update the port information on the device
			device.refreshport(scannedmacaddressobject, self.lastportsupdate, scannedaddress.getipaddress())



# ---------------------------------------------------------
# This method takes a MAC Address and returns the device
# associated with it. If there is no device, create a
# new one and return it.
# ---------------------------------------------------------

	def crossreferencedevice(self, macaddressobject):

		# Look for a device with this MAC Address
		device = self.getdevicebymacaddress(macaddressobject)
		
		# If there is no device, create a new device and return it
		if device is None:
			self.addunknowndevice(macaddressobject)
			outcome = self.getdevicebymacaddress(macaddressobject)
		
		# Or return the existing device
		else:
			outcome = device

		return outcome



# ---------------------------------------------------------
# This method adds a new unknown device to the list, with
# the specified MAC Address
# ---------------------------------------------------------

	def addunknowndevice(self, macaddressobject):
		
		# Increment unique ID counter
		self.unknownindex = self.unknownindex + 1
		
		# Create the device name using unique ID counter
		newdevicenamestring = "00000" + str(self.unknownindex)
		newdevicenamestring = "Unregistered Device " + newdevicenamestring[-5:]
		
		# Add a brand new device to the list, marked as unknown
		self.adddevice(newdevicenamestring)
		
		# Add a port to the new device, marked as unknown
		self.addporttodevice(newdevicenamestring, macaddressobject, "Unknown")

	
	
# ---------------------------------------------------------
# This method adds a port to an existing device, with
# specified MAC Address and Port Type.
# Returns success/failure outcome
# ---------------------------------------------------------

	def addporttodevice(self, devicenamestring, macaddressobject, porttypestring):
		
		# Outcome defaults to Failed
		outcome = False
		
		# Look for the device with this specified name
		device = self.getdevicebyname(devicenamestring)
		
		# If there is a device, add a port to it and return the outcome
		if device is not None:
			outcome = device.addport(macaddressobject, porttypestring)
		
		# If there is no device with the name, print an error
		else:
			print "Device not found for adding port - ", devicenamestring
		
		return outcome
	
	
	
# ---------------------------------------------------------
# This method adds a device to the library, with
# specified name, image and category info.
# Returns success/failure outcome
# ---------------------------------------------------------

	def adddevice(self, devicenamestring):
		
		# Look for the device with the specified name
		# If there is no existing device with that name, add a new device
		if self.getdevicebyname(devicenamestring) is None:
			self.devices.append(Device.createdevice(devicenamestring))
			outcome = True

		# If there is already and existing device with that name, print an error
		else:
			print "Cannot add Device with duplicate name - ", devicenamestring
			outcome = False
		
		return outcome
	
	
	
# ---------------------------------------------------------
# This method adds known devices to the library, read
# from a file
# ---------------------------------------------------------

	def addknowndevices(self):
	
		# Get the scan results from the file
		knowndeviceslist = File.readfromdisk(File.concatenatepaths("database", "knowndevices.txt"))

		# Loop over all lines in the file
		for deviceline in knowndeviceslist:
				
			# Splits the line by tabs
			sections = deviceline.split("\t")
			sectioncount = len(sections)
		
			# If there are at least three items, the line contains valid data
			if sectioncount > 2:
			
				# Use the data from column 1 to create a known device
				self.adddevice(sections[0])

				# Only read port data if there is some
				if sectioncount > 4:
				
					# Loop over number of specified ports
					for currentport in range(3, sectioncount, 2):

						# Add specified port to device
						self.addporttodevice(sections[0], MacAddress.createfromstring(sections[currentport+1]),
																								sections[currentport])
	
	
	
# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# This method returns the device object which matches
# the specified name
# ---------------------------------------------------------

	def getdevicebyname(self, devicenamestring):
		
		# Default to there being no device object returned
		outcome = None
		
		# Search through all device_subcomponent in the list
		for device in self.devices:

			# If the name of the searched device matches the specification,
			# return the device
			if device.getname() == devicenamestring:
				outcome = device
		
		return outcome
	
	
	
# ---------------------------------------------------------
# This method returns the device object which matches
# the specified MAC Address (passed in as an object)
# ---------------------------------------------------------

	def getdevicebymacaddress(self, macaddressobject):
		
		# Default to there being no device object returned
		outcome = None

		# Search through all device_subcomponent in the list
		for device in self.devices:

			# Look for a port in the device which has the same MAC Address
			# If a port is returned, then the device is the correct one
			if device.matchdevicebymacaddress(macaddressobject) == True:
				outcome = device
		
		return outcome


			
# ---------------------------------------------------------
# This method returns the list of devices
# ---------------------------------------------------------

	def getdeviceslist(self):

		return self.devices



# ---------------------------------------------------------
# This method returns the datetime of the last update
# ---------------------------------------------------------

	def getupdatedatetime(self):

		return self.lastportsupdate


