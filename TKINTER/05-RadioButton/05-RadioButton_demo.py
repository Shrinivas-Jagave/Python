from tkinter import *
from tkinter import ttk

def OnSubmit():
    Selected_Button = selected_button_var.get()
    print("Selected Button is : {}".format(Selected_Button))

def main():
    global selected_button_var

    root_window = Tk()
    root_window.title("RadioButton Demo")

    selected_button_var = StringVar()

    Radiobutton_1 = ttk.Radiobutton(root_window)
    Radiobutton_1.configure(
        text="RadioButton-1",
        value="RadioButton-1",
        variable=selected_button_var
    )
    Radiobutton_1.grid(row=0, column=0, sticky=(E, W))

    Radiobutton_2 = ttk.Radiobutton(root_window)
    Radiobutton_2.configure(
        text="RadioButton-2",
        value="RadioButton-2",
        variable=selected_button_var
    )
    Radiobutton_2.grid(row=1, column=0, sticky=(E, W))

    submit_button = ttk.Button(root_window)
    submit_button.configure(text="Submit", command=OnSubmit)
    submit_button.grid(row=2, column=0, sticky=(E, W))

    root_window.mainloop()

main()
