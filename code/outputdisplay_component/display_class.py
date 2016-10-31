from window_subcomponent import Window
import display_privatefunctions as DisplayFunction
#from ..common_components import Vector
from ..common_components import DateTime
from messagelist_subcomponent import MessageList



# ===========================================================================================================
# This class drives the application display
# ===========================================================================================================

class DisplayDriver:



	def __init__(self):

		# Sets up pygame window related properties & methods and loads images, fonts and colours
		self.appwindow = Window()

		# Current date time
		self.recentthreshold = DateTime.createfromiso("20000101000000")
		self.datetimestring = ""
		self.recentdefinition = -60

		# Messages List
		self.messages = MessageList()
		self.currentmessageposition = 0
		self.currentmessagetext = "Monitor Starting..."
		self.messagewidth = self.appwindow.gettextwidth(self.currentmessagetext, "Banner Text")
		self.bannerspeed = 5



# ===========================================================================================================
# Object Processing
# ===========================================================================================================

# ---------------------------------------------------------
# RUN DISPLAY SERVICE
# Is run every cycle
# ---------------------------------------------------------

	def rundisplayoutputservice(self, statusdatabaseobject):

		# Refresh the clock
		self.updateclock()

		# Refresh the device tiles
		self.refreshdevicetiles(statusdatabaseobject)

		# Refresh the banner area
		self.refreshbanner(statusdatabaseobject)

		# Refresh the screen
		self.appwindow.refreshscreen()



	# -------------------------------------------------------------------
	# Updates the clock
	# -------------------------------------------------------------------

	def updateclock(self):

		# Update the clock
		self.recentthreshold = DateTime.getnow()
		datetimestring = self.recentthreshold.getreadabledate("24", False, "3", "3", "0", "0", " ")
		self.datetimestring = datetimestring[:5] + "   " + datetimestring[6:]
		self.recentthreshold.adjustseconds(self.recentdefinition)



# -------------------------------------------------------------------
# Updates the message banner
# -------------------------------------------------------------------

	def refreshbanner(self, statusdatabase):

		showalerts = self.messages.updatemessagelist(statusdatabase.getalertitems(self.recentthreshold),
											DisplayFunction.issafetodelertcurrentmessage(self.currentmessageposition))

		#self.appwindow.printbox(Vector.createfromvalues(0, 0), Vector.createfromvalues(480, 92), "Yellow")
		if showalerts == True:
			self.scrollbannermessage()
			bannercolour = DisplayFunction.bannercolour(self.messages.getcurrentmessagetype())
			self.drawbannericon(self.messages.getcurrentmessagetype(), bannercolour)
			textposition = DisplayFunction.bannerposition(self.currentmessageposition, 1)
			self.appwindow.printtext(self.currentmessagetext, textposition, "Left", bannercolour, "Banner Text")
		else:
			self.currentmessageposition = 100000
			textposition = DisplayFunction.bannerposition(2400, 0)
			self.appwindow.printtext(self.datetimestring, textposition, "Centre", "Grey", "Banner Text")



# -------------------------------------------------------------------
# Scrolls the banner
# -------------------------------------------------------------------

	def scrollbannermessage(self):

		self.currentmessageposition = self.currentmessageposition + self.bannerspeed
		textposition = (DisplayFunction.bannerposition(self.currentmessageposition, 1)).getx()
		if textposition < 0 - self.messagewidth:
			self.changebannermessage()



# -------------------------------------------------------------------
# Changes the banner message
# -------------------------------------------------------------------

	def changebannermessage(self):

		self.currentmessageposition = 0
		self.currentmessagetext = self.messages.changemessage()
		self.messagewidth = self.appwindow.gettextwidth(self.currentmessagetext, "Banner Text")



# -------------------------------------------------------------------
# Updates all the device tiles
# -------------------------------------------------------------------

	def refreshdevicetiles(self, statusdatabase):

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

		# Else write the MAC Address if it's an unknown device
		else:
			iconposition = DisplayFunction.itemposition("Wide", devicecounter, 1, -999)
			#self.appwindow.windowobject.drawbox(iconposition, Vector.createfromvalues(199, 31), "Faded Yellow")
			self.appwindow.printtext(statusobject.getname(), iconposition, "Left", tilecolour, "Unknown Device Label")

		# Draw the alert box (if it's recently changed)
		self.drawalertbox(devicecounter, statusobject, devicetotal, tiletype, tilecolour)

		return (devicecounter + 1)



	def drawbannericon(self, icontype, iconcolour):

		iconposition = DisplayFunction.bannerposition(self.currentmessageposition, 0)
		self.appwindow.printicon(icontype, iconposition, iconcolour)



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

		if DisplayFunction.alertboxflash(statusobject.getalertstatus(self.recentthreshold)) == True:
			boxposition = DisplayFunction.itemposition(tiletype, devicecounter, -1, devicetotal)
			boxsize = DisplayFunction.alertboxdimensions(tiletype)
			self.appwindow.printbox(boxposition, boxsize, tilecolour)

	

	# ===========================================================================================================
	# Get Information
	# ===========================================================================================================


