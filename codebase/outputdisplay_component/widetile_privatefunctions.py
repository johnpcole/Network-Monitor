from ..common_components.vector_datatype import vector_module as Vector



def getposition(itemindexinteger):

	colval = int(itemindexinteger / 2)
	rowval = itemindexinteger - (colval * 2)
	
	return Vector.createfromvalues(colval * 240, 244 + (rowval * 38))

	

def getoffset(itemindexinteger):

	if itemindexinteger == -1:
		ver = 2
		hor = 2
	elif itemindexinteger == 0:
		ver = 4
		hor = 4
	else:
		ver = 0
		hor = 38
		
	return Vector.createfromvalues(hor, ver)

	
	
def getboxdimensions():

	return Vector.createfromvalues(240, 38)
	
	

def getalertdimensions():

	return Vector.add(getboxdimensions(), Vector.createfromvalues(-4, -4))

	