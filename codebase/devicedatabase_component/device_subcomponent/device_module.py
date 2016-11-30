from . import device_class as DeviceClass



# ---------------------------------------------
# Builds a Device object
# ---------------------------------------------

def createdevice(devicenamestring):
	return DeviceClass.DefineDevice(devicenamestring)

