from tkinter import *
from tkinter import ttk
import sys

root_window = Tk()
root_window.title('Listbox Demo')
root_window.geometry('400x400')
root_window.grid_rowconfigure(0, weight=1)
root_window.grid_columnconfigure(0, weight=1)

def on_contact_select(*args):
    selection = listbox.curselection()[0]
    print(indian_states[selection])

    
listbox = Listbox(root_window)
listbox.configure(foreground='white', background='#505050', font=('arial', 12))
listbox.grid(row=0, column=0, padx=5, pady=5, sticky=(E, W, N, S))

listbox.bind('<<ListboxSelect>>', on_contact_select)

indian_states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

for state in indian_states:
    listbox.insert(END, state)

root_window.mainloop()