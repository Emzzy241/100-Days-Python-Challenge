# Day-28, today we will be building a Pomodoro app with all we have learnt.
# Pomodoro technique book, The Acclaimed Time-Management System That Has Transformed How We Work. By Francesco Cirilo
# The application will allows us to do 25minutes work, 5 minutes break, after 4 of this, then bwe get a 20 minutes break
# A handy tool to achieve more and build more using this pomodoro application.

from tkinter import *
# import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 50
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, timer

    if timer is not None:
        window.after_cancel(timer)
        timer = None

    reps = 0

    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    start_button.config(state="normal")
    # timer_text= 00:00
    # title_label = "Timer"
    # reset check_marks
    # we want to cancel the after

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    start_button.config(state="disabled")

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)

    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    # count_min = math.floor(count /60)
    count_min = count // 60
    count_sec = count % 60
    # this works but these are completely 2 different datatypes
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        # the reason we are able to do this is because of the flexibility of python datatype
        # this feature ain't available in languages like C, Java, C++
        # python is a strongly dynamically typed language
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        # work_sessions = math.floor(reps / 2)
        work_sessions = reps // 2

        for _ in range(work_sessions):
            marks += "✔️"

        checkmarks_label.config(text=marks)

        start_timer()
            
            
        # if reps % 2 == 0:
        #     checkmarks_label.config(text="✔️")

# python dynamic typing helped us to ensure our clock did not do: 5:00
# a = 3, and then doing a = "Hello", this is known as dynamic typing... 
# Python is a very unique language, on one hand it is strongly typed in the sense that it holds on to the datatype of the variable, a is a string... a ^ 2, that is a type error, types matter, quite a lot. That explains python's strong nature
# 
# a function, pow("a") also returns a type error, this is where the language is strongly typed... 
# Now the part where the language is dynamically typed is that, even though it knows what type a variable is, 
# it knows what type a function expects, you can also dynamically change the datatype of any variable like this: a = 3, after initially doing: a = "hello", 
# that is exactly what we are doing here, dynamic typing, changing the datatype from int to string:if count_sec == 0:
        # count_sec = "00"
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro") 
window.config(padx=100, pady=50, bg=YELLOW)


# def say_something(thing, a, b, c):
#     print(thing)
#     print(a)
#     print(b)
#     print(c)

# window.after(1000, say_something, "Hello", 3, 5, 8) // We have now seen how th eafter method works above


# The after method takes the amount of time that it should wait, and then after that amount of time, it simply calls the particular function that you tell it to call, passing in any arguments you want to give it
# The last thing in .after(), the astericks args allows us to put in an unlimited amount of positional arguments, not keyword arguments which is (**kwargs)
# And those unlimited arguments will be the arguments passed into the function, in this case, the say_something() function, and the thingargument

# fgto color a label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# count_down(5)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
checkmarks_label.grid(column=1, row=3)

# some arguments are specific to a widget like file being specific to PhotoImage, while some arguments like bg, padx, etc cut across various widgets
# highlightthickness=0, this helped us get rid of the tiny white background that the tomato had on the canvas.
# we call GUI program timer an event-driven program





window.mainloop()
# In Italian, Pomodoro essentially means tomato
# the tkinter canvas widget is similar to a real-life widget, it allows you to draw something and draw something on top... In our case, it allows us to paste an image into our program and also to place some texts on top of that