import customtkinter as ctk
import tkinter as ttk
from bulbs import *
from PIL import Image
import os 
from frames.RightSidebarFrame import *
from frames.HomeFrame import *
from frames.SceneFrame import *
from frames.Device import *


class Route:
    def __init__(self, master, parent) -> None:
        
        right_frame = RightSideBarFrame(parent, width=600, height=250)

        self.list = [
            {
                "name": "Home",
                "component": HomeFrame(master=right_frame, width=600, height=250),
                "menu": True
            },
            {
                "name": "Scene",
                "component": SceneFrame(master=right_frame, width=600, height=250),
                "menu": True

            },
            {
                "name": "Settings",
                "component": "",
                "menu": True
            },

        ]

        file_path = os.path.dirname(os.path.realpath(__file__))
        self.image = customtkinter.CTkImage(light_image=Image.open(file_path + "/home-icon.png"),
                                          dark_image=Image.open(
                                              file_path + "/home-icon.png"),
                                       size=(20, 20))
        
        self.current_page = self.list[0]["component"]


    def get_route_by_name(self, name):
        for i in self.list:
            if i["name"] == name:
                obj = i
        return obj


    def get_current_page(self):
        return self.current_page
    
    def switch_page(self, page):
        self.hide_all_frames()
        self.current_page = page
        page.pack(
            fill="both", padx="30", pady="30", expand=True)
        page.mount_components()
        return True

    def hide_all_frames(self):
        for widget in self.current_page.winfo_children():
            widget.destroy()

        self.current_page.pack_forget()
