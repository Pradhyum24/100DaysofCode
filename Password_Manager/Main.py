from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [(random.choice(letters)) for _ in range(5, 10)]
    password_numbers = [(random.choice(numbers)) for _ in range(2, 4)]
    password_symbols = [(random.choice(symbols)) for char in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers
    password = "".join(password_list)

    input_password.insert([0], password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = input_website.get()
    email = input_username.get()
    password = input_password.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops",message="You have not entered either the password and email")
    else:

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        input_website.delete(0,END)
        input_password.delete(0,END)

# ---------------------------- SEARCH PASSWORD------------------------------- #
def search_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Error",message="You did not save any data as of now.")
    else:
        try:
            website = input_website.get()
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title="Error",message=f"Sorry the {website} details are not saved in the app. \n Please save the details and try again. ")
        else:
            messagebox.showinfo(title=website,message=f"Email :{email} \n Password :{password}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

label_website = Label(text="Website: ")
label_website.grid(row=1,column=0)

input_website = Entry(width=18)
input_website.focus()
input_website.grid(row=1,column=1)

label_username = Label(text="Email/Username: ")
label_username.grid(row=2,column=0)

input_username = Entry(width=35)
input_username.grid(row=2,column=1,columnspan=2)
input_username.insert([0],"yourmail@gmail.com")

label_password = Label(text="Password:")
label_password.grid(row=3,column=0)

input_password = Entry(width=18)
input_password.grid(row=3,column=1)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=12,command=search_password)
search_button.grid(row=1,column=2)
window.mainloop()
