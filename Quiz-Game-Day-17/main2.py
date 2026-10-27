# Building a Quiz in Python
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # print("new user being created...")
        # inside here, we initialize/create starting values for our attributes. 
        # NOTE: init function will be called every time you create a new object from this class. The id is the attribute for every car, we can add many more
        #  When you add parameters to the constructor (which is the __init__ function), you are now saying that whenever a new object is being constructed
        # From this class, it must provide these 2 pieces of data (user_id, and username)

    # This method allows person A to follow person B, vice versa
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "dynasty")
# user_1.id = "001"
# user_1.username = "Dynasty"

# print(user_1.followers)
# def function():
#     pass

user_2 = User("002", "dagreat")
user_1.follow(user_2)

print(user_1.followers) # 0
print(user_1.following) # 1
print(user_2.following) # 0
print(user_2.followers) # 1

# If you don't want to write anything inside a class or inside a function

# Time to start building our Quiz Game.