
"""Python program to generate random password using Tkinter module"""
import random
from tkinter import Radiobutton, Label, Entry, Tk, IntVar, END
from tkinter.ttk import Button, Combobox
import pyperclip

def low():
    """calculates password"""
    entry.delete(0, END)

    #get password lenght
    length = var1.get()

    number = "0123456789"
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols = letter + 5*number + 7*"!@#$?=&"
    password = ""

    #low strenght
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(number)
        return password

    #medium strenght
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(letter)
        return password

    #strong strenght
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(symbols)
        return password
    else:
        print("Please choose an option")


def generate():
    """generates password"""
    password1 = low()
    entry.insert(10, password1)
    return password1


#tkinter block
#GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

"""window title"""
root.title("passwdgen")

#create label and entry to show password
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

def copypasswd():
    """copies password to clipboard"""
    random_password = entry.get()
    pyperclip.copy(random_password)

copy_button = Button(root, text="Copy", command=copypasswd)
copy_button.grid(row=0, column=2)

#create label for password length
c_label = Label(root, text="Length")
c_label.grid(row=1)

#create generate button
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=1, column=2)

#strength selector
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=2, column=0, sticky='N')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=2, column=1, sticky='N')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=2, column=2, sticky='N')
combo = Combobox(root, textvariable=var1)

#Combo Box for password length
combo['values'] = (8, 10, 12, 14, 16, 18, 20, 22, 24)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

#start GUI
root.mainloop()
