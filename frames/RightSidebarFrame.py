import customtkinter as ctk


class RightSideBarFrame(ctk.CTkFrame):

    def __init__(self, master, width, height) -> None:
        super().__init__(master, width, height, fg_color="transparent")
        self.pack(side="right", fill="both", padx=10, pady=10, expand=True)
