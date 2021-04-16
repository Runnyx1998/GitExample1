class Device:
    ipAddress = ""
    port = ""

    @staticmethod
    def findDevices():
        devices = []

        d = Device()
        d.ipAddress = "192.168.1.5"
        d.port = "21"

        devices.append(d)

        d = Device()
        d.ipAddress = "10.0.0.1"
        d.port = "8"

        devices.append(d)

        d = Device()
        d.ipAddress = "172.16.10.2"
        d.port = "30"

        devices.append(d)

        return devices

class DevicesView:
    def showDevices(self,devices):
        for d in devices:
            print("--------")
            print("IP Address: " + d.ipAddress)
            print("Port: " + str(d.port))
            print("--------")

class DevicesController:
    def __init__(self):
        devices = Device.findDevices()
        v = DevicesView()
        v.showDevices(devices)

c = DevicesController()



