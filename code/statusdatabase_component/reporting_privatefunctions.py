from priorityitem_subcomponent import PriorityItem
from alertitem_subcomponent import AlertItem
from ..common_components import DateTime
import operator as ListFunction



# ---------------------------------------------------------
# This method returns the top x known and top y unknown
# devices in the database
# ---------------------------------------------------------

def getprioritisedstatuslist(statusdevicelist, knownlimit, unknownlimit):

	prioritylist = populatenamelists(statusdevicelist)

	prioritylist['FinalPriorityList'] = populateprioritisednamelist(['Expected-Off', 'Expected-On', 'Optional-On',
																			'Optional-Off'], prioritylist, knownlimit)

	prioritylist['FinalPriorityList'] = populateprioritisednamelist(['Unexpected-On', 'Unexpected-Off'],
																							prioritylist, unknownlimit)

	return createprioritisedstatuslist(statusdevicelist, prioritylist['FinalPriorityList'])
	
# ---------------------------------------------------------
# 
# ---------------------------------------------------------

def createprioritisedstatuslist(statusdevicelist, prioritynamelist):
	
	outcome = []
	
	for statusdevice in statusdevicelist:
	
		for prioritisedname in prioritynamelist:
			if statusdevice.getname() == prioritisedname:
			
				outcome.append(statusdevice)
	
	return outcome


# ---------------------------------------------------------
# 
# ---------------------------------------------------------


def createnamelists():
	
	prioritylist = {}
	prioritylist['Expected-On'] = []
	prioritylist['Expected-Off'] = []
	prioritylist['Optional-On'] = []
	prioritylist['Optional-Off'] = []
	prioritylist['Unexpected-On'] = []
	prioritylist['Unexpected-Off'] = []
	prioritylist['FinalPriorityList'] = []

	return prioritylist
	
	
	
# ---------------------------------------------------------
# 
# ---------------------------------------------------------
	
def populatenamelists(statusdevicelist):

	currentdatetime = DateTime.getnow()

	prioritylist = createnamelists()

	for statusdevice in statusdevicelist:
	
		if statusdevice.getconnectionstatus("Any") == True:
			prioritylistname = statusdevice.getcategory() + "-On"
		else:
			prioritylistname = statusdevice.getcategory() + "-Off"
		
		datelastchanged = DateTime.secondsdifference(currentdatetime, statusdevice.getlastchangeddate())
		
		prioritylist[prioritylistname].append(PriorityItem(statusdevice.getname(), datelastchanged.getsecondsvalue()))
		
	return prioritylist

	
	
# ---------------------------------------------------------
# 
# ---------------------------------------------------------

def populateprioritisednamelist(sublistnames, prioritylist, listsizelimit):

	prioritydevicecount = 0
	templist = prioritylist['FinalPriorityList']
	for prioritylistname in sublistnames:
		prioritylist[prioritylistname].sort(key=ListFunction.attrgetter('secondssincelastchanged'))
		for pitem in prioritylist[prioritylistname]:
			prioritydevicecount = prioritydevicecount + 1
			if prioritydevicecount < listsizelimit + 1:
				templist.append(pitem.getname())
	return templist



# ---------------------------------------------------------
#
# ---------------------------------------------------------

def getalertitems(statusdevicelist, datetimethreshold):

	outcome = []
	for device in statusdevicelist:
		if device.getalertstatus(datetimethreshold) == True:
			if device.getforcedalertstatus() == True:
				alerttype = "alert"
			else:
				alerttype = "info"
			outcome.append(AlertItem(device.getname(), device.getchangereason(), alerttype))

	return outcome