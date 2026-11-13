# Today we will be discussing the Graphical User Interface, GUI using Tkinter in python.
# Yes, previously we did some bit of GUI with Turtle Graphics, we will be doing more advanced stuffs now.
# The inbuilt Tkinter module in python... Talk about buttons, inputs, etc., Also we will cover Advanced Functions such as:
# Default Arguments: * Args, **Kwargs, we will now combine these advanced concepts with Tkinter to build a Unit Converter Application
# This Program can do: Miles to KM, Liters to gallons or any conversion you often use
# Let us begin.... Our goal in today's lesson: To learn about Tkinter... Before GUI, we had MS Console, TUIs
# One of the earliest Computers that incorporated GUIs was the Mac Lisa... Windows is the GUI Operating System from Microsoft... Mac Lisa, 
# first to ever creating GUI, Apple sued Microsoft for stealing their GUI for handling the computer...Biography of Steve Jobs, Walter Isaacson
# Xerox PARC is the inventor of GUI, they created the first GUI put to use in a computer, before Apple or Microsoft ever thought about it
# Xerox also created other things like the Ethernet (LAN), the first OOPL (SMALLTALK), also created first GUI that allowed a user to interact with a computer by pointing and clicking, they even developed the first mouse to do this
# Interested and wanna learn more?? Watch a movie called: Pirates of Silicon Valley

# 3: Creating Windows and Labels with Tkinter

# 4: The **kw, a deep dive of more advanced python arguments
# Functions that can take in unlimited Arguments:
# def add(*args):
#     for n in args:
#         print(n)
# The *args tells python that this function add can accept any number of arguments, and once inside the function you can actually loop through all of the arguments that will be in form of a tuple, and you can do anything you want with those arguments

# import tkinter or import every  component from that module
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Adding padding to all of our widgets... Remember, padding adds space around the widget
window.config(padx=100, pady=100)

def button_clicked():
    print("Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    # my_label.config(text="Button got Clicked")
    # my_label.config()
    

# Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "italic"))
my_label = Label(text="I Am a Label", font=("Arial", 24))
# After creating the component Label, we lay out how that component will be shown on the screen
# my_label.pack(side="left") #our label is now showing and its packed so it can show in the center of our program... We use the packer to pack out text to the middle of the screen
# The packer is a geometry management system, it is a simple way to layout the components that we are building
# packer has a number of options; .expand(), .anchor(), .fill("x, y, both, none"), .side("left or right or top or bottom"), .padx(), .pady()... Read more from link in course resources
# how to configure or change properties of a particular component that we have created
# my_label["text"] = "New Text" or...
my_label.config(text="New Text")
my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button

button = Button(text="Click Me", command=button_clicked) # remember it iis the name of the function and not calling the function
# Do not forget, in order to make anything appear on screen, it needs to have a layout, so we use: pack()
# button.pack(side="left")
button.grid(column=1, row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
# input.pack(side="left")
# button_clicked(input)

# Using Advanced Python Arguments in order to specify a wider range of inputs **kw
# When keywords are used, the order of the arguments does not matter, Python matches by name and not by position
# 3 widgets: Label, Button, Input

# Tkinter layout managers: tkinter has different layout managers that then defines how to position each of the widget in your GUI program
# There are 3 you should know about; Pack, Place, and Grid
# All Pack does is it packs each of the widgets next to each other in a vaguely logical format... By default, Pack always starts at the top and then pack every other widget below the previous one
# Pack is a bit difficult with specific position that you want
# Up Next is Place... Place is all about precise positioning
# Note again: If a widget is specified and has no layout manager with it such as pack, place or grid, the widget would not show
# End of your program
# the downside of place is it is soooo specific, and we need to calculate the coordinate in our head
# The final layout manager is the Grid... The Grid is a really simple concept, it imagines your entire program is a grid and you can manage it to any number of rows or columns that you want to
# Grid is the easiest way to work with layouts... Note(WARNING): You cannot mix-up grid and pack in the same program... You cannot use grid for one widget, and pack() for another widget in the same application, they will counter each other


window.mainloop()
