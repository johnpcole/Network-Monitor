from ....common_components import Vector


class DefineButton:
	# ==========================================================================================
	# Object Setup
	# ==========================================================================================



	def __init__(self, buttonposition, buttondimensions, buttongroupmembership):

		# pixel location of button
		self.position = buttonposition

		# pixel size of button
		self.dimensions = buttondimensions

		# state of button - Can be Hidden, Disabled, or Enabled
		self.state = "Hidden"

		# any membership of button groups
		self.groups = buttongroupmembership





	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Change a button's boundary
	# -------------------------------------------------------------------
	
	def changeboundary(self, newposition, newdimensions):

		self.position = newposition
		self.dimensions = newdimensions



	# -------------------------------------------------------------------
	# Change a button's state
	# -------------------------------------------------------------------

	def changestate(self, newstate):

		if (newstate == "Hidden") or (newstate == "Enabled") or (newstate == "Disabled"):
			self.state = newstate
		else:
			print "Invalid button state - ", newstate


	# -------------------------------------------------------------------
	# Change multiple button states
	# -------------------------------------------------------------------

	def changegroupstate(self, groupname, newstate):

		for groupitem in self.groups:
			if groupitem == groupname:
				self.changestate(newstate)



	# ==========================================================================================
	# Get Information
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Returns the state of the button
	# -------------------------------------------------------------------

	def getstate(self):

		return self.state



	# -------------------------------------------------------------------
	# Returns whether the specified location is in the button boundary
	# and if so, returns the state
	# -------------------------------------------------------------------

	def gethoverstate(self, mouseposition):

		if Vector.ispointinarea(mouseposition, self.position, self.dimensions) == True:
			outcome = self.state
		else:
			outcome = ""

		return outcome




