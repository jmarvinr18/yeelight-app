import customtkinter as ctk
import tkinter as ttk
from bulbs import *
from PIL import Image
import os
from frames.RightSidebarFrame import *
from frames.home.main import *
from frames.SceneFrame import *
from frames.Device import *


class Route:
    def __init__(self, master, parent) -> None:

        self.right_frame = RightSideBarFrame(parent, width=600, height=250)

        self.list = [
            {
                "name": "Home",
                "image": "/Users/rouvinramoda/Documents/personal/lwa/yeelight-app/components/home.png",
                "menu": True
            },
            {
                "name": "Scene",
                "image": "/Users/rouvinramoda/Documents/personal/lwa/yeelight-app/components/scene.png",
                "menu": True

            },
            {
                "name": "Settings",
                "component": "",
                "image": "/Users/rouvinramoda/Documents/personal/lwa/yeelight-app/components/cog.png",
                "menu": True
            },

        ]

    def get_route_by_name(self, name):
        for i in self.list:
            if i["name"] == name:
                obj = i
        return obj
