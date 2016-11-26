# ===========================================================================================================
# ???
# ===========================================================================================================

class DefineAlertItem:
	
	
	
	def __init__(self, devicename, changetype, alerttype):
		
		# 
		self.name = devicename
		
		# 
		self.changetype = changetype

		#
		self.alerttype = alerttype

		
	def getname(self):
		return self.name


	def getchangetype(self):
		return self.changetype


	def getalerttype(self):
		return self.alerttype