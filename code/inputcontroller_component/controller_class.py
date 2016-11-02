from ..common_components import AppInput
from ..common_components import Vector

# ===========================================================================================================
# This class captures all user inputs using pygame.
# ===========================================================================================================

class InputController:



	def __init__(self):

		self.inputobject = AppInput.createappinput()
		self.setupbuttons()
		self.inputobject.setareastate("symbol", "Hidden")
		self.inputobject.setareastate("shift", "Hidden")
		self.inputobject.setareastate("keyboard", "Enabled")


	def setupbuttons(self):

#----------------------------------------------------------------------------------------------------------

		self.definebutton("shift-on",  280,   0,    80,    40, ["keyboard", "shift"])
		self.definebutton("z",         280,  80,    40,    40, ["keyboard"])
		self.definebutton("x",         280, 120,    40,    40, ["keyboard"])
		self.definebutton("c",         280, 160,    40,    40, ["keyboard"])
		self.definebutton("v",         280, 200,    40,    40, ["keyboard"])
		self.definebutton("b",         280, 240,    40,    40, ["keyboard"])
		self.definebutton("n",         280, 280,    40,    40, ["keyboard"])
		self.definebutton("m",         280, 320,    40,    40, ["keyboard"])
		self.definebutton("space",     280, 360,   120,    40, ["keyboard", "shift", "symbol"])

		self.definebutton("caps-on",   240,   0,    60,    40, ["keyboard", "shift"])
		self.definebutton("caps-off",  240,   0,    60,    40, [])
		self.definebutton("a",         240,  60,    40,    40, ["keyboard"])
		self.definebutton("s",         240, 100,    40,    40, ["keyboard"])
		self.definebutton("d",         240, 140,    40,    40, ["keyboard"])
		self.definebutton("f",         240, 180,    40,    40, ["keyboard"])
		self.definebutton("g",         240, 220,    40,    40, ["keyboard"])
		self.definebutton("h",         240, 260,    40,    40, ["keyboard"])
		self.definebutton("j",         240, 300,    40,    40, ["keyboard"])
		self.definebutton("k",         240, 340,    40,    40, ["keyboard"])
		self.definebutton("l",         240, 380,    40,    40, ["keyboard"])
		self.definebutton("enter1",    240, 420,    60,    40, ["keyboard", "shift", "symbol"])

		self.definebutton("symbol-on", 200,   0,    40,    40, ["keyboard", "shift"])
		self.definebutton("q",         200,  40,    40,    40, ["keyboard"])
		self.definebutton("w",         200,  80,    40,    40, ["keyboard"])
		self.definebutton("e",         200, 120,    40,    40, ["keyboard"])
		self.definebutton("r",         200, 160,    40,    40, ["keyboard"])
		self.definebutton("t",         200, 200,    40,    40, ["keyboard"])
		self.definebutton("y",         200, 240,    40,    40, ["keyboard"])
		self.definebutton("u",         200, 280,    40,    40, ["keyboard"])
		self.definebutton("i",         200, 320,    40,    40, ["keyboard"])
		self.definebutton("o",         200, 360,    40,    40, ["keyboard"])
		self.definebutton("p",         200, 400,    40,    40, ["keyboard"])
		self.definebutton("enter2",    200, 440,    40,    40, ["keyboard", "shift", "symbol"])

		self.definebutton("escape",    160,   0,    20,    40, ["keyboard", "shift", "symbol"])
		self.definebutton("1",         160,  20,    40,    40, ["keyboard", "shift"])
		self.definebutton("2",         160,  60,    40,    40, ["keyboard", "shift"])
		self.definebutton("3",         160, 100,    40,    40, ["keyboard", "shift"])
		self.definebutton("4",         160, 140,    40,    40, ["keyboard", "shift"])
		self.definebutton("5",         160, 180,    40,    40, ["keyboard", "shift"])
		self.definebutton("6",         160, 220,    40,    40, ["keyboard", "shift"])
		self.definebutton("7",         160, 260,    40,    40, ["keyboard", "shift"])
		self.definebutton("8",         160, 300,    40,    40, ["keyboard", "shift"])
		self.definebutton("9",         160, 340,    40,    40, ["keyboard", "shift"])
		self.definebutton("0",         160, 380,    40,    40, ["keyboard", "shift"])
		self.definebutton("backspace", 160, 420,    60,    40, ["keyboard", "shift", "symbol"])

