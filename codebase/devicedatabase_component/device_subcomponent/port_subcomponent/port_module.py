from . import port_class as PortClass



# ---------------------------------------------
# Builds a Port Object
# ---------------------------------------------

def createport(macaddressobject, porttypestring):
	return PortClass.DefineMonitoredPort(macaddressobject, porttypestring)

