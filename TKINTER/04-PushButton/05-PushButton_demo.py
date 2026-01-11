from tkinter import *
from tkinter import ttk
import sys

def terminate():
    print("Exiting the app.....")
    sys.exit(0)

root_window = Tk()
root_window.title("Button Demo")

b = ttk.Button(root_window)
b.configure(text="Button", command=terminate)
b.grid(row=0, column=0, sticky=(E, W))

root_window.mainloop()
