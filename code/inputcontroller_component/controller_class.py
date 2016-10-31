from ..common_components import GUI



# ===========================================================================================================
# This class captures all user inputs using pygame.
# ===========================================================================================================

class InputController:



	def __init__(self):

		# Specifies whether the user has requested to close the application in this cycle
		self.quitstate = False



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

		# Loop over all events logged in this cycle
		for event in GUI.event.get():

			# Set quit game status if user closes the application window
			if event.type == GUI.QUIT:
				self.quitstate = True

		return outcome



	# ===========================================================================================================
	# Get Information
	# ===========================================================================================================

	# -------------------------------------------------------------------
	# Returns whether the user has requested the application to end
	# -------------------------------------------------------------------

	def getquitstate(self):

		return self.quitstate

