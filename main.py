import customtkinter as ctk
import tkinter as ttk
from bulbs import *
from CTkListbox import *
from tkinter import colorchooser
import json
# from frames.RightSidebarFrame import *
from frames.LeftSideBarFrame import *
# from frames.home.main import *
from frames.SceneFrame import *
from components.Route import *


class App(ctk.CTk):

    def __init__(self, fg_color='#EFEFEF') -> None:
        super().__init__(fg_color)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        self.title('LWA Yeelight Control Panel')
        self.geometry("1050x700")
        self.switch_var = ctk.StringVar(value="on")
        self.resizable(False, False)

        LeftSideBarFrame(master=self, width=600, height=450)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")

        with open('selected-ip.json', 'r') as json_File:
            data = json.load(json_File)

        bulb = YeelightBulbs(data['ip'])

        bulb.set_rgb(color_code[0])

    def switch_event(self):

        with open('selected-ip.json', 'r') as json_File:
            data = json.load(json_File)

        bulb = YeelightBulbs(data['ip'])

        if self.switch_var.get() == 'on':
            bulb.turnOn()
        else:
            bulb.turnOff()


app = App()
app.mainloop()
