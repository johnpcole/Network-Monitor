from window_subcomponent import window_module as Window
from messagelist_subcomponent import messagelist_module as MessageList
from . import display_privatefunctions as DisplayFunction
from ..common_components.datetime_datatypes import datetime_module as DateTime
from ..common_components.vector_datatype import vector_module as Vector



# ===========================================================================================================
# This class drives the application display
# ===========================================================================================================

class DefineDisplayDriver:



	def __init__(self):

		# Sets up pygame window related properties & methods and loads images, fonts and colours
		self.appwindow = Window.createwindow()
		self.lastscreenupdate = -999

		# Current date time
		self.recentthreshold = DateTime.createfromiso("20000101000000")
		self.datetimestring = ""

		# Messages List
		self.messages = MessageList.createlist()
		self.currentmessageposition = 0
		self.currentmessagetext = "Monitor Starting..."
		self.messagewidth = self.appwindow.gettextwidth(self.currentmessagetext, "Banner Text")
		self.clockvisibility = 200
		self.framerateissue = False

		# Speeds
		self.bannerspeed = 50
		self.clocktransitionspeed = 5
		self.displayrefreshspeed = 5
		self.recentdefinition = -60



# ===========================================================================================================
# Object Processing
# ===========================================================================================================

# ---------------------------------------------------------
# RUN DISPLAY SERVICE
# Is run every cycle
# ---------------------------------------------------------

	def rundisplayoutputservice(self, statusdatabaseobject, inputcontrollerobject):

		# Determine whether to bother to update the display
		if self.cycledisplay() == True:

			# Refresh the clock
			self.updateclock()

			# Refresh the device tiles
			self.refreshdevicetiles(statusdatabaseobject)

			# Refresh the banner area
			self.refreshbanner(statusdatabaseobject)

			# Refresh the buttons
			self.refreshbuttons(inputcontrollerobject)

			# Refresh the screen
			self.appwindow.refreshscreen()

# -------------------------------------------------------------------
# Updates the clock
# -------------------------------------------------------------------

	def cycledisplay(self):

		# Update the clock
		newtimefraction = DateTime.getnowfraction(False)

		if abs(newtimefraction - self.lastscreenupdate) > self.displayrefreshspeed:
			outcome = True
			self.lastscreenupdate = newtimefraction
		else:
			outcome = False

		self.checkrefreshrate(outcome)

		return outcome



# -------------------------------------------------------------------
# Updates the clock
# -------------------------------------------------------------------

	def checkrefreshrate(self, updateflag):

		if updateflag == True:
			if self.framerateissue == True:
				print "Refresh Rate Lag"
			self.framerateissue = True
		else:
			self.framerateissue = False



# -------------------------------------------------------------------
# Updates the clock
# -------------------------------------------------------------------

	def updateclock(self):

		self.recentthreshold.settonow()

		# Create the clock string which is printed in the banner
		datetimestring = self.recentthreshold.getreadabledate("24", False, "3", "3", "0", "0", " ")
		self.datetimestring = datetimestring[:5] + "   " + datetimestring[6:]

		# Update the threshold datetime for marking items as recently changed
		self.recentthreshold.adjustseconds(self.recentdefinition)



# -------------------------------------------------------------------
# Updates the message banner
# -------------------------------------------------------------------

	def refreshbanner(self, statusdatabase):

		# Get list of devices that are alerting from the status database
		alertslist = statusdatabase.getalertitems(self.recentthreshold)

		# Determine if it is safe to delete the current message
		# (Because it's not in view)
		issafetodeletecurrentmessage = DisplayFunction.issafetodelertcurrentmessage(self.currentmessageposition)

		# Update the message list, and return whether there are any messages
		queuedalertsflag = self.messages.updatemessagelist(alertslist, issafetodeletecurrentmessage)

		if self.updateclockvisibility(queuedalertsflag) == True:
			self.scrollbannermessage()
			self.drawmessagingbanner()
		else:
			self.currentmessageposition = 100000
			self.drawclockbanner()


# -------------------------------------------------------------------
# Updates clock visibility
# -------------------------------------------------------------------

	def updateclockvisibility(self, showalertflag):

		if showalertflag == True:
			self.clockvisibility = max(0, self.clockvisibility - self.clocktransitionspeed)
		else:
			self.clockvisibility = min(200, self.clockvisibility + self.clocktransitionspeed)

		if self.clockvisibility > 0:
			outcome = False
		else:
			outcome = True

		return outcome



