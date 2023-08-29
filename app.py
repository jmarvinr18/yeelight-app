from yeelight import discover_bulbs
import tkinter

bulb = discover_bulbs()
print(bulb)

root = tkinter.Tk()

label = tkinter.Label(root)
root.mainloop()
