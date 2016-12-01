from ...common_components.datetime_datatypes import datetime_module as DateTime
from ...common_components.vector_datatype import vector_module as Vector


# ===========================================================================================================
# This class captures the status of an individual device
# ===========================================================================================================

class DefineDeviceStatus:

	def __init__(self, devicenamestring, imagenamestring, devicecategorystring):

		self.devicename = devicenamestring
		self.deviceimage = imagenamestring
		self.devicecategory = devicecategorystring
		self.connectionstate = {}
		self.connectionstate['Wired'] = False
		self.connectionstate['Wireless'] = False
		self.connectionstate['Unknown'] = False
		self.lastchanged = DateTime.createfromiso("20000101000000")
		self.changereason = 0



	def updateconnectionstatus(self, connectiontypestring, connectionstateboolean):

		outcome = 0
		oldstatus = self.connectionstate[connectiontypestring]
		if oldstatus != connectionstateboolean:
			if oldstatus == False:
				outcome = 1
			else:
				outcome = -1
		self.connectionstate[connectiontypestring] = connectionstateboolean
		return outcome
		

		
	def setchangelog(self, changedatetimeobject, changereasoninteger):

		self.lastchanged.setfromobject(changedatetimeobject)
		self.changereason = changereasoninteger
		


	def refreshinformation(self, deviceobject, updatedatetimeobject):
	
		oldconnectivity = self.getconnectionstatus("Any")
		change = False
		for porttype in ['Wired', 'Wireless', 'Unknown']:
			if 0 != self.updateconnectionstatus(porttype,
													deviceobject.porttypeseensince(updatedatetimeobject, porttype)):
				change = True

		connectivitychange = 0
		if self.getconnectionstatus("Any") == True:
			if oldconnectivity == False:
				connectivitychange = 1
		else:
			if oldconnectivity == True:
				connectivitychange = -1

		if change == True:
			self.setchangelog(updatedatetimeobject, connectivitychange)



	def getname(self):
	
		return self.devicename
	
	
	
	def getimage(self):
		
		return self.deviceimage



	def getcategory(self):

		return self.devicecategory

		

	def gettype(self):
	
		if self.devicecategory == "Unexpected":
			outcome = "Unknown"
		else:
			outcome = "Known"
		return outcome
		
		
		
	def getlastchangeddate(self):
	
		return self.lastchanged
		
	
	
	def haschangedsince(self, baselinedatetimeobject):
	
		if DateTime.isfirstlaterthansecond(self.lastchanged, baselinedatetimeobject) == True:
			outcome = True
		else:
			outcome = False
	
		return outcome



	def getalertstatus(self, baselinedatetimeobject):

		outcome = False
		if self.getforcedalertstatus() == True:
			outcome = True
		else:
			if self.haschangedsince(baselinedatetimeobject) == True:
				outcome = True

		return outcome



	def getforcedalertstatus(self):

		outcome = False
		if self.devicecategory == "Expected":
			if self.getconnectionstatus("Any") == False:
				outcome = True
		elif self.devicecategory == "Unexpected":
			if self.getconnectionstatus("Any") == True:
				outcome = True

		return outcome



	def getchangereason(self):

		return self.changereason



	def getconnectionstatus(self, connectiontypestring):

		outcome = False
		if connectiontypestring == "Any":
			connectiontypelist = ['Wired', 'Wireless', 'Unknown']
		else:
			connectiontypelist = [connectiontypestring]

		for connectiontype in connectiontypelist:
			if self.connectionstate[connectiontype] == True:
				outcome = True

		return outcome