

class Devices:
    name = "devices"
    column = ("ip TEXT", "port TEXT", "capabilities TEXT")


device = Devices

for i in device.column:
    print(i)
