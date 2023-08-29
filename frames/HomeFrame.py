
import customtkinter as ctk
import tkinter as tk
from functools import partial
from frames.Device import *
from components.SubRoute import *

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, width, height) -> None:
        super().__init__(master, width, height, fg_color="#FFFFFF")
        self.pack(fill="both", padx="30", pady="30", expand=True)

        self.master = master

        device_list = DeviceList(self)
        device_list.mount()

    
class DeviceList(ctk.CTkFrame):

    def __init__(self, master) -> None:
        super().__init__(master)
        

        self.top_frame = ctk.CTkFrame(
            master, width=100, height=50, fg_color="#FFFFFF")
        self.top_frame.pack(side="top", fill="both", padx=10, pady=10)

        self.middle_frame = ctk.CTkFrame(
            master, width=100, height=50, fg_color="#FFFFFF")
        self.middle_frame.pack(side="top", fill="both",
                               padx=10, pady=10, anchor="n")

        self.master = master
        
    def mount(self):


        font = ctk.CTkFont(
            family="Arial",  size=20, weight="bold")

        label1 = ctk.CTkLabel(self.top_frame, text="All Devices",
                              font=font, text_color="black", pady=3)
        label1.pack(side="left", pady=20, padx=20, anchor="nw")

        button = ctk.CTkButton(self.top_frame, text="Add Device",
                               fg_color="#D22D4A", command=lambda: print("test"))
        button.pack(side="right", pady=20, padx=20, anchor="ne")

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        numbers = [num for num in range(20)]

        container = ctk.CTkFrame(
            self.middle_frame, width=250, height=250, fg_color="#FFFFFF")
        container.grid(column=0, row=0, sticky='news', padx=10, pady=10)
        for i in range(5):
            container.grid_columnconfigure(i, weight=3, uniform='pics')

        col = 0
        row = 0

        for number in numbers:
            bg = '#8D4BF6'

            pic = ctk.CTkLabel(container, text=f'Pic {number+1}', fg_color=bg, font=(
                'Arial', 20), text_color="#FFFFFF", pady=3)
            pic.grid(column=col, row=row, sticky='news',
                     padx=10, pady=10, ipadx=15, ipady=15)

            pic.bind("<Button>", command=partial(
                self.toggle_list_and_details, number + 1))
            if col == 5:
                col = 0
                row += 1
            else:
                col += 1
            container.grid_rowconfigure(row, weight=5, uniform='rows')

    def toggle_list_and_details(self, *args):
        print(args)
        self.hide_device_list()

        device_details = DeviceDetails(self.master, args[0])
        device_details.mount()


    def hide_device_list(self):
        for widget in self.master.winfo_children():
            widget.destroy()


class DeviceDetails(ctk.CTkFrame):
    def __init__(self, master, name) -> None:
        super().__init__(master)
        self.top_frame = ctk.CTkFrame(
            master, width=100, height=50, fg_color="blue")
        self.top_frame.pack(side="top", fill="both", padx=10, pady=10)

        self.middle_frame = ctk.CTkFrame(
            master, width=100, height=50, fg_color="#FFFFFF")
        self.middle_frame.pack(side="top", fill="both",
                               padx=10, pady=10, anchor="n")
        
        self.master = master
        self.name = name

    def mount(self):

        font = ctk.CTkFont(
            family="Arial",  size=20, weight="bold")

        label1 = ctk.CTkLabel(self.top_frame, text=f"Bulb {self.name}",
                              font=font, text_color="white", pady=3)
        label1.pack(side="left", pady=20, padx=20, anchor="nw")

        button = ctk.CTkButton(self.top_frame, text="Save Details",
                               fg_color="#D22D4A", command=self.toggle_list_and_details)
        button.pack(side="right", pady=20, padx=20, anchor="ne")

        self.middle_frame = ctk.CTkFrame(
            self, width=100, height=50, fg_color="#FFFFFF")
        self.middle_frame.pack(side="top", fill="both",
                               padx=10, pady=10, anchor="n")

    def toggle_list_and_details(self, *args):

        self.hide_device_list()
        device_details = DeviceList(self.master)
        device_details.mount()

    def hide_device_list(self):
        for widget in self.master.winfo_children():
            widget.destroy()
