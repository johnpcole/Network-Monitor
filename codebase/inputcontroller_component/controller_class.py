from ..common_components.appinput_framework import appinput_module as AppInput
from ..common_components.vector_datatype import vector_module as Vector

# ===========================================================================================================
# This class captures all user inputs using pygame.
# ===========================================================================================================

class DefineInputController:



	def __init__(self):

		self.inputobject = AppInput.createappinput()
		self.setupbuttons()
		self.inputobject.setareastate("symbol", "Hidden")
		self.inputobject.setareastate("shift", "Hidden")
		self.inputobject.setareastate("keyboard", "Enabled")
		self.keyboardbuffer = ""
		self.keyboardstate = "On"     # Off On Shift Caps Symbol


	def setupbuttons(self):

#----------------------------------------------------------------------------------------------------------

		self.definebutton("shift-on",  281,   1,    78,    38, ["keyboard"])
		self.definebutton("z",         281,  81,    38,    38, ["keyboard"])
		self.definebutton("x",         281, 121,    38,    38, ["keyboard"])
		self.definebutton("c",         281, 161,    38,    38, ["keyboard"])
		self.definebutton("v",         281, 201,    38,    38, ["keyboard"])
		self.definebutton("b",         281, 241,    38,    38, ["keyboard"])
		self.definebutton("n",         281, 281,    38,    38, ["keyboard"])
		self.definebutton("m",         281, 321,    38,    38, ["keyboard"])
		self.definebutton("space",     281, 361,   118,    38, ["keyboard", "shift", "symbol"])

		self.definebutton("caps-on",   241,   1,    58,    38, ["keyboard", "shift"])
		self.definebutton("caps-off",  241,   1,    58,    38, [])
		self.definebutton("a",         241,  61,    38,    38, ["keyboard"])
		self.definebutton("s",         241, 101,    38,    38, ["keyboard"])
		self.definebutton("d",         241, 141,    38,    38, ["keyboard"])
		self.definebutton("f",         241, 181,    38,    38, ["keyboard"])
		self.definebutton("g",         241, 221,    38,    38, ["keyboard"])
		self.definebutton("h",         241, 261,    38,    38, ["keyboard"])
		self.definebutton("j",         241, 301,    38,    38, ["keyboard"])
		self.definebutton("k",         241, 341,    38,    38, ["keyboard"])
		self.definebutton("l",         241, 381,    38,    38, ["keyboard"])
		self.definebutton("enter1",    241, 421,    58,    38, ["keyboard", "shift", "symbol"])

		self.definebutton("symbol-on", 201,   1,    38,    38, ["keyboard", "shift"])
		self.definebutton("q",         201,  41,    38,    38, ["keyboard"])
		self.definebutton("w",         201,  81,    38,    38, ["keyboard"])
		self.definebutton("e",         201, 121,    38,    38, ["keyboard"])
		self.definebutton("r",         201, 161,    38,    38, ["keyboard"])
		self.definebutton("t",         201, 201,    38,    38, ["keyboard"])
		self.definebutton("y",         201, 241,    38,    38, ["keyboard"])
		self.definebutton("u",         201, 281,    38,    38, ["keyboard"])
		self.definebutton("i",         201, 321,    38,    38, ["keyboard"])
		self.definebutton("o",         201, 361,    38,    38, ["keyboard"])
		self.definebutton("p",         201, 401,    38,    38, ["keyboard"])
		self.definebutton("enter2",    201, 441,    38,    40, ["keyboard", "shift", "symbol"])

		self.definebutton("escape",    161,   1,    18,    38, ["keyboard", "shift", "symbol"])
		self.definebutton("1",         161,  21,    38,    38, ["keyboard", "shift"])
		self.definebutton("2",         161,  61,    38,    38, ["keyboard", "shift"])
		self.definebutton("3",         161, 101,    38,    38, ["keyboard", "shift"])
		self.definebutton("4",         161, 141,    38,    38, ["keyboard", "shift"])
		self.definebutton("5",         161, 181,    38,    38, ["keyboard", "shift"])
		self.definebutton("6",         161, 221,    38,    38, ["keyboard", "shift"])
		self.definebutton("7",         161, 261,    38,    38, ["keyboard", "shift"])
		self.definebutton("8",         161, 301,    38,    38, ["keyboard", "shift"])
		self.definebutton("9",         161, 341,    38,    38, ["keyboard", "shift"])
		self.definebutton("0",         161, 381,    38,    38, ["keyboard", "shift"])
		self.definebutton("backspace", 161, 421,    58,    38, ["keyboard", "shift", "symbol"])

#----------------------------------------------------------------------------------------------------------

		self.definebutton("shift-off", 281,   1,    78,    38, ["shift"])
		self.definebutton("Z",         281,  81,    38,    38, ["shift"])
		self.definebutton("X",         281, 121,    38,    38, ["shift"])
		self.definebutton("C",         281, 161,    38,    38, ["shift"])
		self.definebutton("V",         281, 201,    38,    38, ["shift"])
		self.definebutton("B",         281, 241,    38,    38, ["shift"])
		self.definebutton("N",         281, 281,    38,    38, ["shift"])
		self.definebutton("M",         281, 321,    38,    38, ["shift"])

		self.definebutton("A",         241,  61,    38,    38, ["shift"])
		self.definebutton("S",         241, 101,    38,    38, ["shift"])
		self.definebutton("D",         241, 141,    38,    38, ["shift"])
		self.definebutton("F",         241, 181,    38,    38, ["shift"])
		self.definebutton("G",         241, 221,    38,    38, ["shift"])
		self.definebutton("H",         241, 261,    38,    38, ["shift"])
		self.definebutton("J",         241, 301,    38,    38, ["shift"])
		self.definebutton("K",         241, 341,    38,    38, ["shift"])
		self.definebutton("L",         241, 381,    38,    38, ["shift"])

		self.definebutton("Q",         201,  41,    38,    38, ["shift"])
		self.definebutton("W",         201,  81,    38,    38, ["shift"])
		self.definebutton("E",         201, 121,    38,    38, ["shift"])
		self.definebutton("R",         201, 161,    38,    38, ["shift"])
		self.definebutton("T",         201, 201,    38,    38, ["shift"])
		self.definebutton("Y",         201, 241,    38,    38, ["shift"])
		self.definebutton("U",         201, 281,    38,    38, ["shift"])
		self.definebutton("I",         201, 321,    38,    38, ["shift"])
		self.definebutton("O",         201, 361,    38,    38, ["shift"])
		self.definebutton("P",         201, 401,    38,    38, ["shift"])

