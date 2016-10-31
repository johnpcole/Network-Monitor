# ===========================================================================================================
# ???
# ===========================================================================================================

class PriorityItem:
	
	
	
	def __init__(self, devicename, integersecondssincelastchanged):
		
		# 
		self.name = devicename
		
		# 
		self.secondssincelastchanged = integersecondssincelastchanged
		

		
	def getname(self):
		return self.name