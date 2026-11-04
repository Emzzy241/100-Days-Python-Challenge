# Let us now learn about File Management System.
# We can get python to do al of the repetitive tasks we do not want to do. 
# First, let's improve our snake game, Day
# We gonna be learning how to open, read write to a file, all without touching the mouse.
# The .txt file we created can be text edit on mac, and notepad on windows

# def open(
#     file: FileDescriptorOrPath,
#     mode: OpenTextMode = "r",
#     buffering: int = -1,
#     encoding: str | None = None,
#     errors: str | None = None,
#     newline: str | None = None,
#     closefd: bool = True,
#     opener: _Opener | None = None
# ) -> TextIOWrapper[_WrappedBuffer]: ...

# Opening up the file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close() # We need to close the file because once python opens up that file, it basically takes up some of the resources of your computer
# And at some point later, it may decide to close it and free up those resources, but we don't know when that is going to happen, and if it will ever happen
# so instead, we will tell it to close the file manually using the file.close()... It is similar to making your computer operate at its best by using the actual amount of tabs that you need
# Every extra tab is going to add a little bit of burden to your computer, and especially if you are using a very heavy application 
# like chrome which likes to take up a lot of resources of your CPU and your computer, ig you have more than 20 or 30 tabs opened, you will notice a significant decrease
# in the speed of your computer... So, a Computer Tip as well as Programming tip, always close down tabs that you have opened and always close down files that you have opened
# 

# Many Python Developers opt for the following because one can forget to close a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    
    # Now we no longer need to remember to close a file.... How Dr. Angela wishes something similar exists for tabs
    
    # Writing to a file
# with open("my_file.txt", mode="w") as file:
#     contents = file.write("New Text")
    
    # Append to a file: TO prevent all we previously wrote from disappearing and thus, we adding to it. Very similar to list.append()
# with open("my_file.txt", mode="a") as file:
#     contents = file.write("\nNew Text")
    
# # Important: Opening a file in write mode and that file does not exist, it will create it for you from scratch
# with open("new_file.txt", mode="w") as file:
#     contents = file.write("New Text")
    
# NOTE: The Above only works in the write mode, and when the file does not exist.

# Learning file paths now
# / is essentially the root, the origin of our file path 
# The root on a Mac is a Macintosh HD, and that root is represented by a simple / (slash)
# A path is similar to the direction, it is a way for the computer to navigate to the file of interest. E.g; /Work/Project/talk.ppt
# Known as an absolute file path, and absolute file paths always start of relative to the root, so you will always see a forward slash to begin with
# Sometimes, you see a C: for windows, on a Mac, you'll just see a forward slash. This absolute file path is basically a path that starts from the origin (the root of the computer storage system)
# A Relative file Path also exists.... Looking at this:
# /root
#     |-Work
#     |- report.doc
#     |-Project
#         |-talk.ppt # To get here, we know the absolute file path is /Work/Project/talk.ppt

# Once we have established our current working directory, then we can use a relative file path to get to a file that we are interested in.
# From Project/ folder, the relative file path is just ./talk.ppt, ./ signifies; look in the current folder for this file named talk.ppt
# If we were in the Work/ folder, to get to the talk.ppt, the absolute file path will never change, but the relative file path would be: ./Project/talk.ppt
# To go upwards. While inside Project to get into report.doc, we do ../report.doc --> The 2 dots represent going 1-step up in the hierarchy to the parent folder which is the Work/ folder
# Same directory, to get hold of report.doc, we use ./report.doc... This explains why we have been able to open the my_file.txt which is in same folder with our main.py

# Challenge Now: For the absolute Path
with open("C:/Users/User/Desktop/Mini-Desktop/100DaysOfCode-Dr. Angela Yu/my_file.txt") as file:
    contents = file.read()
    print(contents)
    
# For relative path
with open("../my_file.txt") as file:
    contents = file.read()
    print(contents)
    
# A peculiarity between files on mac and windows.
# ?On Mac, each file is separated with a /, while on a windows it is \ (a backslash)
# Note: When writing python code, we do not really care about that and we can just write it with backward slash and be good to go.
# Absolute paths follows from the root path: On Windows C:\... For Mac it is \Users\...

# Main Difference between Absolute file path and relative file path is that:
# The Absolute file path is always relative to the root of your computer (windows it is C Drive, on a mac it is the Macintosh HD)
# The relative file path is relative to your current working directory, so it depends on where you are, and where you are trying to get to.
# Depending on the situation, you may decide to use any of the 2.