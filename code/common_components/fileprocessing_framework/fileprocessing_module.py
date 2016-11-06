# ---------------------------------------------------------
# Opens and reads a file into a simple string list
# ---------------------------------------------------------

def readfromdisk(filename):

	outcome = []

	try:
		# Open the file for the duration of this process
		with open(filename) as fileobject:
			
			# Loop over all lines in the file
			for fileline in fileobject.readlines():
				
				# Only add data if the line isn't blank
				if fileline != "":
				
					# Attempt to extract useful information, if possible
					outcome.append(fileline.rstrip('\r\n'))

	except:
		# Print an error if the file cannot be read
		print "Cannot read file - ", filename
		
	return outcome

