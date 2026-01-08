from tkinter import *

root_window = Tk()
root_window.title("Label Demo")

L1 = Label(root_window)
L1.configure(text="Label demo", fg="black")
L1.grid(row=0, column=0)

L2 = Label(root_window)
L2.configure(text="Shrinivas U. Jagave", fg="black", bg="yellow")
L2.grid(row=1, column=0)

root_window.mainloop()
