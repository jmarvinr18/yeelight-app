import customtkinter as ctk
import tkinter as ttk
from bulbs import *
from CTkListbox import *
from tkinter import colorchooser
import json
from frames.RightSidebarFrame import *
from frames.LeftSideBarFrame import *
from frames.HomeFrame import *
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



        # label1 = ctk.CTkLabel(home_frame.top_left_frame, text="ggyywer", font=(
        #     'Arial', 20), text_color="black", pady=3)
        # label1.grid(row=0, column=0, rowspan=2, padx=10,
        #             pady=30)
        # bulb = YeelightBulbs()

        # listbox = CTkListbox(self, command=bulb.changeIp, text_color=(
        #     "black", "white"), border_width=0)
        # listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # for b in bulb.detectBulbs():
        #     print(b)
        #     listbox.insert(b['ip'], b['ip'])




    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        
        with open('selected-ip.json', 'r') as json_File:
            data = json.load(json_File)

        bulb = YeelightBulbs(data['ip'])

        bulb.set_rgb(color_code[0])
        print(color_code[0])


        


    
    def switch_event(self):

        with open('selected-ip.json', 'r') as json_File:
            data = json.load(json_File)

        bulb = YeelightBulbs(data['ip'])
        print(self.switch_var.get())
        if self.switch_var.get() == 'on':
            bulb.turnOn()
        else:
            bulb.turnOff()



app = App()
app.mainloop()
