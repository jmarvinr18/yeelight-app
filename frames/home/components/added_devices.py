from frames.home.devices import ScanDevice
import customtkinter as ctk
from functools import partial


class AddedDevices(ScanDevice):

    def __init__(self, master) -> None:
        self.master = master

    def add(self, capabilities, bulb, index):
        font = ctk.CTkFont(
            family="Arial",  size=15, weight="bold")

        device_container = ctk.CTkFrame(
            self.master, height=70, fg_color="#8D4BF6")
        device_container.pack(side="top", fill="both",
                              padx=5, pady=5, anchor="n")
        device_label = ctk.CTkLabel(
            device_container, text=f"{capabilities['model']}", text_color="#FFFFFF", font=font)

        device_label.pack(side="left", pady=20, padx=20, anchor="nw")

        device_button = ctk.CTkButton(device_container, text="Remove", text_color="black",
                                      fg_color="#FFFFFF", command=partial(
                                          self.remove_device, bulb, index, device_container),  hover=False)

        device_button.pack(side="right", pady=20, padx=20, anchor="ne")
        self.remove_device

    def remove(self):
        pass
