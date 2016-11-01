from ..common_components import AppInput


# ===========================================================================================================
# This class captures all user inputs using pygame.
# ===========================================================================================================

class InputController:



	def __init__(self):

		self.inputobject = AppInput.createappinput()



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

