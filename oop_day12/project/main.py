from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(height=200, width=600)


text_box = Entry(width=200)
text_box.insert(END, string="0")
text_box.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

equal_to = Label("is equal to")
equal_to.grid(row=1, column=0)

number = Label("0")
number.grid(row=1, column=1)

km = Label("Km")
km.grid(row=1, column=2)

calculate = Button(text="Calculate")  # command=)
calculate.grid(row=2, column=1)


window.mainloop()
