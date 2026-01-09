from tkinter import *
from tkinter import ttk

root_window = Tk()
root_window.title("Input Demo")

label_1 = Label(root_window)
label_1.configure(text="Enter Name : ")
label_1.grid(row=0, column=0)

entry_1 = ttk.Entry(root_window)
entry_1.grid(row=0, column=1, sticky=(E, W))

root_window.mainloop()
