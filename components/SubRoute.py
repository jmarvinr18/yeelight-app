import customtkinter as ctk
import tkinter as ttk
from bulbs import *
from PIL import Image
import os
from frames.RightSidebarFrame import *
from frames.Device import *


class SubRoute:
    def __init__(self, master, parent) -> None:

        right_frame = RightSideBarFrame(parent, width=600, height=250)

        self.list = [
            {
                "name": "Device",
                "component": Device(master=right_frame, width=600, height=250),
                "menu": False
            },
        ]

        self.current_page = self.list[0]["component"]

    def get_route_by_name(self, name):
        for i in self.list:
            if i["name"] == name:
                obj = i
        return obj

    def get_current_page(self):
        return self.current_page

    def switch_page(self, page):
        self.current_page.pack_forget()
        self.current_page = page
        self.current_page.pack(
            fill="both", padx="30", pady="30", expand=True)
        return True
