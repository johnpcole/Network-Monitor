from button_subcomponent import DefineButton
from ...common_components import Vector
from ...common_components import GUI



class DefineApplicationInput:
	# ==========================================================================================
	# Object Setup
	# ==========================================================================================



	def __init__(self):

#		self.mouse = DefineMouseInformation()

#		self.keys = DefineKeyboardInformation()

		self.buttons = {}

		self.quitstate = False

		self.mouselocation = Vector.createfromvalues(-999, -999)

		#self.mousesourcebutton = ""

		self.mousecurrentbutton = ""

		self.mousebuttonpressstate = False

		self.mouseaction = False



	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Interprets input events for this cycle
	# -------------------------------------------------------------------

	def processinputs(self):

		# Loop over all events logged in this cycle
		for event in GUI.event.get():

			# Set quit game status if user closes the application window
			self.processquit(event)

			# Process keyboard actions
			self.processkey(event)

			# Process mouse actions
			self.processmouse(event)

		return 0



	# -------------------------------------------------------------------
	# Process keyboard
	# -------------------------------------------------------------------

	def processquit(self, event):

		# Set quit game status if user closes the application window
		if event.type == GUI.QUIT:
			self.quitstate = True



	# -------------------------------------------------------------------
	# Process keyboard
	# -------------------------------------------------------------------

	def processkey(self, event):

		if event.type == GUI.KEYDOWN:
			action = "Press"
		elif event.type == GUI.KEYUP:
			action = "Release"
		else:
			action = "None"

		if action != "None":
			keyname = event.key
			keylabel = keyname[2:]
			if keylabel[:2] == "KP":
				keylabel = keylabel[2:]
			if keylabel[:1] == "_":
				keylabel = keylabel[1:]
			keylabel.upper()

			#UNFINISHED!



	# -------------------------------------------------------------------
	# Process mouse
	# -------------------------------------------------------------------

	def processmouse(self, event):

		if event.type == GUI.MOUSEMOTION:
			action = "Move"
		elif event.type == GUI.MOUSEBUTTONDOWN:
			action = "Press"
		elif event.type == GUI.MOUSEBUTTONUP:
			action = "Release"
		else:
			action = "None"

		if action == "None":
			self.mouseaction = False
		else:
			self.mouseaction = True
			self.mouselocation = Vector.createfrompair(event.pos)
			if action == "Press":
				currentbutton = self.getcurrentmousebutton()


				self.mouse





		elif action == "Release":

		else:







	# -------------------------------------------------------------------
	# Set button or buttongroup state
	# -------------------------------------------------------------------

	def setbuttonstate(self, buttonname, newstate):

		if buttonname in self.buttons:
			self.buttons[buttonname].changestate(newstate)
		else:
			for button in self.buttons:
				button.changegroupstate(buttonname, newstate)



	# ==========================================================================================
	# Get Information
	# ==========================================================================================





	# -------------------------------------------------------------------
	# Returns whether the user has requested the application to end
	# -------------------------------------------------------------------

	def getquitstate(self):

		return self.quitstate



	# -------------------------------------------------------------------
	# Returns which button the mouse is currently over
	# -------------------------------------------------------------------

	def getmousearea(self):

		return self.mousecurrentbutton



	# -------------------------------------------------------------------
	# Returns whether a mouse action has occured
	# -------------------------------------------------------------------

	def getmouseaction(self):

		return self.mouseaction



	# -------------------------------------------------------------------
	# Returns the location of the mouse
	# -------------------------------------------------------------------

	def getmouselocation(self):

		return self.mouselocation



	# -------------------------------------------------------------------
	# Returns the current hovering button - INTERNAL FUNCTION
	# -------------------------------------------------------------------

	def getcurrentmousebutton(self):

		outcome = ""
		for buttonname, button in self.buttons:
			if button.gethoverstate(self.mouseposition) != "":
				outcome = buttonname
		return outcome