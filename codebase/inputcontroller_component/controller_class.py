from ..common_components.appinput_framework import appinput_module as AppInput
from ..common_components.vector_datatype import vector_module as Vector
from ..common_components.enumeration_datatype import enumeration_module as Enumeration


# ===========================================================================================================
# This class captures all user inputs using pygame.
# ===========================================================================================================

class DefineInputController:



	def __init__(self):

		self.inputobject = AppInput.createappinput()
		self.setupbuttons()
		self.inputobject.setareastate("symbol", "Hidden")
		self.inputobject.setareastate("shift", "Hidden")
		self.inputobject.setareastate("base", "Hidden")
		self.inputobject.setareastate("QUIT", "Enabled")
		self.inputobject.setareastate("devices", "Enabled")
		self.keyboardbuffer = ""
		self.keyboardstate = Enumeration.createenum(["Off", "On", "Shift", "Caps", "Symbol"], "Off")
		self.appmode = Enumeration.createenum(["Overview", "Device Detail"], "Overview")



	def setupbuttons(self):

#----------------------------------------------------------------------------------------------------------

		self.definebutton("shift-on",    3,  0, 4, 2, ["keyboard", "base"])
		self.definebutton("z",           3,  5, 2, 2, ["keyboard", "base"])
		self.definebutton("x",           3,  7, 2, 2, ["keyboard", "base"])
		self.definebutton("c",           3,  9, 2, 2, ["keyboard", "base"])
		self.definebutton("v",           3, 11, 2, 2, ["keyboard", "base"])
		self.definebutton("b",           3, 13, 2, 2, ["keyboard", "base"])
		self.definebutton("n",           3, 15, 2, 2, ["keyboard", "base"])
		self.definebutton("m",           3, 17, 2, 2, ["keyboard", "base"])
		self.definebutton("space",       3, 19, 6, 2, ["keyboard", "base", "shift", "symbol"])

		self.definebutton("caps-on",     2,  0, 3, 2, ["keyboard", "base", "shift"])
		self.definebutton("caps-off",    2,  0, 3, 2, ["keyboard"])
		self.definebutton("a",           2,  4, 2, 2, ["keyboard", "base"])
		self.definebutton("s",           2,  6, 2, 2, ["keyboard", "base"])
		self.definebutton("d",           2,  8, 2, 2, ["keyboard", "base"])
		self.definebutton("f",           2, 10, 2, 2, ["keyboard", "base"])
		self.definebutton("g",           2, 12, 2, 2, ["keyboard", "base"])
		self.definebutton("h",           2, 14, 2, 2, ["keyboard", "base"])
		self.definebutton("j",           2, 16, 2, 2, ["keyboard", "base"])
		self.definebutton("k",           2, 18, 2, 2, ["keyboard", "base"])
		self.definebutton("l",           2, 20, 2, 2, ["keyboard", "base"])
		self.definebutton("enter1",      2, 22, 3, 2, ["keyboard", "base", "shift", "symbol"])

		self.definebutton("symbol-on",   1,  0, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("q",           1,  3, 2, 2, ["keyboard", "base"])
		self.definebutton("w",           1,  5, 2, 2, ["keyboard", "base"])
		self.definebutton("e",           1,  7, 2, 2, ["keyboard", "base"])
		self.definebutton("r",           1,  9, 2, 2, ["keyboard", "base"])
		self.definebutton("t",           1, 11, 2, 2, ["keyboard", "base"])
		self.definebutton("y",           1, 13, 2, 2, ["keyboard", "base"])
		self.definebutton("u",           1, 15, 2, 2, ["keyboard", "base"])
		self.definebutton("i",           1, 17, 2, 2, ["keyboard", "base"])
		self.definebutton("o",           1, 19, 2, 2, ["keyboard", "base"])
		self.definebutton("p",           1, 21, 2, 2, ["keyboard", "base"])
		self.definebutton("enter2",      1, 23, 2, 3, ["keyboard", "base", "shift", "symbol"])

		self.definebutton("escape",      0,  0, 1, 2, ["keyboard", "base", "shift", "symbol"])
		self.definebutton("1",           0,  2, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("2",           0,  4, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("3",           0,  6, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("4",           0,  8, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("5",           0, 10, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("6",           0, 12, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("7",           0, 14, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("8",           0, 16, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("9",           0, 18, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("0",           0, 20, 2, 2, ["keyboard", "base", "shift"])
		self.definebutton("backspace",   0, 22, 3, 2, ["keyboard", "base", "shift", "symbol"])

#----------------------------------------------------------------------------------------------------------

		self.definebutton("shift-off",   3,  0, 4, 2, ["keyboard", "shift"])
		self.definebutton("Z",           3,  5, 2, 2, ["keyboard", "shift"])
		self.definebutton("X",           3,  7, 2, 2, ["keyboard", "shift"])
		self.definebutton("C",           3,  9, 2, 2, ["keyboard", "shift"])
		self.definebutton("V",           3, 11, 2, 2, ["keyboard", "shift"])
		self.definebutton("B",           3, 13, 2, 2, ["keyboard", "shift"])
		self.definebutton("N",           3, 15, 2, 2, ["keyboard", "shift"])
		self.definebutton("M",           3, 17, 2, 2, ["keyboard", "shift"])

		self.definebutton("A",           2,  4, 2, 2, ["keyboard", "shift"])
		self.definebutton("S",           2,  6, 2, 2, ["keyboard", "shift"])
		self.definebutton("D",           2,  8, 2, 2, ["keyboard", "shift"])
		self.definebutton("F",           2, 10, 2, 2, ["keyboard", "shift"])
		self.definebutton("G",           2, 12, 2, 2, ["keyboard", "shift"])
		self.definebutton("H",           2, 14, 2, 2, ["keyboard", "shift"])
		self.definebutton("J",           2, 16, 2, 2, ["keyboard", "shift"])
		self.definebutton("K",           2, 18, 2, 2, ["keyboard", "shift"])
		self.definebutton("L",           2, 20, 2, 2, ["keyboard", "shift"])

		self.definebutton("Q",           1,  3, 2, 2, ["keyboard", "shift"])
		self.definebutton("W",           1,  5, 2, 2, ["keyboard", "shift"])
		self.definebutton("E",           1,  7, 2, 2, ["keyboard", "shift"])
		self.definebutton("R",           1,  9, 2, 2, ["keyboard", "shift"])
		self.definebutton("T",           1, 11, 2, 2, ["keyboard", "shift"])
		self.definebutton("Y",           1, 13, 2, 2, ["keyboard", "shift"])
		self.definebutton("U",           1, 15, 2, 2, ["keyboard", "shift"])
		self.definebutton("I",           1, 17, 2, 2, ["keyboard", "shift"])
		self.definebutton("O",           1, 19, 2, 2, ["keyboard", "shift"])
		self.definebutton("P",           1, 21, 2, 2, ["keyboard", "shift"])

#----------------------------------------------------------------------------------------------------------

		self.definebutton(u"\u20ac",     3,  3, 2, 2, ["keyboard", "symbol"])
		self.definebutton("\\",          3,  5, 2, 2, ["keyboard", "symbol"])
		self.definebutton("<",           3,  7, 2, 2, ["keyboard", "symbol"])
		self.definebutton(">",           3,  9, 2, 2, ["keyboard", "symbol"])
		self.definebutton("?",           3, 11, 2, 2, ["keyboard", "symbol"])
		self.definebutton(",",           3, 13, 2, 2, ["keyboard", "symbol"])
		self.definebutton(".",           3, 15, 2, 2, ["keyboard", "symbol"])
		self.definebutton("/",           3, 17, 2, 2, ["keyboard", "symbol"])

		self.definebutton("`",           2,  3, 2, 2, ["keyboard", "symbol"])
		self.definebutton("|",           2,  5, 2, 2, ["keyboard", "symbol"])
		self.definebutton(":",           2,  7, 2, 2, ["keyboard", "symbol"])
		self.definebutton("@",           2,  9, 2, 2, ["keyboard", "symbol"])
		self.definebutton("~",           2, 11, 2, 2, ["keyboard", "symbol"])
		self.definebutton(";",           2, 13, 2, 2, ["keyboard", "symbol"])
		self.definebutton("'",           2, 15, 2, 2, ["keyboard", "symbol"])
		self.definebutton("#",           2, 17, 2, 2, ["keyboard", "symbol"])

		self.definebutton("symbol-off",  1,  0, 2, 2, ["keyboard", "symbol"])
		self.definebutton("_",           1,  3, 2, 2, ["keyboard", "symbol"])
		self.definebutton("+",           1,  5, 2, 2, ["keyboard", "symbol"])
		self.definebutton("-",           1,  7, 2, 2, ["keyboard", "symbol"])
		self.definebutton("=",           1,  9, 2, 2, ["keyboard", "symbol"])
		self.definebutton("{",           1, 11, 2, 2, ["keyboard", "symbol"])
		self.definebutton("}",           1, 13, 2, 2, ["keyboard", "symbol"])
		self.definebutton("[",           1, 15, 2, 2, ["keyboard", "symbol"])
		self.definebutton("]",           1, 17, 2, 2, ["keyboard", "symbol"])

		self.definebutton("!",           0,  2, 2, 2, ["keyboard", "symbol"])
		self.definebutton("\"",          0,  4, 2, 2, ["keyboard", "symbol"])
		self.definebutton(u"\xA3",       0,  6, 2, 2, ["keyboard", "symbol"])
		self.definebutton("$",           0,  8, 2, 2, ["keyboard", "symbol"])
		self.definebutton("%",           0, 10, 2, 2, ["keyboard", "symbol"])
		self.definebutton("^",           0, 12, 2, 2, ["keyboard", "symbol"])
		self.definebutton("&",           0, 14, 2, 2, ["keyboard", "symbol"])
		self.definebutton("*",           0, 16, 2, 2, ["keyboard", "symbol"])
		self.definebutton("(",           0, 18, 2, 2, ["keyboard", "symbol"])
		self.definebutton(")",           0, 20, 2, 2, ["keyboard", "symbol"])

#----------------------------------------------------------------------------------------------------------

		self.definebutton("QUIT", 1, 1, 478, 50, [])

		self.definebutton("device-known-0", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-1", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-2", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-3", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-4", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-5", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-6", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-7", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-8", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-known-9", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-unknown-0", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-unknown-1", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-unknown-2", -100, -100, 10, 10, ["devices"])
		self.definebutton("device-unknown-3", -100, -100, 10, 10, ["devices"])

# ----------------------------------------------------------------------------------------------------------






	def definebutton(self, buttonname, down, along, width, height, groupmembership):

		if "keyboard" in groupmembership:
			buttonposition = Vector.createfromvalues((along * 19) + 5, 168 + (38 * down))
			buttonsize = Vector.createfromvalues((width * 19) - 2, (height * 19) - 2)
			if along == 0:
				buttonposition = Vector.add(buttonposition, Vector.createfromvalues(-3, 0))
				buttonsize = Vector.add(buttonsize, Vector.createfromvalues(22, 0))
			if height == 3:
				buttonsize = Vector.add(buttonsize, Vector.createfromvalues(0, -17))
		else:
			buttonposition = Vector.createfromvalues(along, down)
			buttonsize = Vector.createfromvalues(width, height)
		self.inputobject.createarea(buttonname, buttonposition, buttonsize, groupmembership)



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
					if self.inputobject.getcurrentmousearea() == "QUIT":
						self.inputobject.forcequit()
					else:
						if self.keyboardstate.get("Off") == False:
							self.processvirtualkeyboard(self.inputobject.getcurrentmousearea())
						else:
							self.processtileclicks(self.inputobject.getcurrentmousearea())

		return outcome



	# -------------------------------------------------------------------
	# Processes the virtual keyboard
	# -------------------------------------------------------------------

	def processvirtualkeyboard(self, action):

		if (action == "enter1") or (action == "enter2"):
			print "ENTER PRESSED!"

		elif action == "shift-on":
			self.keyboardstate.set("Shift")
			self.inputobject.setareastate("base", "Hidden")
			self.inputobject.setareastate("shift", "Enabled")

		elif (action == "shift-off") or (action == "caps-off"):
			self.keyboardstate.set("On")
			self.inputobject.setareastate("shift", "Hidden")
			self.inputobject.setareastate("base", "Enabled")
			self.inputobject.setareastate("caps-off", "Hidden")
			self.inputobject.setareastate("caps-on", "Enabled")

		elif action == "caps-on":
			self.keyboardstate.set("Caps")
			self.inputobject.setareastate("base", "Hidden")
			self.inputobject.setareastate("shift", "Enabled")
			self.inputobject.setareastate("caps-on", "Hidden")
			self.inputobject.setareastate("caps-off", "Enabled")

		elif action == "symbol-on":
			self.keyboardstate.set("Symbol")
			self.inputobject.setareastate("base", "Hidden")
			self.inputobject.setareastate("shift", "Hidden")
			self.inputobject.setareastate("caps-off", "Hidden")
			self.inputobject.setareastate("symbol", "Enabled")

		elif action == "symbol-off":
			self.keyboardstate.set("On")
			self.inputobject.setareastate("symbol", "Hidden")
			self.inputobject.setareastate("base", "Enabled")

		elif action == "backspace":
			if len(self.keyboardbuffer) > 0:
				self.keyboardbuffer = self.keyboardbuffer[:-1]

		#elif action == "escape":

		else:
			self.keyboardbuffer = self.keyboardbuffer + action
			if self.keyboardstate.get( "Shift") == True:
				self.keyboardstate.set("On")
				self.inputobject.setareastate("shift", "Hidden")
				self.inputobject.setareastate("base", "Enabled")

		print self.keyboardbuffer

		return




	# -------------------------------------------------------------------
	# Processes tile button clicks
	# -------------------------------------------------------------------

	def processtileclicks(self, action):

		#if (action == "enter1") or (action == "enter2"):
		print "TILE CLICKED! ", action

		self.appmode.set("Device Detail")




	# -------------------------------------------------------------------
	# Updates the tile buttons based on which tiles are displayed
	# -------------------------------------------------------------------

	def updatetilebuttons(self, statusdatabase, displaydriver):

		knowntotal = statusdatabase.getprioritisedstatuscount("Known")
		unknowntotal = statusdatabase.getprioritisedstatuscount("Unknown")

		for knownindex in range(0, 10):
			if knownindex < knowntotal:
				buttonposition, buttonsize = displaydriver.gettiledimensions(knownindex, knowntotal, "Narrow")
			else:
				buttonposition = Vector.createblank()
				buttonsize = Vector.createfromvalues(10, 10)
			self.inputobject.setareadimensions("device-known-" + str(knownindex), buttonposition, buttonsize)

		for unknownindex in range(0, 4):
			if unknownindex < unknowntotal:
				buttonposition, buttonsize = displaydriver.gettiledimensions(unknownindex, unknowntotal, "Wide")
			else:
				buttonposition = Vector.createblank()
				buttonsize = Vector.createfromvalues(10, 10)
			self.inputobject.setareadimensions("device-unknown-" + str(unknownindex), buttonposition, buttonsize)




	# ===========================================================================================================
	# Get Information
	# ===========================================================================================================

	# -------------------------------------------------------------------
	# Returns whether the user has requested the application to end
	# -------------------------------------------------------------------

	def getquitstate(self):

		return self.inputobject.getquitstate()



	# -------------------------------------------------------------------
	# Returns the set of buttons in a group
	# -------------------------------------------------------------------

	def getbuttoncollection(self, groupname):

		return self.inputobject.getbuttoncollection(groupname)



	# -------------------------------------------------------------------
	# Returns the button's state
	# -------------------------------------------------------------------

	def getbuttonstate(self, buttonname):

		return self.inputobject.getareastate(buttonname)



	# -------------------------------------------------------------------
	# Returns the button's position
	# -------------------------------------------------------------------

	def getbuttonposition(self, buttonname):
		return self.inputobject.getareaposition(buttonname)



	# -------------------------------------------------------------------
	# Returns the button's size
	# -------------------------------------------------------------------

	def getbuttonsize(self, buttonname):

		return self.inputobject.getareadimensions(buttonname)



	# -------------------------------------------------------------------
	# Returns the keyboard state
	# -------------------------------------------------------------------

	def getkeyboardstate(self, desiredvalue):

		return self.keyboardstate.get(desiredvalue)


	# -------------------------------------------------------------------
	# Returns the application mode
	# -------------------------------------------------------------------

	def getappmode(self, desiredvalue):

		return self.appmode.get(desiredvalue)

