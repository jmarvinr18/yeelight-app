import customtkinter
from yeelight import discover_bulbs

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

bulb = discover_bulbs()


root = customtkinter.CTk()
root.title('LWA Yeelight Control Panel')
root.geometry("500x350")

def login():
   print(bulb)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

def switch_event():
    print("switch toggled, current value:", switch_var.get())

# switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(master=frame, text="CTkSwitch", command=switch_event)

switch.pack(pady=12, padx=10)

root.mainloop()