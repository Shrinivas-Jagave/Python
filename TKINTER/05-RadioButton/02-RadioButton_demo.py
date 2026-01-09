from tkinter import *
from tkinter import ttk

def OnSubmit():
    Selected_Button = selected_button_var.get()
    print("Selected Button is {}:".format(Selected_Button))

def main():
    global selected_button_var

    root_window = Tk()
    root_window.title("RadioButton Demo")

    selected_button_var = StringVar()

    Radiobutton_1 = ttk.Radiobutton(
        root_window,
        text="RadioButton-1",
        value="Radiobutton_1",
        variable=selected_button_var
    )
    Radiobutton_1.grid(row=0, column=0, sticky=(W, E))

    Radiobutton_2 = ttk.Radiobutton(
        root_window,
        variable=selected_button_var,
        text="RadioButton-2",
        value="RadioButton-2"
    )
    Radiobutton_2.grid(row=1, column=0, sticky=(E, W))

    sumbit_button = ttk.Button(root_window)
    sumbit_button.configure(text="Submit", command=OnSubmit)
    sumbit_button.grid(row=2, column=0, sticky=(E, W))

    root_window.mainloop()

main()
