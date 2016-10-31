from statusdatabase_component import StatusDatabase
from devicedatabase_component import DeviceDatabase
from networkscanner_component import NetworkScanner
from inputcontroller_component import InputController
from outputdisplay_component import DisplayDriver
from common_components import GUI


def runapplication():

	GUI.init()



	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# Define objects used to drive application                                     #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	devicedatabase = DeviceDatabase()
	statusdatabase = StatusDatabase()
	networkscanner = NetworkScanner()
	inputcontroller = InputController()
	displaydriver = DisplayDriver()

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
	# Run the application, processing each service in turn                         #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

	while inputcontroller.getquitstate() == False:

		if inputcontroller.runinputcontrollerservice() == True:
			print "Input detected"

		networkscanner.runnetworkscanservice()

		devicedatabase.rundatabaseupdateservice(networkscanner)

		statusdatabase.rundatabaseupdateservice(devicedatabase)

		displaydriver.rundisplayoutputservice(statusdatabase)



	GUI.quit()
