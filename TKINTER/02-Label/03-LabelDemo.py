from tkinter import *

root_window = Tk()
root_window.title("Label Demo")

label_1 = Label(root_window)
label_1.configure(text="Label Demo", fg="Black")
label_1.grid(row=0, column=0)

root_window.mainloop()
