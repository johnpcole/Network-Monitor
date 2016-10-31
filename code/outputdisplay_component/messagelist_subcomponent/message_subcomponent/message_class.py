class DisplayMessage:

	def __init__(self, devicename, indexvalue, changereason, messagetype):

		self.devicename = devicename
		self.order = indexvalue
		self.changereason = changereason
		self.messagetype = messagetype



	def getname(self):
		return self.devicename

	def resetorder(self, newvalue):
		self.order = newvalue

	def getorder(self):
		return self.order

	def getmessagetext(self):
		if self.changereason == 1:
			outcome = self.devicename + " is online"
		elif self.changereason == -1:
			outcome = self.devicename + " is offline"
		else:
			outcome = self.devicename + " is updated"

		return outcome

	def getchangereason(self):
		return self.changereason

	def getmessagetype(self):
		return self.messagetype