from ..common_components import Vector



def gethorizontalpositionlist(itemcountinteger, rowindex):

	if itemcountinteger == 1:
		if rowindex == 0:
			horlist = [192]
		else:
			horlist = [-999]
		
	elif itemcountinteger == 2:
		if rowindex == 0:
			horlist = [114, 270]
		else:
			horlist = [-999]
		
	elif itemcountinteger == 3:
		if rowindex == 0:
			horlist = [64, 192, 320]
		else:
			horlist = [-999]
		
	elif itemcountinteger == 4:
		if rowindex == 0:
			horlist = [27, 137, 247, 357]
		else:
			horlist = [-999]
		
	elif itemcountinteger == 5:
		if rowindex == 0:
			horlist = [64, 192, 320]
		else:
			horlist = [128, 211]
		
	elif itemcountinteger == 6:
		if rowindex == 0:
			horlist = [96, 192, 288]
		else:
			horlist = [96, 192, 288]

	elif itemcountinteger == 7:
		if rowindex == 0:
			horlist = [48, 144, 240, 336]
		else:
			horlist = [96, 192, 288]

	elif itemcountinteger == 8:
		if rowindex == 0:
			horlist = [48, 144, 240, 336]
		else:
			horlist = [48, 144, 240, 336]

	elif itemcountinteger == 9:
		if rowindex == 0:
			horlist = [0, 96, 192, 288, 384]
		else:
			horlist = [48, 144, 240, 336]
		
	elif itemcountinteger == 10:
		if rowindex == 0:
			horlist = [0, 96, 192, 288, 384]
		else:
			horlist = [0, 96, 192, 288, 384]
	else:
		print "Invalid item count"
		horlist = [-999]
	return horlist



def getverticalpositionlist(itemcountinteger):

	if itemcountinteger == 1:
		verlist = [130]
	elif itemcountinteger == 2:
		verlist = [92, 168]
	else:
		print "Invalid item count"
		verlist = [-999]
	return verlist



def getposition(itemindexinteger, itemcountinteger):

	totalitems = min(itemcountinteger, 10)
	
	
	if totalitems < 5:
		rows = 1
		firstrowcolcount = totalitems
	else:
		rows = 2
		firstrowcolcount = int((totalitems + 1) / 2)
		
	secondrowcolcount = totalitems - firstrowcolcount
	
	if itemindexinteger > (firstrowcolcount - 1):
		currentrow = 1
		currentcol = itemindexinteger - firstrowcolcount
	else:
		currentrow = 0
		currentcol = itemindexinteger
	
	verpositionlist = getverticalpositionlist(rows)
	horpositionlist = gethorizontalpositionlist(totalitems, currentrow)

	return Vector.createfromvalues(horpositionlist[currentcol], verpositionlist[currentrow])

	

def getoffset(itemindexinteger):

	if itemindexinteger == -1:
		ver = 2
		hor = 2
	elif itemindexinteger == 0:
		ver = 8
		hor = 28
	else:
		ver = 8 + (20 * (itemindexinteger - 1))
		hor = 8

	return Vector.createfromvalues(hor, ver)


	
def getboxdimensions():

	return Vector.createfromvalues(96, 76)
	
	

def getalertdimensions():

	return Vector.add(getboxdimensions(), Vector.createfromvalues(-4, -4))

	