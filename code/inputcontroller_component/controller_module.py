from . import controller_class as InputControllerClass



# ---------------------------------------------
# Builds a Keyboard/Mouse controller object
# ---------------------------------------------

def createcontroller():
	return InputControllerClass.DefineInputController()