# -------------------------------------------------------------------
# Draws the clock banner
# -------------------------------------------------------------------

	def drawclockbanner(self):

		textposition = DisplayFunction.bannerposition(-999, -1)
		textcolour = DisplayFunction.getgreyshade(self.clockvisibility)
		self.appwindow.printtext(self.datetimestring, textposition, "Centre", textcolour, "Clock Text")



# -------------------------------------------------------------------
# Draws the messages banner
# -------------------------------------------------------------------

	def drawmessagingbanner(self):

		bannercolour = DisplayFunction.bannercolour(self.messages.getcurrentmessagetype())
		self.drawbannericon(self.messages.getcurrentmessagetype(), bannercolour)
		textposition = DisplayFunction.bannerposition(self.currentmessageposition, 1)
		self.appwindow.printtext(self.currentmessagetext, textposition, "Left", bannercolour, "Banner Text")



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



	# -------------------------------------------------------------------
	# Draws a device tile
	# -------------------------------------------------------------------

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
			self.appwindow.printtext(statusobject.getname(), iconposition, "Left", tilecolour + " - Bright",
																								"Unknown Device Label")

		# Draw the alert box (if it's recently changed)
		self.drawalertbox(devicecounter, statusobject, devicetotal, tiletype, tilecolour)

		return (devicecounter + 1)



	# -------------------------------------------------------------------
	# Draws a banner icon
	# -------------------------------------------------------------------

	def drawbannericon(self, icontype, iconcolour):

		iconposition = DisplayFunction.bannerposition(self.currentmessageposition, 0)
		self.appwindow.printicon(icontype, iconposition, iconcolour)



	# -------------------------------------------------------------------
	# Draws a device icon
	# -------------------------------------------------------------------

	def drawdeviceicon(self, devicecounter, statusobject, devicetotal, tiletype, tilecolour):

		iconposition = DisplayFunction.itemposition(tiletype, devicecounter, 0, devicetotal)
		tileshade = DisplayFunction.deviceshade(statusobject.getalertstatus(self.recentthreshold))
		self.appwindow.printicon(statusobject.getimage(), iconposition, tilecolour + tileshade)



	# -------------------------------------------------------------------
	# Draws a port icon
	# -------------------------------------------------------------------

	def drawporticons(self, devicecounter, statusobject, devicetotal, tilecolour):
	
		connectiontypecount = 0
		tileshade = DisplayFunction.deviceshade(statusobject.getalertstatus(self.recentthreshold))
		for connectiontype in ['Wired', 'Wireless', 'Unknown']:
			if statusobject.getconnectionstatus(connectiontype) == True:
				connectiontypecount = connectiontypecount + 1
				iconposition = DisplayFunction.itemposition("Narrow", devicecounter, connectiontypecount, devicetotal)
				self.appwindow.printicon(connectiontype, iconposition, tilecolour + tileshade)



	# -------------------------------------------------------------------
	# Draws the box around each device
	# -------------------------------------------------------------------

	def drawalertbox(self, devicecounter, statusobject, devicetotal, tiletype, tilecolour):

		boxposition = DisplayFunction.itemposition(tiletype, devicecounter, -1, devicetotal)
		boxsize = DisplayFunction.alertboxdimensions(tiletype)
		if statusobject.getalertstatus(self.recentthreshold) == True:
			self.appwindow.printbox(boxposition, boxsize, "",
									DisplayFunction.alertboxflash(tilecolour + " - Bright", "Black"), 3)
			self.appwindow.printbox(boxposition, boxsize, "",
									DisplayFunction.alertboxflash(tilecolour + " - Bright" , tilecolour + " - Dark"), 1)
		else:
			self.appwindow.printbox(boxposition, boxsize, "", tilecolour + " - Dark", 1)

	# -------------------------------------------------------------------
	# Refreshes the display of all buttons
	# -------------------------------------------------------------------

	def refreshbuttons(self, inputcontrollerobject):

		buttonlist = inputcontrollerobject.getbuttoncollection("keyboard")

		for buttonname in buttonlist:
			if inputcontrollerobject.getbuttonstate(buttonname) != "Hidden":
				buttonposition = inputcontrollerobject.getbuttonposition(buttonname)
				buttonsize = inputcontrollerobject.getbuttonsize(buttonname)
				self.appwindow.printbox(buttonposition, buttonsize, "Black", "White", 1)
				texthor = int(((2 * buttonposition.getx()) + buttonsize.getx()) / 2)
				textver = buttonposition.gety() + 4
				self.appwindow.printtext(buttonname, Vector.createfromvalues(texthor,textver), "Centre", "White", "Button Text")












# ===========================================================================================================
# Get Information
# ===========================================================================================================


