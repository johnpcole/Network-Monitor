from button_subcomponent import DefineButton
from ...common_components import Vector
from ...common_components import GUI



class DefineApplicationInput:
	# ==========================================================================================
	# Object Setup
	# ==========================================================================================



	def __init__(self):

		self.buttons = {}

		self.quitstate = False

		# The location the mouse is positioned at
		# regardless of mouse click state
		self.mouselocation = Vector.createfromvalues(-999, -999)

		#self.mousesourcebutton = ""

		# The current button/area that the mouse location is positioned over 
		# regardless of mouse click state
		self.mousecurrentbutton = ""

		# Flag to indicate if mouse button is pressed
		#self.mousebuttonpressstate = False

		# Flag to indicate if rest of application needs to process changes
		# to the mouse
		self.mouseaction = False

		# Flag to indicate the current state of the mouse - Press / Release / Drag / Move
		self.mousestate = "Move"
		


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

		# Determine what kind of mouse action has occurred
		if event.type == GUI.MOUSEMOTION:
			action = "Move"
		elif event.type == GUI.MOUSEBUTTONDOWN:
			action = "Press"
		elif event.type == GUI.MOUSEBUTTONUP:
			action = "Release"
		else:
			action = "None"

			
		# Update the mouse position and action flags (if necessary)
		self.updatemouseposition(action)

		# Update the mouse state
		self.updatemousestate(action)


	# -------------------------------------------------------------------
	# Update the mouse state
	# -------------------------------------------------------------------

	def updatemousestate(self, action):

		oldmousestate = self.mousestate

		# If the mouse is currently being pressed or released, press/release
		if (action == "Press") or (action == "Release"):
			self.mousestate = action
		# If the mouse is currently being moved or not moved, drag/move based on previous state
		else:
			if (oldmousestate == "Press") or (oldmousestate == "Drag"):
				self.mousestate = "Drag"
			else:
				self.mousestate = "Move"



	# -------------------------------------------------------------------
	# Update mouse position and action
	# -------------------------------------------------------------------

	def updatemouseposition(self, action):


		if action == "None":
			self.mouseaction = False
		else:
			self.mouseaction = True
			self.mouselocation = Vector.createfrompair(event.pos)
			self.mousecurrentbutton = self.getcurrentmousebutton()



	# -------------------------------------------------------------------
	# Set button or buttongroup state
	# -------------------------------------------------------------------

	def setareastate(self, buttonname, newstate):

		if buttonname in self.buttons:
			self.buttons[buttonname].changestate(newstate)
		else:
			for button in self.buttons:
				button.changegroupstate(buttonname, newstate)



	# -------------------------------------------------------------------
	# Set button dimensions
	# -------------------------------------------------------------------

	def setareadimensions(self, buttonname, newposition, newdimensions):

		if buttonname in self.buttons:
			self.buttons[buttonname].changeboundary(newposition, newdimensions)
		else:
			print "Invalid button name - ", buttonname



	# -------------------------------------------------------------------
	# Add a button
	# -------------------------------------------------------------------

	def createarea(self, buttonname, buttonposition, buttondimensions, buttongroupmembership):

		if buttonname in self.buttons:
			print "Duplicate button name - ", buttonname
		else:
			self.buttons[buttonname] = DefineButton(buttonposition, buttondimensions, buttongroupmembership)



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

	def getcurrentmousearea(self):

		return self.mousecurrentbutton



	# -------------------------------------------------------------------
	# Returns the state of the button the mouse is currently over
	# -------------------------------------------------------------------

	def getcurrentmouseareastate(self):

		if self.mousecurrentbutton = "":
			outcome = ""
		else
			outcome = self.mousecurrentbutton.getstate()
		
		return outcome



	# -------------------------------------------------------------------
	# Returns whether a mouse action has occured
	# -------------------------------------------------------------------

	def getmouseaction(self):

		return self.mouseaction



	# -------------------------------------------------------------------
	# Returns what the current mouse state is
	# -------------------------------------------------------------------

	def getmousestate(self):

		return self.mousestate



	# -------------------------------------------------------------------
	# Returns the location of the mouse
	# -------------------------------------------------------------------

	def getmouselocation(self):

		return self.mouselocation



	# -------------------------------------------------------------------
	# Returns the state of the specified button
	# -------------------------------------------------------------------

	def getareastate(self, areaname):

		return self.buttons[areaname].getstate()



	# -------------------------------------------------------------------
	# Returns the current hovering button         - INTERNAL FUNCTION
	# Regardless of button state
	# -------------------------------------------------------------------

	def getcurrentmousebutton(self):

		outcome = ""
		for buttonname, button in self.buttons:
			if button.gethoverstate(self.mouseposition) != "":
				outcome = buttonname
		return outcome
	
