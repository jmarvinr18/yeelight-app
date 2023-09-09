import customtkinter as ctk


class SceneFrame(ctk.CTkFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height, fg_color="green")
        self.hide_all_frames()
        self.pack(fill="both", padx="30", pady="30", expand=True)

    def mount_components(self):
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

    def hide_all_frames(self):
        for widget in self.winfo_children():
            widget.destroy()
