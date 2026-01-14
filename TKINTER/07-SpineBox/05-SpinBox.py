from tkinter import *
from tkinter import ttk

def SpinBoxValue():
    value = spinbox_var.get()
    if not value:
        value = None
    print(f"SpinBox Value : {value}")

def main():
    global spinbox_var

    root_window = Tk()
    root_window.title("SpinBox Demo")

    spinbox_var = StringVar()

    label = ttk.Label(root_window)
    label.configure(text="SpinBox", foreground="black")
    label.grid(row=0, column=0)

    spinbox = ttk.Spinbox(root_window)
    spinbox.configure(textvariable=spinbox_var, from_=0, to=10)
    spinbox.grid(row=0, column=1, sticky=(E, W))

    button = ttk.Button(root_window)
    button.configure(text="Get_Value", command=SpinBoxValue)
    button.grid(row=1, column=0, sticky=(E, W))

    root_window.mainloop()

main()