#----------------------------------------------------------------------------------------------------------

		self.definebutton("shift-off", 280,   0,    80,    40, ["shift"])
		self.definebutton("Z",         280,  80,    40,    40, ["shift"])
		self.definebutton("X",         280, 120,    40,    40, ["shift"])
		self.definebutton("C",         280, 160,    40,    40, ["shift"])
		self.definebutton("V",         280, 200,    40,    40, ["shift"])
		self.definebutton("B",         280, 240,    40,    40, ["shift"])
		self.definebutton("N",         280, 280,    40,    40, ["shift"])
		self.definebutton("M",         280, 320,    40,    40, ["shift"])

		self.definebutton("A",         240,  60,    40,    40, ["shift"])
		self.definebutton("S",         240, 100,    40,    40, ["shift"])
		self.definebutton("D",         240, 140,    40,    40, ["shift"])
		self.definebutton("F",         240, 180,    40,    40, ["shift"])
		self.definebutton("G",         240, 220,    40,    40, ["shift"])
		self.definebutton("H",         240, 260,    40,    40, ["shift"])
		self.definebutton("J",         240, 300,    40,    40, ["shift"])
		self.definebutton("K",         240, 340,    40,    40, ["shift"])
		self.definebutton("L",         240, 380,    40,    40, ["shift"])

		self.definebutton("Q",         200,  40,    40,    40, ["shift"])
		self.definebutton("W",         200,  80,    40,    40, ["shift"])
		self.definebutton("E",         200, 120,    40,    40, ["shift"])
		self.definebutton("R",         200, 160,    40,    40, ["shift"])
		self.definebutton("T",         200, 200,    40,    40, ["shift"])
		self.definebutton("Y",         200, 240,    40,    40, ["shift"])
		self.definebutton("U",         200, 280,    40,    40, ["shift"])
		self.definebutton("I",         200, 320,    40,    40, ["shift"])
		self.definebutton("O",         200, 360,    40,    40, ["shift"])
		self.definebutton("P",         200, 400,    40,    40, ["shift"])

#----------------------------------------------------------------------------------------------------------

		self.definebutton("\\",        280,  80,    40,    40, ["symbol"])
		self.definebutton("<",         280, 120,    40,    40, ["symbol"])
		self.definebutton(">",         280, 160,    40,    40, ["symbol"])
		self.definebutton("?",         280, 200,    40,    40, ["symbol"])
		self.definebutton(",",         280, 240,    40,    40, ["symbol"])
		self.definebutton(".",         280, 280,    40,    40, ["symbol"])
		self.definebutton("/",         280, 320,    40,    40, ["symbol"])

		self.definebutton("¬",         240,  60,    40,    40, ["symbol"])
		self.definebutton("¦",         240, 100,    40,    40, ["symbol"])
		self.definebutton("|",         240, 140,    40,    40, ["symbol"])
		self.definebutton(":",         240, 180,    40,    40, ["symbol"])
		self.definebutton("@",         240, 220,    40,    40, ["symbol"])
		self.definebutton("~",         240, 260,    40,    40, ["symbol"])
		self.definebutton(";",         240, 300,    40,    40, ["symbol"])
		self.definebutton("'",         240, 340,    40,    40, ["symbol"])
		self.definebutton("#",         240, 380,    40,    40, ["symbol"])

		self.definebutton("symbol-off",200,   0,    40,    40, ["symbol"])
		self.definebutton("euro",         200,  40,    40,    40, ["symbol"])
		self.definebutton("_",         200,  80,    40,    40, ["symbol"])
		self.definebutton("+",         200, 120,    40,    40, ["symbol"])
		self.definebutton("-",         200, 160,    40,    40, ["symbol"])
		self.definebutton("=",         200, 200,    40,    40, ["symbol"])
		self.definebutton("`",         200, 240,    40,    40, ["symbol"])
		self.definebutton("{",         200, 280,    40,    40, ["symbol"])
		self.definebutton("}",         200, 320,    40,    40, ["symbol"])
		self.definebutton("[",         200, 360,    40,    40, ["symbol"])
		self.definebutton("]",         200, 400,    40,    40, ["symbol"])

		self.definebutton("!",         160,  20,    40,    40, ["symbol"])
		self.definebutton("quote",         160,  60,    40,    40, ["symbol"])
		self.definebutton("£",         160, 100,    40,    40, ["symbol"])
		self.definebutton("$",         160, 140,    40,    40, ["symbol"])
		self.definebutton("%",         160, 180,    40,    40, ["symbol"])
		self.definebutton("^",         160, 220,    40,    40, ["symbol"])
		self.definebutton("&",         160, 260,    40,    40, ["symbol"])
		self.definebutton("*",         160, 300,    40,    40, ["symbol"])
		self.definebutton("(",         160, 340,    40,    40, ["symbol"])
		self.definebutton(")",         160, 380,    40,    40, ["symbol"])

#----------------------------------------------------------------------------------------------------------




	def definebutton(self, buttonname, along, down, width, height, groupmembership):

		self.inputobject.createarea(buttonname, Vector.createfromvalues(down, along), Vector.createfromvalues(width, height), groupmembership)






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

		if self.inputobject.getmouseaction() == True:
			if self.inputobject.getmouseclickaction() == -1:
				if self.inputobject.getcurrentmouseareastate() == "Enabled":
					print self.inputobject.getcurrentmousearea()

		return outcome



	# ===========================================================================================================
	# Get Information
	# ===========================================================================================================

	# -------------------------------------------------------------------
	# Returns whether the user has requested the application to end
	# -------------------------------------------------------------------

	def getquitstate(self):

		return self.inputobject.getquitstate()

