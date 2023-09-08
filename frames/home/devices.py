import customtkinter as ctk
from functools import partial
from yeelight import discover_bulbs
from model.models import Device, SceneDevice
from model.main import session
from sqlalchemy import select

import json


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
                               fg_color="#D22D4A", command=self.goToScanDevice)
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
        self.hide_device_list()

        device_details = DeviceDetails(self.master, args[0])
        device_details.mount()

    def hide_device_list(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def goToScanDevice(self):
        self.hide_device_list()

        scan_device = ScanDevice(self.master)
        scan_device.mount()


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


class ScanDevice(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.top_frame = ctk.CTkFrame(
            master, width=100, height=50, fg_color="transparent")
        self.top_frame.pack(side="top", fill="both", padx=10, pady=10)

        self.master = master

    def mount(self):

        font = ctk.CTkFont(
            family="Arial",  size=20, weight="bold")

        label = ctk.CTkLabel(self.top_frame, text="Scan Devices",
                             font=font, text_color="black", pady=3)
        label.pack(side="left", pady=20, padx=20, anchor="nw")

        button = ctk.CTkButton(self.top_frame, text="Scan",
                               fg_color="#D22D4A", command=self.scan_device)
        button.pack(side="right", pady=20, padx=20, anchor="ne")

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def scan_device(self):
        bulbs = []
        bulbs = discover_bulbs()

        font = ctk.CTkFont(
            family="Arial",  size=15, weight="bold")

        if len(bulbs) > 5:
            self.middle_frame = ctk.CTkScrollableFrame(
                self.master, width=100, height=100, fg_color="#FFFFFF")
        else:
            self.middle_frame = ctk.CTkFrame(
                self.master, width=100, height=100, fg_color="#FFFFFF")

        self.middle_frame.pack(side="top", fill="both",
                               padx=10, pady=10, expand=True)
        for bulb in bulbs:
            device_container = ctk.CTkFrame(
                self.middle_frame, height=70, fg_color="red")
            device_container.pack(side="top", fill="both",
                                  padx=10, pady=10, anchor="n")

            device_label = ctk.CTkLabel(
                device_container, text=f"{bulb['capabilities']['model']}", text_color="#FFFFFF", font=font)
            device_label.pack(side="left", pady=20, padx=20, anchor="nw")

            device_button = ctk.CTkButton(device_container, text="Add",
                                          fg_color="#FFFFFF", command=partial(
                                              self.add_device, bulb))
            device_button.pack(side="right", pady=20, padx=20, anchor="ne")

    def add_device(self, *bulb):

        statement = select(Device).where(Device.ip == bulb[0]['ip'])

        result = session.scalars(statement).all()

        if len(result) == 0:
            device = Device(bulb[0]['ip'], bulb[0]['port'],
                            json.dumps(bulb[0]['capabilities']))
            session.add(device)
            session.commit()

        else:
            print('IP already added.')

    def toggle_list_and_details(self, *args):

        self.hide_device_list()
        device_details = DeviceList(self.master)
        device_details.mount()

    def hide_device_list(self):
        for widget in self.master.winfo_children():
            widget.destroy()
