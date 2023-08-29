import customtkinter as ctk
from components.Route import *
import tkinter as tk
import tkinter as ttk
from tkinter.font import Font

class LeftSideBarFrame(ctk.CTkFrame):

    def __init__(self, master, width, height) -> None:
        super().__init__(master, width, height, fg_color="#E0C34C")
        self.pack(side="left", fill="both", ipadx=20)
        
        self.route = Route(self, master)

        self.display_menus()

    def display_menus(self):
        
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(side="left", fill="x", padx=20)

        sidebar_font = ctk.CTkFont(
            family="Arial",  size=30, weight="bold")

        k = 0
        menus = []
        for i in self.route.list:

            if i['menu']:
                self.route.list[k] = ctk.CTkLabel(
                    frame, image=self.route.image, text=f"  {i['name']}", font=sidebar_font, text_color="#1F389C", pady=20, compound="left")
                self.route.list[k].pack(
                    side="top", padx=10, pady=10, anchor="w")

                self.route.list[k].bind(
                    "<Button-1>", command=partial(self.change_frame, i["component"], self.route.current_page))

                menus.append(i["component"])
                k += 1

        self.index = 0

    def change_frame(self, *args):
        if self.route.current_page is not args[0]:
            self.route.switch_page(args[0])
