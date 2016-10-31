from ...common_components import AppDisplay
from ...common_components import Vector



# ===========================================================================================================
# This class drives the application display
# ===========================================================================================================

class Window:



	def __init__(self):

		# Define Screensize
		self.windowsize = Vector.createfromvalues(480, 320)

		# Sets up pygame window related properties & methods and loads images, fonts and colours
		self.windowobject = AppDisplay.createappwindow(self.windowsize, "Network Monitor")
		self.imagesize = {}
		self.setupimages()
		self.setupfonts()



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
		imagelist['unknown'] = "Small Device"
		imagelist['unknownconnection'] = "Port"
		imagelist['wired'] = "Port"
		imagelist['wireless'] = "Port"
		imagelist['wirelessrouter'] = "Device"
		imagelist['workstation'] = "Device"

		for spritename in imagelist:
			self.windowobject.addimage(spritename, "images", spritename, True)
			self.imagesize[spritename] = imagelist[spritename]



	def setupfonts(self):

		self.windowobject.addfont("Unknown Device Label", "graphics/gillsanscondensed.ttf", 32)
		
		



# ===========================================================================================================
# Object Processing
# ===========================================================================================================



# -------------------------------------------------------------------
# Flips the display, then blanks it in preparation for the next frame
# -------------------------------------------------------------------

	def refreshscreen(self):

		self.windowobject.updatescreen()
		self.windowobject.drawbox(Vector.createfromvalues(0, 0), self.windowsize, "Black")



# -------------------------------------------------------------------
# Draws an icon (which is a coloured rectangle with a cutout overlay
# -------------------------------------------------------------------

	def printicon(self, iconlabel, positioncoordinates, colourlabel):

		iconname = iconlabel.lower()
		self.windowobject.drawbox(positioncoordinates, self.geticonsize(iconname), colourlabel)
		self.windowobject.drawimage(iconname, positioncoordinates)


# -------------------------------------------------------------------
# Draws text
# -------------------------------------------------------------------

	def printtext(self, outputtext, textposition, textalignment, textcolour, fontname):
		
		self.windowobject.drawtext(outputtext, textposition, textalignment, textcolour, fontname)



# -------------------------------------------------------------------
# Draws a box outline of thickness 2
# -------------------------------------------------------------------

	def printbox(self, topleftvector, dimensionsvector, colourlabel):
		
		self.windowobject.drawboxoutline(topleftvector, dimensionsvector, colourlabel, 2)



# ===========================================================================================================
# Get Information
# ===========================================================================================================



# -------------------------------------------------------------------
# Returns the icon size of the specified icon
# -------------------------------------------------------------------

	def geticonsize(self, iconlabel):
	
		sizelabel = self.imagesize[iconlabel]
		if sizelabel == "Banner":
			outcome = Vector.createfromvalues(92, 92)
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













