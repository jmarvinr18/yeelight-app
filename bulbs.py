from yeelight import discover_bulbs, Bulb
import customtkinter
from CTkListbox import *
import json


class YeelightBulbs:
    def __init__(self, ip=None) -> None:
        self.ip = ip
        self.bulb = Bulb(ip)

    def detectBulbs(self):
        bulbs = discover_bulbs()

        return bulbs

    def changeIp(self, ip):
        self.ip = ip
        ip_data = {"ip": ip}
        with open('selected-ip.json', 'w') as json_file:
            json.dump(ip_data, json_file, allow_nan=True)

    def turnOn(self):
        self.bulb.turn_on()

    def turnOff(self):
        self.bulb.turn_off()

    def getIp(self) -> str:
        return self.ip

    def set_rgb(self, rgb):
        r, g, b = rgb[0], rgb[1], rgb[2]
        self.bulb.set_rgb(r, g, b)

    def set_brightness(self, value):
        self.bulb.set_brightness(value)
