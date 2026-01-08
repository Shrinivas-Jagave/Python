from tkinter import *

root_window = Tk()
root_window.title("Input Demo")

label_1 = Label(root_window)
label_1.configure(text="Enter Name : ")
label_1.grid(row=0, column=0)

entry1 = Entry(root_window)
entry1.grid(row=0, column=1)

label_2 = Label(root_window)
label_2.configure(text="Enter Email : ")
label_2.grid(row=1, column=0)

entry2 = Entry(root_window)
entry2.grid(row=1, column=1)

root_window.mainloop()
