from message_subcomponent import message_module as DisplayMessage


class DefineMessageList:

	def __init__(self):

		self.messages = []
		self.currentmessage = -999



	def updatemessagelist(self, recentlychangedlist, safetodeletecurrent):

		#Add new
		for recentitem in recentlychangedlist:
			recentname = recentitem.getname()
			changereason = recentitem.getchangetype()
			existingmessage = self.getmessagefromcombo(recentname, changereason)
			if existingmessage is None:
				self.addmessage(recentname, changereason, recentitem.getalerttype())

		#Delete old
		for existingmessage in self.messages:
			messagename = existingmessage.getname()
			messagereason = existingmessage.getchangereason()
			recentfound = False
			for recentitem in recentlychangedlist:
				if recentitem.getname() == messagename:
					if recentitem.getchangetype() == messagereason:
						recentfound = True
			if recentfound == False:
				self.deletemessage(messagename, messagereason, safetodeletecurrent)

		if self.getmessagecount() > 0:
			outcome = True
		else:
			outcome = False

		return outcome



	def addmessage(self, devicename, changereason, messagetype):

		devicesearch = self.getmessagefromcombo(devicename, changereason)

		if devicesearch is None:
			self.messages.append(DisplayMessage.createmessage(devicename, 1 + self.getmessagecount(), changereason,
																										messagetype))
			if self.getmessagecount() == 1:
				self.currentmessage = 1



	def deletemessage(self, devicename, changereason, safetodeleteflag):

		currentdevice = self.getcurrentmessage()

		devicesearch = self.getmessagefromcombo(devicename, changereason)

		if devicesearch is not None:
			if (devicesearch != currentdevice) or (safetodeleteflag == True):
				self.messages.remove(devicesearch)
				self.repairordering()
				self.repaircurrentmessage(currentdevice)



	def repaircurrentmessage(self, currentdevice):

		if self.getmessagecount() == 0:
			self.currentmessage = -999
		else:
			self.currentmessage = currentdevice.getorder()



	def repairordering(self):

		messageindex = 0
		for message in self.messages:
			messageindex = messageindex + 1
			message.resetorder(messageindex)



	def getmessagecount(self):

		return len(self.messages)



	def getmessagefromcombo(self, devicename, changereason):
		outcome = None
		for message in self.messages:
			if message.getname() == devicename:
				if message.getchangereason() == changereason:
					outcome = message
		return outcome



	def getmessagefromindex(self, indexvalue):
		outcome = None
		for message in self.messages:
			if message.getorder() == indexvalue:
				outcome = message
		return outcome



	def changemessage(self):
		if self.getmessagecount() > 0:
			self.currentmessage = self.currentmessage + 1
			if self.currentmessage > self.getmessagecount():
				self.currentmessage = 1
		else:
			self.currentmessage = -999
		return self.getcurrentmessagetext()



	def getcurrentmessage(self):
		return self.getmessagefromindex(self.currentmessage)



	def getcurrentmessagetext(self):
		currentdevice = self.getcurrentmessage()
		if currentdevice is None:
			outcome = "! NO DEVICE !"
		else:
			outcome = currentdevice.getmessagetext()
		return outcome


	def getcurrentmessagetype(self):
		currentdevice = self.getcurrentmessage()
		return currentdevice.getmessagetype()