from ...common_components import DateTime



# ===========================================================================================================
# This class captures the status of an individual device
# ===========================================================================================================

class DeviceStatus:

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
				outcome = 0
		self.connectionstate[connectiontypestring] = connectionstateboolean
		return outcome
		

		
	def setchangelog(self, changedatetimeobject, changereasoninteger):

		self.lastchanged.setfromobject(changedatetimeobject)
		self.changereason = changereasoninteger

		
		


	def refreshinformation(self, deviceobject, updatedatetimeobject):
	
		connectivitychange = 0
		anychange = False
		for porttype in ['Wired', 'Wireless', 'Unknown']:
			currentchange = self.updateconnectionstatus(porttype,
														deviceobject.porttypeseensince(updatedatetimeobject, porttype))
			if currentchange != 0:
				anychange = True
			connectivitychange = connectivitychange + currentchange
		if anychange == True:
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
	
		if DateTime.isfirstlaterthansecond(self.lastchanged, baselinedatetimeobject):
			outcome = True
		else:
			outcome = False
	
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