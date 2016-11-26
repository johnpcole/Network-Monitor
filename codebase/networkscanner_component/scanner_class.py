from scanneditems_subcomponent import scanneditem_module as ScannedItem
from ..common_components.datetime_datatypes import datetime_module as DateTime
from ..common_components.datetime_datatypes import duration_module as Duration
from ..common_components.fileprocessing_framework import fileprocessing_module as File
from ..common_components.terminalinterface_framework import terminalinterface_module as Terminal

# ===========================================================================================================
# This class performs a network scan (interfacing with the OS), and
# captures all items returned from the network scan.
# ===========================================================================================================

class DefineNetworkScanner:
	
	
	
	def __init__(self):
		
		# Date of the latest scan (as an object)
		self.scandate = DateTime.createfromiso("20000101000000")
		
		# Library of items returned from the scan (initially empty, repeatedly emptied)
		self.scanresults = []
		
		# Frequency (in seconds) of the network scanning
		self.refreshrate = Duration.createfromvalues(10, "Seconds")
		
		# Date of the latest cycle (as an object)
		self.cycledate = DateTime.createfromiso("20000101000000")
		
		# Debug mode
		self.debugmode = True
		
		# Prepare the terminal screen
		Terminal.clearscreen(self.debugmode)

		
		
# ===========================================================================================================
# Object Processing
# ===========================================================================================================

# ---------------------------------------------------------
# RUN NETWORK SCANNING SERVICE
# Is run every cycle
# Returns true if a scan was performed
# ---------------------------------------------------------

	def runnetworkscanservice(self):

		# Set the cycle date to now
		self.cycledate.settonow()
		
		# Determine how long ago the last scan was
		timesincelastscan = DateTime.secondsdifference(self.scandate, self.cycledate)
		
		# If the last scan was longer ago than the refresh rate
		if Duration.iswithinlimit(timesincelastscan, self.refreshrate) == False:

			print "Performing Scan at ", self.scandate.getiso()

			# Perform the scan
			self.performnetworkscan()

			outcome = True
		
		else:

			outcome = False
		
		return outcome


# ---------------------------------------------------------
# Performs a scan using the OS, which creates a file
# Clear down the list of scanned items each time
# ---------------------------------------------------------

	def performnetworkscan(self):

		self.scandate.setfromobject(self.cycledate)
		self.deletescanneditems()
		Terminal.scannetwork("cache/scanresults.txt", self.debugmode)
		self.collatescanresults()
			
		
		
# ---------------------------------------------------------
# Opens and reads the file produced by the network scan
# ---------------------------------------------------------

	def collatescanresults(self):

		# Get the scan results from the file
		scanresults = File.readfromdisk("cache/scanresults.txt")

		# Loop over all lines in the file
		for scanline in scanresults:
				
			# Splits the line by tabs
			sections = scanline.split("\t")
		
			# If there are three items, the line contains valid data
			if len(sections) == 3:
			
				# Use the data from columns 2 & 1 to create a scanned item
				self.addscanneditem(sections[1], sections[0])



# ---------------------------------------------------------
# Adds a scanned item to the list
# ---------------------------------------------------------

	def addscanneditem(self, macaddressstring, ipaddressstring):

		self.scanresults.append(ScannedItem.createitem(macaddressstring, ipaddressstring))

		
		
# ---------------------------------------------------------
# Deletes all scanned items from the list,
# ready for a new scan
# ---------------------------------------------------------

	def deletescanneditems(self):

		del self.scanresults[:]


		
# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# Returns the list of scan results (as an object list)
# ---------------------------------------------------------

	def getscanresults(self):

		return self.scanresults
		
		
		
# ---------------------------------------------------------
# Returns the latest scan date (as an object)
# ---------------------------------------------------------

	def getscandatetime(self):

		return self.scandate
		