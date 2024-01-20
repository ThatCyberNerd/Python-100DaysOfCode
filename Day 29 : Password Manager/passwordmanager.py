from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for value in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for value in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char

    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(email_username) == 0 or len(website) == 0:
        messagebox.showinfo(title="Warning!", message="The entry fields cannot be blank!")

    else:
        is_ok = messagebox.askokcancel(
            message=f"These are the credentials entered : \n Wesbite : {website} \n Email/Username : {email_username} \n Password : {password} \n Is it okay to save?")

        if is_ok:
            with open("passwords.txt", mode="a") as passwords_file:
                passwords_file.write(f"{website} | {email_username} | {password} \n")
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title="Confirmation", message="Password Successfully Added!")

        else:
            pass

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_entry = Entry()
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=35, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
