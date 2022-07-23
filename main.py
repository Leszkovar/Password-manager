from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

FONT_NAME = ("Arial", 20)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_func():
    pass

def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 12))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    pw_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():

    web = web_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": pw,
        }
    }

    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        try:
            with open("my_passwords.json", "r") as file:
                # reading the old data
                data = json.load(file)
                # update the old data with new data
                data.update(new_data)
            with open("my_passwords.json", "w") as file:
                # write the data
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            with open("my_passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pw_entry.delete(0, END)


def search():
    web = web_entry.get()
    try:
        with open("my_passwords.json", "r") as data_file:
            data = json.load(data_file)
            if web in data:
                email_search = data[web]["email"]
                pw_search = data[web]["password"]
                messagebox.showinfo(title=web, message=f"Email: {email_search}\nPassword: {pw_search}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {web} exists." )
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")




# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20, bg="white")

windows.grid_columnconfigure(0, minsize=25)
windows.grid_columnconfigure(1, minsize=50)
windows.grid_columnconfigure(2, minsize=25)
windows.grid_rowconfigure(0, minsize=100)
windows.grid_rowconfigure(1, minsize=25)
windows.grid_rowconfigure(2, minsize=25)
windows.grid_rowconfigure(3, minsize=25)
windows.grid_rowconfigure(4, minsize=25)


canvas = Canvas(width=250, height=250, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(125, 125, image=img)
canvas.grid(column=0, row=0, columnspan=3)

webs = Label(text="Website:", font=FONT_NAME)
webs.grid(column=0, row=1, sticky=E)

email = Label(text="Email/Username:", font=FONT_NAME)
email.grid(column=0, row=2)

pw = Label(text="Password:", font=FONT_NAME)
pw.grid(column=0, row=3, sticky=E)

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky=W)
web_entry.focus()

email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(0, "leszkovar@gmail.com")  # 0, or END

pw_entry = Entry(width=35)
pw_entry.grid(column=1, row=3, sticky=W)

generate_button = Button(text="Generate", width=14, command=generate, font=("Arial", 12))
generate_button.grid(column=2, row=3, sticky=E)

add_button = Button(text="Add", width=40, command=add_to_file, font=("Arial", 12))
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

search_button = Button(text="Search", width=14, command=search, font=("Arial", 12))
search_button.grid(column=2, row=1, columnspan=2, sticky=E)


windows.mainloop()
