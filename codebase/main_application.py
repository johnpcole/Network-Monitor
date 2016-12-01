from statusdatabase_component import statusdatabase_module as StatusDatabase
from devicedatabase_component import devicedatabase_module as DeviceDatabase
from networkscanner_component import scanner_module as NetworkScanner
from inputcontroller_component import controller_module as InputController
from outputdisplay_component import display_module as DisplayDriver
from common_components.userinterface_framework import userinterface_module as GUI


def runapplication():

	GUI.init()



	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# Define objects used to drive application                                     #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	devicedatabase = DeviceDatabase.createdatabase()
	statusdatabase = StatusDatabase.createdatabase()
	networkscanner = NetworkScanner.createscanner()
	inputcontroller = InputController.createcontroller()
	displaydriver = DisplayDriver.createdisplay()

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# Run the application, processing each service in turn                         #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	while inputcontroller.getquitstate() == False:

		if inputcontroller.runinputcontrollerservice() == True:
			print "Input detected"

		networkscanner.runnetworkscanservice()

		devicedatabase.rundatabaseupdateservice(networkscanner)

		statusdatabase.rundatabaseupdateservice(devicedatabase)

		displaydriver.rundisplayoutputservice(statusdatabase, inputcontroller)

		inputcontroller.updatetilebuttons(statusdatabase, displaydriver)

	GUI.quit()
