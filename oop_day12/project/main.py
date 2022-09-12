from tkinter import *

window = Tk()
window.title("Mile to Km converter")
#window.config(padx=20, pady=20)
#window.minsize(height=100, width=200)


def click():
    number_miles = int(text_box.get())
    number_km = round((number_miles * 1.609), 2)
    number.config(text=f"{number_km}")


text_box = Entry(width=10)
text_box.insert(END, string="0")
text_box.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)

number = Label(text="0")
number.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

calculate = Button(text="Calculate", command=click)
calculate.grid(row=2, column=1)


window.mainloop()
