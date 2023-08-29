import customtkinter as ctk


class Device(ctk.CTkFrame):
    def __init__(self, master, width=600, height=250):
        super().__init__(master, width, height, fg_color="red")

        self.top_frame = ctk.CTkFrame(
            self, width=100, height=50, fg_color="green")
        self.top_frame.pack(side="top", fill="both",
                            expand=True, padx=10, pady=10, anchor="n")

        self.middle_frame = ctk.CTkFrame(
            self, width=100, height=50, fg_color="green")
        self.middle_frame.pack(side="top", fill="both",
                               expand=True, padx=10, pady=10, anchor="n")

        self.middle2_frame = ctk.CTkFrame(
            self, width=100, height=50, fg_color="green")
        self.middle2_frame.pack(side="top", fill="both",
                                expand=True, padx=10, pady=10, anchor="n")

        self.bottom_frame = ctk.CTkFrame(
            self, width=100, height=100, fg_color="green")
        self.bottom_frame.pack(side="top", fill="both",
                               expand=True, padx=10, pady=10, anchor="n")
