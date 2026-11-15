# We are building MyPass, A Password Manager
# Not an internetbased service, but we will be storing this newly generated password for us inside a txt file which will be completely offline, off the grid
# As soon as we click on GeneratePassword, it not only generates a strong password, it also copies it to your clipboard
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
app_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=app_logo) #a tuple, containing the x and y positions of our image, and our image name
# canvas.grid(column=1, row=1)
canvas.pack()

window.mainloop()