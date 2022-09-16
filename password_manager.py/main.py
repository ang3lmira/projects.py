from re import search
import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_box.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_info = website_box.get()
    email_info = email_box.get()
    password_info = password_box.get()
    new_data = {
        website_info:
        {"email": email_info,
         "password": password_info
         }
    }

    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Something isn't right :$",
                            message="Please fill in the boxes with info.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(new_data, data_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_box.delete(0, END)
            password_box.delete(0, END)
#-----------------------------FIND PASSWORD-------------------------------------#


def find_password():
    website = website_box.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_box = Entry(width=35)
website_box.grid(row=1, column=1)
website_box.focus()

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_box = Entry(width=35)
email_box.grid(row=2, column=1)
email_box.insert(0, "a0codes@yahoo.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_box = Entry(width=35)
password_box.grid(row=3, column=1)


password_generator = Button(
    text="Generate Password", width=23, command=generate_password)
password_generator.grid(row=3, column=2)

add_password = Button(text="Add", width=53, command=save)
add_password.grid(row=4, column=1, columnspan=2)


click_search = Button(text="Search", width=23, command=search)
click_search.grid(row=1, column=2)
window.mainloop()
