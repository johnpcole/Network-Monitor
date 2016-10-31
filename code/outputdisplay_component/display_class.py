from window_subcomponent import Window
import display_privatefunctions as DisplayFunction
from ..common_components import Vector
from ..common_components import DateTime



# ===========================================================================================================
# This class drives the application display
# ===========================================================================================================

class DisplayDriver:



	def __init__(self):

		# Sets up pygame window related properties & methods and loads images, fonts and colours
		self.appwindow = Window()

		# Current date time
		self.recentthreshold = DateTime.createfromiso("20000101000000")

		# Last Updated
		self.lastupdated = DateTime.createfromiso("20000101000000")



# ===========================================================================================================
# Object Processing
# ===========================================================================================================

# ---------------------------------------------------------
# RUN DISPLAY SERVICE
# Is run every cycle
# ---------------------------------------------------------

	def rundisplayoutputservice(self, statusdatabaseobject):

		# Only refresh once a second
		if self.updatedisplayclock() == True:

			# Refresh the device tiles
			self.refreshdevicetiles(statusdatabaseobject)

			# Refresh the screen
			self.appwindow.refreshscreen()


# -------------------------------------------------------------------
# Updates the display clock, returning true if the time has changed
# -------------------------------------------------------------------


	def updatedisplayclock(self):

		currenttime = DateTime.getnow()

		if DateTime.areidentical(currenttime, self.lastupdated) == False:
			self.lastupdated.setfromobject(currenttime)
			outcome = True
		else:
			outcome = False

		return outcome



# -------------------------------------------------------------------
# Updates all elements of the screen, flips the display
# -------------------------------------------------------------------

	def refreshdevicetiles(self, statusdatabase):

		self.recentthreshold = DateTime.getnow()
		self.recentthreshold.adjustseconds(-30)
	
		knownindexer = 0
		unknownindexer = 0
		knowntotal = statusdatabase.getprioritisedstatuscount("Known")

		displaylist = statusdatabase.getprioritisedstatuslist(10, 4)


		for statusitem in displaylist:

			if statusitem.gettype() == "Unknown":
				unknownindexer = self.drawdevicetile(unknownindexer, statusitem, -999)
			else:
				knownindexer = self.drawdevicetile(knownindexer, statusitem, knowntotal)



	def drawdevicetile(self, devicecounter, statusobject, devicetotal):

		# Get the tile type, Narrow or Wide
		tiletype = DisplayFunction.tiletype(statusobject.gettype())
	
		# Get the tile colour
		tilecolour = DisplayFunction.devicecolour(statusobject.getcategory(), statusobject.getconnectionstatus("Any"))

		# Draw the main device icon
		self.drawdeviceicon(devicecounter, statusobject, devicetotal, tiletype, tilecolour)
		
		# Draw the ports if it's a known device
		if tiletype == "Narrow":
			self.drawporticons(devicecounter, statusobject, devicetotal, tilecolour)

		# Else write the MAC Address if it's an known device
		else:
			iconposition = DisplayFunction.itemposition("Wide", devicecounter, 1, -999)
			self.appwindow.windowobject.drawbox(iconposition, Vector.createfromvalues(200, 30), "Faded Yellow")
			self.appwindow.printtext("88:88:88:88:88:88", iconposition, "Left", tilecolour, "Unknown Device Label")

		# Draw the alert box (if it's recently changed)
		self.drawalertbox(devicecounter, statusobject, devicetotal, tiletype, tilecolour)

		return (devicecounter + 1)


		
	def drawdeviceicon(self, devicecounter, statusobject, devicetotal, tiletype, tilecolour):

		iconposition = DisplayFunction.itemposition(tiletype, devicecounter, 0, devicetotal)
		self.appwindow.printicon(statusobject.getimage(), iconposition, tilecolour)
		

		
	def drawporticons(self, devicecounter, statusobject, devicetotal, tilecolour):
	
		connectiontypecount = 0
		for connectiontype in ['Wired', 'Wireless', 'Unknown']:
			if statusobject.getconnectionstatus(connectiontype) == True:
				connectiontypecount = connectiontypecount + 1
				iconposition = DisplayFunction.itemposition("Narrow", devicecounter, connectiontypecount, devicetotal)
				self.appwindow.printicon(connectiontype, iconposition, tilecolour)
		
		
		
	def drawalertbox(self, devicecounter, statusobject, devicetotal, tiletype, tilecolour):

		if DisplayFunction.alertboxflash(statusobject.haschangedsince(self.recentthreshold)) == True:
			boxposition = DisplayFunction.itemposition(tiletype, devicecounter, -1, devicetotal)
			boxsize = DisplayFunction.alertboxdimensions(tiletype)
			self.appwindow.printbox(boxposition, boxsize, tilecolour)

	

	# ===========================================================================================================
	# Get Information
	# ===========================================================================================================


