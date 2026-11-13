def add(*args):
    print(args[2])
    sum = 0
    for n in args:
        # sum += args[n] + args[n + 1]
        sum += n
    return sum

# def add(*args):
#     print(type(args))

# The asterisks keyword packs all the numbers and we can loop through and do whatever we want
# Unlimited Arguments using this asterisks is also known as Unlimited Positional Arguments

# print(add(1, 2, 3, 4, 5, 6))

# To refer to our arguments by name instead of position
# **kwargs: Many
# Keyworded Arguments

# Double asterisks allows us to work with an arbitrary number of keyword arguments

def calculate(n, **kwargs):
    # print(type(kwargs))
    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value )
        # print(kwargs["add"])
    n += kwargs["add"] #starts with n, which is 2,... 2+3 = 5
    n *= kwargs["multiply"] # then moves on to multiply, it picks up from where it left off which is with 5, and 5*5 = 25
    print(n)

calculate(2, add=3, multiply=5)
# All of the above now explains why  tkinter.Label() does not bring out all the arguments in the Label but only just **kwards.
# Tkinter was written in a different language called tk, and in order for python to be able to use tk and tkinter, all of these arguments are stored with **kwargs, many keyword positional arguments

class Car:
    
    def __init__(self, **kw):
        # self.make = kw["make"] or
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        # The benefit of get(), is if the key does not exist in this dictionary, it will just return none and would not lead to an error
        
        
my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)

# Car()--> By doing this and clicking in between the (), we see: (**kw: Any) -> Car, which indicates kw
# Now we created a class with a lot of optional arguments... Not specifying color or seats when instantiating the Car()class does not lead to any error because we now have unlimited keyworded arguments
# Again, tkinter model was converted from another language, and the most efficient way for them to be able to do this was with classes that have unlimited keyworded arguments
