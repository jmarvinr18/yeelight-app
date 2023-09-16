from devices import *


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

        self.middle_frame.name = "middle_frame"

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

        return color_code

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

        config_font = ctk.CTkFont(
            family="Arial",  size=15, weight="bold")

    # IP Address ======================================================================

        ip_label = ctk.CTkLabel(self.middle_frame, text="IP Address:",
                                font=config_font, text_color="black", pady=3)
        ip_label.grid(row=1, column=1, pady=20, padx=20, sticky="w")

        ip = ctk.CTkLabel(
            self.middle_frame, text=self.device_details['ip'], text_color="black", pady=3)
        ip.grid(row=1, column=2, pady=20, padx=20, sticky="w")

    # Model ======================================================================

        model_label = ctk.CTkLabel(self.middle_frame, text="Model:",
                                   font=config_font, text_color="black", pady=3)
        model_label.grid(row=1, column=3, pady=20, padx=20, sticky="w")

        model = ctk.CTkLabel(
            self.middle_frame, text=self.name, text_color="black", pady=3)
        model.grid(row=1, column=4, pady=20, padx=20, sticky="w")

    # Name ======================================================================

        name_label = ctk.CTkLabel(self.middle_frame, text="Name:",
                                  font=config_font, text_color="black", pady=3)
        name_label.grid(row=2, column=1, pady=20, padx=20, sticky="w")

        name = ctk.CTkEntry(
            self.middle_frame, placeholder_text="Enter device name")
        name.grid(row=2, column=2, pady=20, padx=20, sticky="w")

    # Power Mode ======================================================================

        switch_label = ctk.CTkLabel(self.middle_frame, text="Power:",
                                    font=config_font, text_color="black", pady=3)
        switch_label.grid(row=2, column=3, pady=20, padx=20, sticky="w")

        switch = ctk.CTkSwitch(self.middle_frame, text="Power", command=self.switch_event,
                               variable=self.switch_var, onvalue="on", offvalue="off")
        switch.grid(row=2, column=4, pady=20, padx=20, sticky="w")

    # Color ======================================================================

        color_chooser_label = ctk.CTkLabel(self.middle_frame, text="Color:",
                                           font=config_font, text_color="black", pady=3)
        color_chooser_label.grid(
            row=4, column=1, pady=20, padx=20, sticky="w")

        color_chooser = ctk.CTkButton(self.middle_frame, text="Choose Color",
                                      fg_color=self.selected_color, border_color="#D2D4DA", command=self.choose_color)

        color_chooser.grid(
            row=4, column=2, pady=20, padx=20, sticky="w")

    # Brightness ======================================================================

        brightness_label = ctk.CTkLabel(self.middle_frame, text="Brightness:",
                                        font=config_font, text_color="black", pady=3)
        brightness_label.grid(
            row=5, column=1, pady=20, padx=20, sticky="w")

        brightness = ctk.CTkSlider(
            self.middle_frame, from_=0, to=100, command=self.adjust_brightness)
        brightness.grid(
            row=5, column=2, pady=20, padx=20, sticky="w")

    # Submit =========================================================================

        label1 = ctk.CTkLabel(self.top_frame, text=self.name.upper(),
                              font=font, text_color="black", pady=3)
        label1.pack(side="left", pady=20, padx=20, anchor="nw")

        button = ctk.CTkButton(self.top_frame, text="Save Details",
                               fg_color="#D22D4A", command=partial(self.submit_entry, name, switch, color_chooser, brightness))
        button.pack(side="right", pady=20, padx=20, anchor="ne")

    def submit_entry(self, *entries):
        # name = entries[0].get()
        # power = entries[1].get()
        # color = self.selected_color
        # brightness = entries[3].get()
        # print(f"NAME: {name}")
        # print(f"COLOR: {color}")
        # print(f"POWER: {power}")
        # print(f"BRIGHTNESS: {brightness}")

        print(self.master.nametowidget())

        # self.toggle_list_and_details()

    def toggle_list_and_details(self, *args):

        self.hide_device_list()
        device_details = DeviceList(self.master)
        device_details.mount()

    def hide_device_list(self):
        for widget in self.master.winfo_children():
            widget.destroy()
