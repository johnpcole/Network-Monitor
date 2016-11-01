from ..common_components import AppInput
from ..common_components import Vector

# ===========================================================================================================
# This class captures all user inputs using pygame.
# ===========================================================================================================

class InputController:



	def __init__(self):

		self.inputobject = AppInput.createappinput()
		self.setupbuttons()

	def setupbuttons(self):

		self.definebutton("shift",   0,   0,    80,    40, ["keyboard"])
		self.definebutton("z",       0,  80,    40,    40, ["keyboard"])
		self.definebutton("x",       0, 120,    40,    40, ["keyboard"])
		self.definebutton("c",       0, 160,    40,    40, ["keyboard"])
		self.definebutton("v",       0, 200,    40,    40, ["keyboard"])
		self.definebutton("b",       0, 240,    40,    40, ["keyboard"])
		self.definebutton("n",       0, 280,    40,    40, ["keyboard"])
		self.definebutton("m",       0, 320,    40,    40, ["keyboard"])
		self.definebutton("space",   0, 360,   120,    40, ["keyboard"])

		self.definebutton("caps",   40,   0,    60,    40, ["keyboard"])
		self.definebutton("a",      40,  60,    40,    40, ["keyboard"])
		self.definebutton("s",      40, 100,    40,    40, ["keyboard"])
		self.definebutton("d",      40, 140,    40,    40, ["keyboard"])
		self.definebutton("f",      40, 180,    40,    40, ["keyboard"])
		self.definebutton("g",      40, 220,    40,    40, ["keyboard"])
		self.definebutton("h",      40, 260,    40,    40, ["keyboard"])
		self.definebutton("j",      40, 300,    40,    40, ["keyboard"])
		self.definebutton("k",      40, 340,    40,    40, ["keyboard"])
		self.definebutton("l",      40, 380,    40,    40, ["keyboard"])
		self.definebutton("enter1", 40, 420,    60,    40, ["keyboard"])

		self.definebutton("symbol", 80,   0,    40,    40, ["keyboard"])
		self.definebutton("q",      80,  40,    40,    40, ["keyboard"])
		self.definebutton("w",      80,  80,    40,    40, ["keyboard"])
		self.definebutton("e",      80, 120,    40,    40, ["keyboard"])
		self.definebutton("r",      80, 160,    40,    40, ["keyboard"])
		self.definebutton("t",      80, 200,    40,    40, ["keyboard"])
		self.definebutton("y",      80, 240,    40,    40, ["keyboard"])
		self.definebutton("u",      80, 280,    40,    40, ["keyboard"])
		self.definebutton("i",      80, 320,    40,    40, ["keyboard"])
		self.definebutton("o",      80, 360,    40,    40, ["keyboard"])
		self.definebutton("p",      80, 400,    40,    40, ["keyboard"])
		self.definebutton("enter2", 40, 440,    40,    40, ["keyboard"])




	def definebutton(self, buttonname, x, y, width, height, groupmembership):

		self.inputobject.createarea(buttonname, Vector.createfromvalues(x, y), Vector.createfromvalues(width, height), groupmembership)






	# ===========================================================================================================
	# Object Processing
	# ===========================================================================================================

	# ---------------------------------------------------------
	# RUN USER INPUT SCANNING SERVICE
	# Is run every cycle
	# Returns true if valid user input was detected
	# ---------------------------------------------------------

	def runinputcontrollerservice(self):

		# Default to no valid input detected
		outcome = False

		# Process all inputs in the eventlist
		self.inputobject.processinputs()

		return outcome



	# ===========================================================================================================
	# Get Information
	# ===========================================================================================================

	# -------------------------------------------------------------------
	# Returns whether the user has requested the application to end
	# -------------------------------------------------------------------

	def getquitstate(self):

		return self.inputobject.getquitstate()

