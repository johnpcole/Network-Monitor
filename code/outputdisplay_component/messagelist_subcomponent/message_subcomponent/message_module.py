from . import message_class as MessageClass



# ---------------------------------------------
# Builds a message object
# ---------------------------------------------

def createmessage(devicename, indexvalue, changereason, messagetype):
	return MessageClass.DefineDisplayMessage(devicename, indexvalue, changereason, messagetype)