#----------------------------------------------------------------------------------------------------------

		self.definebutton("\\",        281,  81,    38,    38, ["symbol"])
		self.definebutton("<",         281, 121,    38,    38, ["symbol"])
		self.definebutton(">",         281, 161,    38,    38, ["symbol"])
		self.definebutton("?",         281, 201,    38,    38, ["symbol"])
		self.definebutton(",",         281, 241,    38,    38, ["symbol"])
		self.definebutton(".",         281, 281,    38,    38, ["symbol"])
		self.definebutton("/",         281, 321,    38,    38, ["symbol"])

		self.definebutton("NOT-USED",         241,  61,    38,    38, ["symbol"])
		self.definebutton("NOT-USED",         241, 101,    38,    38, ["symbol"])
		self.definebutton("|",         241, 141,    38,    38, ["symbol"])
		self.definebutton(":",         241, 181,    38,    38, ["symbol"])
		self.definebutton("@",         241, 221,    38,    38, ["symbol"])
		self.definebutton("~",         241, 261,    38,    38, ["symbol"])
		self.definebutton(";",         241, 301,    38,    38, ["symbol"])
		self.definebutton("'",         241, 341,    38,    38, ["symbol"])
		self.definebutton("#",         241, 381,    38,    38, ["symbol"])

		self.definebutton("symbol-off",201,   1,    38,    38, ["symbol"])
		self.definebutton("euro",         201,  41,    38,    38, ["symbol"])
		self.definebutton("_",         201,  81,    38,    38, ["symbol"])
		self.definebutton("+",         201, 121,    38,    38, ["symbol"])
		self.definebutton("-",         201, 161,    38,    38, ["symbol"])
		self.definebutton("=",         201, 201,    38,    38, ["symbol"])
		self.definebutton("`",         201, 241,    38,    38, ["symbol"])
		self.definebutton("{",         201, 281,    38,    38, ["symbol"])
		self.definebutton("}",         201, 321,    38,    38, ["symbol"])
		self.definebutton("[",         201, 361,    38,    38, ["symbol"])
		self.definebutton("]",         201, 401,    38,    38, ["symbol"])

		self.definebutton("!",         161,  21,    38,    38, ["symbol"])
		self.definebutton("quote",         161,  61,    38,    38, ["symbol"])
		self.definebutton("pound",         161, 101,    38,    38, ["symbol"])
		self.definebutton("$",         161, 141,    38,    38, ["symbol"])
		self.definebutton("%",         161, 181,    38,    38, ["symbol"])
		self.definebutton("^",         161, 221,    38,    38, ["symbol"])
		self.definebutton("&",         161, 261,    38,    38, ["symbol"])
		self.definebutton("*",         161, 301,    38,    38, ["symbol"])
		self.definebutton("(",         161, 341,    38,    38, ["symbol"])
		self.definebutton(")",         161, 381,    38,    38, ["symbol"])

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
					self.processvirtualkeyboard(self.inputobject.getcurrentmousearea())

		return outcome



	# -------------------------------------------------------------------
	# Processes the virtual keyboard
	# -------------------------------------------------------------------

	def processvirtualkeyboard(self, action):

		if (action == "enter1") or (action == "enter2"):
			print "ENTER PRESSED!"

		elif action == "shift-on":
			self.keyboardstate = "Shift"
			self.inputobject.setareastate("keyboard", "Hidden")
			self.inputobject.setareastate("shift", "Enabled")

		elif (action == "shift-off") or (action == "caps-off"):
			self.keyboardstate = "On"
			self.inputobject.setareastate("shift", "Hidden")
			self.inputobject.setareastate("keyboard", "Enabled")
			self.inputobject.setareastate("caps-off", "Hidden")
			self.inputobject.setareastate("caps-on", "Enabled")

		elif action == "caps-on":
			self.keyboardstate = "Caps"
			self.inputobject.setareastate("keyboard", "Hidden")
			self.inputobject.setareastate("shift", "Enabled")
			self.inputobject.setareastate("caps-on", "Hidden")
			self.inputobject.setareastate("caps-off", "Enabled")

		#elif action == "symbol-on":

		#elif action == "symbol-off":

		elif action == "backspace":
			if len(self.keyboardbuffer) > 0:
				self.keyboardbuffer = self.keyboardbuffer[:-1]

		#elif action == "escape":

		else:
			self.keyboardbuffer = self.keyboardbuffer + action
			if self.keyboardstate == "Shift":
				self.keyboardstate = "On"
				self.inputobject.setareastate("shift", "Hidden")
				self.inputobject.setareastate("keyboard", "Enabled")

		print self.keyboardbuffer

		return












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

