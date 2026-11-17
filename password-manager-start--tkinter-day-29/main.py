# We are building MyPass, A Password Manager
# Not an internetbased service, but we will be storing this newly generated password for us inside a txt file which will be completely offline, off the grid
# As soon as we click on GeneratePassword, it not only generates a strong password, it also copies it to your clipboard
from tkinter import * # only imports all the classes and constants, but would not import things like the message box which is simply just anothe rmodule of code
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# # From Password Generator Project
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# # nr_letters = randint(8, 10)
# # nr_symbols = randint(2, 4)
# # nr_numbers = randint(2, 4)

# # password_list = []

# # [new_item for item in list]... The keyword format for lists

# # print([choice(letters) for _ in range(nr_letters)])
# password_letters = [choice(letters) for _ in range(randint(8, 10))]

# password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

# password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

# # for char in range(nr_letters):
# #   password_list.append(random.choice(letters))

# # for char in range(nr_symbols):
# #   password_list += random.choice(symbols)

# # for char in range(nr_numbers):
# #   password_list += random.choice(numbers)

# password_list = password_letters + password_symbols + password_numbers

# shuffle(password_list)

# password = "".join(password_list)

# # password = ""
# # for char in password_list:
# #   password += char

# print(f"Your password is: {password}")

def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_input.get()
    email = email_input.get()   
    password = password_input.get()
    new_data = {
        website: {
          "email": email,
          "password": password,  
    }
        }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                    #    reading old data
                        data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data) 
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)
            
        finally:              
            # json.load() takes the json file and converts it into a python dictionary: $ python main.py
            # <class 'dict'>... So essentially, we can use json.dump(), and json.load() to serialize and deserialize from json.data to python dictionary
            # And it allows us that free interchange of information.... We change it into a json data for storing, and convert to python dictionary so we can easily work with it in our code
            # Update data   
            # print(type(data))
            website_input.delete(0, END)
            password_input.delete(0, END)
        
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:    
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error: File Not Found", message=f"No data file found ")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            print(f"{email} and {password}")
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists")
            
# if if & else works flawlessly, then use it, instead of using try and except.... 
# Note: An exception is something that happens very rarely, whereas if and else happens frequently, it is pretty often that a user searches your website.
# ONly use exception handling if you don't have another easy alternative
            
# Before json data improvement
# def save():
    
#     website = website_input.get()
#     email = email_input.get()   
#     password = password_input.get()
    
#     if len(website) == 0 or len(email) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
#     else:
#         # Please don't leave any fields empty!
        
#         # messagebox.showinfo(title="Title", message="Message"), also has yesno, okcancel, retrycancel, askquestion, yesnocancel
#         is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?")
        
#         if is_ok:
#             # to close this file automatically without us having to write: file.close()
#             with open("data.txt", "a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_input.delete(0, END)
#                 password_input.delete(0, END)
    
# Standard Dialogs are popups that your tkinter program can generate, most popular is the messagebox(): YesNo, OkCancel, RetryCancel
# # ---------------------------- UI SETUP ------------------------------- #

# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=200, height=200)
# app_logo = PhotoImage(file="logo.png")
# canvas.create_image(100, 112, image=app_logo) #a tuple, containing the x and y positions of our image, and our image name
# canvas.grid(column=1, row=0)
# # canvas.pack()

# website_label = Label(text="Website:")
# website_label.grid(column=0, row=1)

# # Input
# website_input = Entry(width=43)
# website_input.grid(column=1, row=1, columnspan=2)
# website_input.focus()
# # Email/Username
# email_label = Label(text="Email/Username:")
# email_label.grid(column=0, row=2)

# email_input = Entry(width=43)
# email_input.grid(column=1, row=2, columnspan=2)
# email_input.insert(0, "dynasty.dev241@gmail.com")
# # .insert(1: index, 2: string to be inserted) index is where the cursor is... index can be equated to 0 or END... before the text is 0, at the end of the text is END


# # Password
# password_label = Label(text="Password:")
# password_label.grid(column=0, row=3)

# password_input = Entry(width=21)
# # password_input.insert(0, generate_password())
# password_input.grid(column=1, row=3)

# # Generate Password Button
# password_button = Button(text="Generate Password", command=generate_password)
# password_button.grid(column=2, row=3)

# # Add button
# add_button = Button(text="Add", width=35, command=save)
# add_button.grid(column=1, row=4, columnspan=2)


# Improving the UI:
# ---------------------------- UI SETUP ------------------------------- #
BG_COLOR = "#FFFFFF"       # Clean white background
ACCENT_COLOR = "#E74C3C"   # Modern red accent (matches standard MyPass logo)
TEXT_COLOR = "#2C3E50"     # Dark slate gray for softer, modern text
ENTRY_BG = "#F8F9FA"       # Subtle off-white tint for input fields
FONT_LABEL = ("Segoe UI", 10, "bold")
FONT_INPUT = ("Segoe UI", 10)

window = Tk()
window.title("MyPass Password Manager")
window.config(padx=45, pady=40, bg=BG_COLOR)
window.resizable(False, False)  # Prevents awkward window stretching

# Canvas & Logo
canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
app_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=app_logo)
canvas.grid(column=1, row=0, pady=(0, 15))

# Labels (Right-aligned with sticky="e" for a clean form edge)
website_label = Label(text="Website:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_LABEL)
website_label.grid(column=0, row=1, sticky="e", padx=(0, 10), pady=6)

email_label = Label(text="Email/Username:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_LABEL)
email_label.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=6)

password_label = Label(text="Password:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_LABEL)
password_label.grid(column=0, row=3, sticky="e", padx=(0, 10), pady=6)

# Inputs (Stretched cleanly across columns with sticky="ew")
website_input = Entry(bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT_INPUT, relief="solid", bd=1)
website_input.grid(column=1, row=1, sticky="ew", pady=6, ipady=4, padx=10)
website_input.focus()

email_input = Entry(bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT_INPUT, relief="solid", bd=1)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew", pady=6, ipady=4, padx=5)
email_input.insert(0, "dynasty.dev241@gmail.com")

password_input = Entry(width=24, bg=ENTRY_BG, fg=TEXT_COLOR, font=FONT_INPUT, relief="solid", bd=1)
password_input.grid(column=1, row=3, sticky="ew", pady=6, padx=(0, 8), ipady=4)

# Buttons (Flat modern style with cursor pointer)
password_button = Button(
    text="Generate Password",
    command=generate_password,
    bg="#ECF0F1",
    fg=TEXT_COLOR,
    font=("Segoe UI", 9, "bold"),
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=4
)
search_button = Button(
    text="Search",
    command=find_password,
    bg="#ECF0F1",
    fg=TEXT_COLOR,
    font=("Segoe UI", 9, "bold"),
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=4,
    width=12
)
password_button.grid(column=2, row=3, sticky="ew", pady=6)
search_button.grid(column=2, row=1, sticky="ew", pady=6)

add_button = Button(
    text="Add Password",
    command=save,
    bg=ACCENT_COLOR,
    fg="#FFFFFF",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    cursor="hand2",
    pady=6
)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=(12, 0))

window.mainloop()

# pyperclip() a cross-platform python module for copy and paste clipboard functions 
