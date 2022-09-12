from tkinter import *

window = Tk()
window.title("m's window")
window.minsize(width=500, height=600)


def click():
    new_text = input.get()
    label.config(text=new_text)


label = Label(text="welcome boys & girls")
label.pack()


button = Button(text="say hi", command=click)
button.pack()

input = Entry()
input.pack()

window.mainloop()
