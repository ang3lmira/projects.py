from tkinter import *

window = Tk()
window.title("m's window")
window.minsize(width=500, height=600)


def click():
    label.config(text="The button has been clicked!")


label = Label(text="welcome boys & girls")
label.pack(side="right")


button = Button(text="say hi", command=click)
button.pack()

window.mainloop()
