import customtkinter as ctk
from functools import partial
from yeelight import discover_bulbs
from bulbs import *
from model.models import Device
from tkinter import colorchooser
from model.main import session
from sqlalchemy import select, delete
from PIL import Image
import os
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

        statement = select(Device)
        bulbs = session.scalars(statement).all()

        container = ctk.CTkFrame(
            self.middle_frame, width=250, height=250, fg_color="#FFFFFF")
        container.grid(column=0, row=0, sticky='news', padx=10, pady=10)

        col = 0
        row = 0

        file_path = os.path.dirname(os.path.realpath(__file__))

        image = ctk.CTkImage(light_image=Image.open(file_path + '/bulb.png'),
                             dark_image=Image.open(
            file_path + '/bulb.png'),
            size=(50, 50))
        for bulb in bulbs:
            bg = '#8D4BF6'
            bulb_name = json.loads(bulb.__dict__["capabilities"])["model"]

            pic = ctk.CTkButton(container, text=bulb_name, image=image, compound="top", fg_color=bg, font=(
                'Arial', 20), text_color="#FFFFFF", width=50, command=partial(
                self.toggle_list_and_details, bulb.__dict__))
            pic.grid(column=col, row=row, sticky='news',
                     padx=10, pady=10, ipadx=20, ipady=20)

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
    def __init__(self, master, device) -> None:
        super().__init__(master)
        self.top_frame = ctk.CTkFrame(
            master, width=100, height=50, fg_color="transparent")
        self.top_frame.pack(side="top", fill="both", padx=10, pady=10)

        self.middle_frame = ctk.CTkFrame(
            master, width=100, height=50, fg_color="transparent")
        self.middle_frame.pack(side="top", fill="both", expand=True,
                               padx=10, pady=10, anchor="n")

        self.master = master
        self.device_details = device
        self.name = json.loads(device['capabilities'])['model']
        self.switch_var = ctk.StringVar(value="on")

        self.selected_color = "#FFFFFF"

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")

        bulb = YeelightBulbs(self.device_details['ip'])

        bulb.set_rgb(color_code[0])

        self.selected_color = color_code

    def switch_event(self):

        bulb = YeelightBulbs(self.device_details['ip'])

        if self.switch_var.get() == 'on':
            bulb.turnOn()
        else:
            bulb.turnOff()

    def adjust_brightness(self, value):
        bulb = YeelightBulbs(self.device_details['ip'])
        bulb.set_brightness(value)

    def mount(self):

        font = ctk.CTkFont(
            family="Arial",  size=20, weight="bold")

        label1 = ctk.CTkLabel(self.top_frame, text=self.name.upper(),
                              font=font, text_color="black", pady=3)
        label1.pack(side="left", pady=20, padx=20, anchor="nw")

        button = ctk.CTkButton(self.top_frame, text="Save Details",
                               fg_color="#D22D4A", command=self.toggle_list_and_details)
        button.pack(side="right", pady=20, padx=20, anchor="ne")

        config_font = ctk.CTkFont(
            family="Arial",  size=15, weight="bold")

        switch_label = ctk.CTkLabel(self.middle_frame, text="Power",
                                    font=config_font, text_color="black", pady=3)
        switch_label.grid(row=1, column=1, pady=20, padx=20, sticky="w")

        switch = ctk.CTkSwitch(self.middle_frame, text="Power", command=self.switch_event,
                               variable=self.switch_var, onvalue="on", offvalue="off")
        switch.grid(row=1, column=2, pady=20, padx=20, sticky="w")

        color_chooser_label = ctk.CTkLabel(self.middle_frame, text="Color",
                                           font=config_font, text_color="black", pady=3)
        color_chooser_label.grid(
            row=2, column=1, pady=20, padx=20, sticky="w")

        color_chooser = ctk.CTkButton(self.middle_frame, text="Choose Color",
                                      fg_color=self.selected_color, border_color="#D2D4DA", command=self.choose_color)

        color_chooser.grid(
            row=2, column=2, pady=20, padx=20, sticky="w")

        brightness_label = ctk.CTkLabel(self.middle_frame, text="Brightness",
                                        font=config_font, text_color="black", pady=3)
        brightness_label.grid(
            row=3, column=1, pady=20, padx=20, sticky="w")

        brightness = ctk.CTkSlider(
            self.middle_frame, from_=0, to=100, command=self.adjust_brightness)
        brightness.grid(
            row=3, column=2, pady=20, padx=20, sticky="w")

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

        self.middle_frame = ctk.CTkScrollableFrame(
            self.master, width=100, height=500, fg_color="transparent")
        self.middle_frame.pack(side="top", fill="both", expand=True,
                               padx=20, pady=20)

        self.saved_devices = self.render_saved_devices()

    def mount(self):

        font = ctk.CTkFont(
            family="Arial",  size=20, weight="bold")

        label = ctk.CTkLabel(self.top_frame, text="Scan Devices",
                             font=font, text_color="black", pady=3)
        label.pack(side="left", pady=20, padx=20, anchor="nw")
        file_path = os.path.dirname(os.path.realpath(__file__))

        if len(self.saved_devices) > 0:
            image = ctk.CTkImage(light_image=Image.open(file_path + "/search-icon.png"),
                                 dark_image=Image.open(
                file_path + "/search-icon.png"), size=(20, 20))
            button = ctk.CTkButton(self.top_frame, image=image, compound="left", text="Scan", text_color="black", border_width=1, border_color="#D2D4DA",
                                   fg_color="transparent", command=self.scan_device, hover=False)
            button.pack(side="right", ipady=10, pady=20, padx=20, anchor="ne")

            self.master.columnconfigure(0, weight=1)
            self.master.rowconfigure(0, weight=1)

        else:
            image = ctk.CTkImage(light_image=Image.open(file_path + "/search-icon.png"),
                                 dark_image=Image.open(
                file_path + "/search-icon.png"), size=(50, 50))
            button = ctk.CTkButton(self.middle_frame, font=font, text_color="black", border_width=1, border_color="#702632", image=image, compound="top", text="Scan",
                                   fg_color="transparent", command=self.scan_device, hover=False)
            button.pack(side="top", expand=True,
                        ipadx=20, ipady=20, anchor="center")

    def render_saved_devices(self):
        statement = select(Device)
        bulbs = session.scalars(statement).all()
        index = 0

        devices = list()
        for bulb in bulbs:
            self.make_device_frame(bulb.__dict__, True, index)
            index += 1
            devices.append(bulb.__dict__['ip'])

        return devices

    def scan_device(self):
        bulbs = discover_bulbs()
        file_path = os.path.dirname(os.path.realpath(__file__))

        for bulb in bulbs:
            statement = select(Device).where(Device.ip == bulb['ip'])

            result = session.scalars(statement).all()

            if len(result) == 0:
                self.make_device_frame(bulb)

            if len(self.middle_frame.winfo_children()) == 0:
                for widget in self.middle_frame.winfo_children():
                    widget.destroy()
                image = ctk.CTkImage(light_image=Image.open(file_path + "/search-icon.png"),
                                     dark_image=Image.open(
                    file_path + "/search-icon.png"), size=(20, 20))
                button = ctk.CTkButton(self.top_frame, image=image, compound="left", text="Scan", text_color="black", border_width=1, border_color="#D2D4DA",
                                       fg_color="transparent", command=self.scan_device, hover=False)
                button.pack(side="right", ipady=10,
                            pady=20, padx=20, anchor="ne")

    def make_device_frame(self, bulb, is_added=False, index=0):
        font = ctk.CTkFont(
            family="Arial",  size=15, weight="bold")
        device_container = ctk.CTkFrame(
            self.middle_frame, height=70, fg_color="#8D4BF6")
        device_container.pack(side="top", fill="both",
                              padx=10, pady=10, anchor="n")

        if type(bulb['capabilities']) == str:
            capabilities = json.loads(bulb['capabilities'])
        else:
            capabilities = bulb['capabilities']

        if is_added:
            device_label = ctk.CTkLabel(
                device_container, text=f"{capabilities['model']}", text_color="#FFFFFF", font=font)

            device_label.pack(side="left", pady=20, padx=20, anchor="nw")

            device_button = ctk.CTkButton(device_container, text="Remove", text_color="black",
                                          fg_color="#FFFFFF", command=partial(
                                              self.remove_device, bulb, index, device_container), hover=False)
        else:
            device_label = ctk.CTkLabel(
                device_container, text=f"{capabilities['model']}", text_color="#FFFFFF", font=font)

            device_label.pack(side="left", pady=20, padx=20, anchor="nw")

            device_button = ctk.CTkButton(device_container, text="Add", text_color="black",
                                          fg_color="#FFFFFF", command=partial(
                                              self.add_device, bulb), hover=False)
        device_button.pack(side="right", pady=20, padx=20, anchor="ne")

    def add_device(self, *bulb):

        statement = select(Device).where(Device.ip == bulb[0]['ip'])

        result = session.scalars(statement).all()

        if len(result) == 0:
            self.saved_devices.append(bulb[0]['ip'])
            device = Device(bulb[0]['ip'], bulb[0]['port'],
                            json.dumps(bulb[0]['capabilities']))
            session.add(device)
            session.commit()

        else:
            print('IP already added.')

    def remove_device(self, *bulb):
        index = self.saved_devices.index(bulb[0]['ip'])
        device = session.query(Device).where(
            Device.ip == bulb[0]['ip']).first()
        session.delete(device)
        session.commit()
        self.middle_frame.winfo_children()[index].destroy()

        self.saved_devices.remove(bulb[0]['ip'])

    def toggle_list_and_details(self, *args):

        self.hide_device_list()
        device_details = DeviceList(self.master)
        device_details.mount()

    def hide_device_list(self):
        for widget in self.master.winfo_children():
            widget.destroy()
