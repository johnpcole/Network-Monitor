from ...common_components.appdisplay_framework import appdisplay_module as AppDisplay
from ...common_components.vector_datatype import vector_module as Vector



# ===========================================================================================================
# This class drives the application display
# ===========================================================================================================

class DefineWindow:



	def __init__(self):

		# Define Screensize
		self.windowsize = Vector.createfromvalues(480, 320)

		# Sets up pygame window related properties & methods and loads images, fonts and colours
		self.windowobject = AppDisplay.createwindow(self.windowsize, "Network Monitor")
		self.imagesize = {}
		self.setupimages()
		self.setupfonts()
		self.setupcolours()



	def setupimages(self):

		imagelist = {}
		imagelist['alert'] = "Banner"
		imagelist['cloud'] = "Device"
		imagelist['earth'] = "Device"
		imagelist['folder'] = "Device"
		imagelist['gamepad'] = "Device"
		imagelist['info'] = "Banner"
		imagelist['keypad'] = "Device"
		imagelist['laptop'] = "Device"
		imagelist['monitor'] = "Device"
		imagelist['presentation'] = "Device"
		imagelist['projector'] = "Device"
		imagelist['question'] = "Device"
		imagelist['radar'] = "Device"
		imagelist['router'] = "Device"
		imagelist['smartphone'] = "Device"
		imagelist['tv'] = "Device"
		imagelist['unknowndevice'] = "Small Device"
		imagelist['unknown'] = "Port"
		imagelist['wired'] = "Port"
		imagelist['wireless'] = "Port"
		imagelist['wirelessrouter'] = "Device"
		imagelist['workstation'] = "Device"

		for spritename in imagelist:
			self.windowobject.addimage(spritename, "images", spritename, True)
			self.imagesize[spritename] = imagelist[spritename]



	def setupfonts(self):

		self.windowobject.addfont("Unknown Device Label", "", "gillsanscondensed", 30)
		self.windowobject.addfont("Clock Text", "", "gillsansnormal", 68)
		self.windowobject.addfont("Banner Text", "", "gillsansnormal", 72)



	def setupcolours(self):

		self.windowobject.addcolour("info", 128, 255, 255)
		self.windowobject.addcolour("alert", 255, 128, 128)
		self.windowobject.addcolour("Expected - Connected - Bright", 0, 255, 128)
		self.windowobject.addcolour("Expected - Disconnected - Bright", 255, 0, 0)
		self.windowobject.addcolour("Optional - Connected - Bright", 255, 255, 128)
		self.windowobject.addcolour("Optional - Disconnected - Bright", 0, 0, 255)
		self.windowobject.addcolour("Unexpected - Connected - Bright", 255, 128, 0)
		self.windowobject.addcolour("Unexpected - Disconnected - Bright", 64, 64, 64)
		self.windowobject.addcolour("Expected - Connected - Dark", 32, 160, 96)
		self.windowobject.addcolour("Expected - Disconnected - Dark", 160, 32, 32)
		self.windowobject.addcolour("Optional - Connected - Dark", 160, 160, 96)
		self.windowobject.addcolour("Optional - Disconnected - Dark", 32, 32, 160)
		self.windowobject.addcolour("Unexpected - Connected - Dark", 160, 96, 32)
		self.windowobject.addcolour("Unexpected - Disconnected - Dark", 64, 64, 64)



# ===========================================================================================================
# Object Processing
# ===========================================================================================================



# -------------------------------------------------------------------
# Flips the display, then blanks it in preparation for the next frame
# -------------------------------------------------------------------

	def refreshscreen(self):

		self.windowobject.updatescreen()
		self.windowobject.drawrectangle(Vector.createfromvalues(0, 0), self.windowsize, "Black", "", 0)



# -------------------------------------------------------------------
# Draws an icon (which is a coloured rectangle with a cutout overlay
# -------------------------------------------------------------------

	def printicon(self, iconlabel, positioncoordinates, colourlabel):

		iconname = iconlabel.lower()
		if colourlabel != "None":
			self.windowobject.drawrectangle(positioncoordinates, self.geticonsize(iconname), colourlabel, "", 0)
		self.windowobject.drawimage(iconname, positioncoordinates)


# -------------------------------------------------------------------
# Draws text
# -------------------------------------------------------------------

	def printtext(self, outputtext, textposition, textalignment, textcolour, fontname):
		
		self.windowobject.drawtext(outputtext, textposition, textalignment, textcolour, fontname)



# -------------------------------------------------------------------
# Draws a box outline of thickness 2
# -------------------------------------------------------------------

	def printbox(self, topleftvector, dimensionsvector, colourlabel, thickness):
		
		self.windowobject.drawrectangle(topleftvector, dimensionsvector, "", colourlabel, thickness)



# ===========================================================================================================
# Get Information
# ===========================================================================================================



# -------------------------------------------------------------------
# Returns the icon size of the specified icon
# -------------------------------------------------------------------

	def geticonsize(self, iconlabel):
	
		sizelabel = self.imagesize[iconlabel]
		if sizelabel == "Banner":
			outcome = Vector.createfromvalues(64, 64) # Was 92
		elif sizelabel == "Device":
			outcome = Vector.createfromvalues(60, 60)
		elif sizelabel == "Small Device":
			outcome = Vector.createfromvalues(30, 30)
		elif sizelabel == "Port":
			outcome = Vector.createfromvalues(20, 20)
		else:
			print "Unexpected Icon Size - ", sizelabel
			outcome = Vector.createfromvalues(2, 2)

		return outcome



	# -------------------------------------------------------------------
	# Text Width
	# -------------------------------------------------------------------

	def gettextwidth(self, outputtext, fontname):

		return (self.windowobject.gettextsize(outputtext, fontname)).getx()



	# -------------------------------------------------------------------
	# Window Size
	# -------------------------------------------------------------------

	def getscreensize(self):
		return self.windowsize











