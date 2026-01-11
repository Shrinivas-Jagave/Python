from tkinter import *

root_window = Tk()
root_window.title("Label Demo")

L = Label(root_window)
L.configure(text="Label demo", fg="Black")
L.grid(row=0, column=0)

root_window.mainloop()
