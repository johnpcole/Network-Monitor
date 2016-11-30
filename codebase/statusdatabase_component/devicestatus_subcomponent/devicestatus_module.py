from . import devicestatus_class as DeviceStatusClass



# ---------------------------------------------
# Builds the device status object
# ---------------------------------------------

def createstatus(devicenamestring, imagenamestring, devicecategorystring):
	return DeviceStatusClass.DefineDeviceStatus(devicenamestring, imagenamestring, devicecategorystring)

