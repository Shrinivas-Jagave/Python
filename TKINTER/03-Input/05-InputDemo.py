from tkinter import *
from tkinter import ttk

root_window = Tk()
root_window.title("Input Demo")

Label_1 = Label(root_window)
Label_1.configure(text="Enter Name : ")
Label_1.grid(row=0, column=0)

Entry_1 = ttk.Entry(root_window)
Entry_1.grid(row=0, column=1, sticky=(E, W))

root_window.mainloop()
