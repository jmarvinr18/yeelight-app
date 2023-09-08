
import customtkinter as ctk

from frames.Device import *
from components.SubRoute import *
from frames.home.devices import *


class HomeFrame(ctk.CTkFrame):
    def __init__(self, master, width, height) -> None:
        super().__init__(master, width, height, fg_color="#FFFFFF")
        self.pack(fill="both", padx="30", pady="30", expand=True)

        self.master = master

        device_list = DeviceList(self)
        device_list.mount()
