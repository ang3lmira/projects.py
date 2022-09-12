from tkinter import *


def click():
    new_text = input.get()
    label.config(text=new_text)


# Window launch
window = Tk()
window.title("m's window")
window.minsize(width=500, height=600)

# Label creator
label = Label(text="welcome boys & girls")
label.grid(row=0, column=0)

# Button creation
button = Button(text="say hi", command=click)
button.grid(row=1, column=3)


button_2 = Button(text="say hi", command=click)
button_2.grid(row=0, column=2)

input = Entry()
input.grid(row=2, column=3)

window.mainloop()
