from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_info = website_box.get()
    email_info = email_box.get()
    password_info = password_box.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website_info} | {email_info} | {password_info} ")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0, )

website_box = Entry(width=35,)
website_box.grid(row=1, column=1, columnspan=2)
website_box.focus()

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_box = Entry(width=35)
email_box.grid(row=2, column=1, columnspan=2)
email_box.insert(0, "a0codes@yahoo.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_box = Entry(width=21)
password_box.grid(row=3, column=1)


password_generator = Button(text="Generate Password")
password_generator.grid(row=3, column=2)

add_password = Button(text="Add", width=36, command=save)
add_password.grid(row=4, column=1)
window.mainloop()
