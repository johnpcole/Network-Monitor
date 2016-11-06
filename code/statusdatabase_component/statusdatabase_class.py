from devicestatus_subcomponent import devicestatus_module as DeviceStatus
from ..common_components.datetime_datatypes import datetime_module as DateTime
from ..common_components.fileprocessing_framework import fileprocessing_module as File
from . import reporting_privatefunctions as ReportingFunction



# ===========================================================================================================
# This class captures all devices and their ports within a single object, along with information about the
# last update time. The database refreshes by being passed a list of addresses resulting from a scan.
# ===========================================================================================================

class DefineStatusDatabase:
	
	
	
	def __init__(self):
		
		# The last time the statuses were updated
		self.laststatusupdate = DateTime.createfromiso("20000101000000")
		
		# The library of device_subcomponent (which starts empty)
		self.statusdevices = []
		
		# Pre-populate the database with known devices
		self.addknowndevices()


# ===========================================================================================================
# Object Processing
# ===========================================================================================================

# ---------------------------------------------------------
# RUN DATABASE UPDATE SERVICE
# Can be run every cycle (or just after a scan)
# Returns true if an update was performed
# ---------------------------------------------------------

	def rundatabaseupdateservice(self, devicedatabaseobject):

		# Get the timedate of the last scan
		lastscantimedate = devicedatabaseobject.getupdatedatetime()

		# If the last update doesn't match the last scan
		if DateTime.areidentical(self.laststatusupdate, lastscantimedate) == False:

			# Update the last time the ports were updated
			self.laststatusupdate.setfromobject(lastscantimedate)
		
			# Perform the update on all devices
			self.refreshstatuses(devicedatabaseobject)

			outcome = True
		else:
			outcome = False

		return outcome



# ---------------------------------------------------------
# ---------------------------------------------------------
	
	def refreshstatuses(self, devicedatabaseobject):
		
		# Loop over all devices in the device database
		for device in devicedatabaseobject.getdeviceslist():

			# Identify the device associated with the MAC Address
			# (Creating a new device if necessary)
			statusdevice = self.crossreferencestatusdevice(device.getname())
			
			# Update the information on the statusdevice
			statusdevice.refreshinformation(device, self.laststatusupdate)



# ---------------------------------------------------------
# ---------------------------------------------------------

	def crossreferencestatusdevice(self, devicenamestring):

		# Look for a device with this MAC Address
		statusdevice = self.getstatusdevicebyname(devicenamestring)
		
		# If there is no device, create a new device and return it
		if statusdevice is None:
			self.addstatusdevice(devicenamestring, "unknowndevice", "Unexpected")
			outcome = self.getstatusdevicebyname(devicenamestring)
		
		# Or return the existing device
		else:
			outcome = statusdevice

		return outcome



# ---------------------------------------------------------
# ---------------------------------------------------------

	def addstatusdevice(self, devicenamestring, imagenamestring, devicecategorystring):
		
		# Look for the device with the specified name
		# If there is no existing device with that name, add a new device
		if self.getstatusdevicebyname(devicenamestring) is None:
			self.statusdevices.append(DeviceStatus.createstatus(devicenamestring, imagenamestring, devicecategorystring))
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
		knowndeviceslist = File.readfromdisk("database/knowndevices.txt")

		# Loop over all lines in the file
		for deviceline in knowndeviceslist:
				
			# Splits the line by tabs
			sections = deviceline.split("\t")
			sectioncount = len(sections)
		
			# If there are at least three items, the line contains valid data
			if sectioncount > 2:
			
				# Use the data from columns 1-3 to create a known device
				self.addstatusdevice(sections[0], sections[2], sections[1])



# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# This method returns the device object which matches
# the specified name
# ---------------------------------------------------------

	def getstatusdevicebyname(self, devicenamestring):
		
		# Default to there being no device object returned
		outcome = None
		
		# Search through all device_subcomponent in the list
		for statusdevice in self.statusdevices:

			# If the name of the searched device matches the specification,
			# return the device
			if statusdevice.getname() == devicenamestring:
				outcome = statusdevice
		
		return outcome

		

# ---------------------------------------------------------
# This method returns the list of devices
# ---------------------------------------------------------

	def getfullstatuslist(self):

		return self.statusdevices



# ---------------------------------------------------------
# This method returns the prioritised list of devices
# ---------------------------------------------------------

	def getprioritisedstatuslist(self, knownlimit, unknownlimit):

		return ReportingFunction.getprioritisedstatuslist(self.statusdevices, knownlimit, unknownlimit)



# ---------------------------------------------------------
# This method returns the list of device names for devices
# which have changed since the specified date, or are
# in an inappropriate state
# ---------------------------------------------------------

	def getalertitems(self, datetimethreshold):
		#for test in ReportingFunction.getrecentlychangeditems(self.statusdevices, datetimethreshold):
			#print "Reporting Recently Changed at ", datetimethreshold.getiso(), " - ", test.getname(), test.getchangetype()
		return ReportingFunction.getalertitems(self.statusdevices, datetimethreshold)



# ---------------------------------------------------------
# This method returns the number of prioritised devices
# ---------------------------------------------------------

	def getprioritisedstatuscount(self, devicetype):
	
		itemcount = 0
		for pi in self.getprioritisedstatuslist(20, 20):
			if pi.gettype() == devicetype:
				itemcount = itemcount + 1
		
		return itemcount


