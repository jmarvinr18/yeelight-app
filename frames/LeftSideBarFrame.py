import customtkinter as ctk
from components.Route import *
import tkinter as tk
import tkinter as ttk
from tkinter.font import Font
from frames.home import *


class LeftSideBarFrame(ctk.CTkFrame):

    def __init__(self, master, width, height) -> None:
        super().__init__(master, width, height, fg_color="#E0C34C")
        self.pack(side="left", fill="both", ipadx=20)

        self.route = Route(self, master)

        self.display_menus()

        HomeFrame(self.route.right_frame, width=600, height=250)

    def display_menus(self):

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(side="left", fill="x", padx=20)

        sidebar_font = ctk.CTkFont(
            family="Arial",  size=30, weight="bold")

        k = 0
        menus = []

        for i in self.route.list:
            image = ctk.CTkImage(light_image=Image.open(i['image']),
                                 dark_image=Image.open(
                i['image']),
                size=(30, 30))
            if i['menu']:
                self.route.list[k] = ctk.CTkLabel(
                    frame, image=image, text=f"  {i['name']}", font=sidebar_font, text_color="#1F389C", pady=20, compound="left")
                self.route.list[k].pack(
                    side="top", padx=10, pady=10, anchor="w")

                self.route.list[k].bind(
                    "<Button-1>", command=partial(self.change_frame, i["name"]))

                k += 1

        self.index = 0

    def change_frame(self, *args):
        for widget in self.route.right_frame.winfo_children():
            widget.destroy()
        print(args[0])
        match args[0]:
            case "Home":
                HomeFrame(self.route.right_frame, width=600, height=250)
            case "Scene":
                SceneFrame(master=self.route.right_frame,
                           width=600, height=250)
            case "Settings":
                pass
