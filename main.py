from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        ## Here put the direction of where you want to keep the .json, you dont need to create it it will create itself
        ##given a place to do it so
        with open("../../../passwords.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found. Please create one by saving a password.")

    if website in data:
        messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: "
                                                   f"{data[website]['password']}")
    else:
        messagebox.showwarning("Website not found. Please try again")


def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Fill the blanks")
    else:
        try:
            # # Here put the direction of where you want to keep the .json, you dont need to create it it will create
            # itself given a place to do it so
            with open("../../../passwords.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            ## Here put the direction of where you want to keep the .json, you dont need to create it it will create
            ## itself given a place to do it so
            with open("../../../passwords.json", mode="w") as data_file:
                json.dump(new_data, data_file)
        else:
            ## Here put the direction of where you want to keep the .json, you dont need to create it it will create
            ## itself given a place to do it so
            with open("../../../passwords.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.resizable(False, False)
# window.minsize(width=200, height=200)
canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_entry = Entry(width=21)
website_entry.focus()
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1)

# Email
email_label = Label(text="Email/Username:")
email_entry = Entry(width=36)
email_entry.insert(0, "selorenzano1@gmail.com")
email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_entry = Entry(width=21)
password_button = Button(width=11, text="Generate Password", command=generate_password)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
password_button.grid(column=2, row=3)

# Add
add_button = Button(width=34, text="Add", command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

# Search
search_button = Button(width=11, text="Search", command=search_password)
search_button.grid(column=2, row=1)
window.mainloop()
