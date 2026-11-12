# turtle only works with the gif image, that is why we have a .gif image

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(height=491, width=725)
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
# print(all_states)

# No more need for this code below because we already have our x and y values for all the 50 states in USA
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # an alternative way of keeping our screen opened even after our code has finished  running, it is similar to screen.exitonclick()
# A conscience check


# print(answer_state)

while len(guessed_states) < 50: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    # If answer_state is one of the states in all of the states in the states_csv
    if answer_state == "Exit":
        # Save the missing states to a .csv
        # for state in all_states:
        #     if state not in guessed_states:
            
        #         # Save the missing states to a CSV
        #         missing_states = [
        #             state for state in all_states
        #             if state not in guessed_states
        #         ]
        #         states_to_learn = pandas.DataFrame({
        #             "state": missing_states
        #         })

        #         states_to_learn.to_csv("states_to_learn.csv", index=False)

        # Alternative way
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        # Following the format:
        # missing_states = [new_item for item in list if test]
        # The one line below saved us 4 lines of code
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        # print(missing_states)
        # rewriting things with a List Comprehension
        
        
        break
    # had to prevent repetition of states. Previously, Alabama multiple times kept increasing the state score counter
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        print(state_data)
        t.goto(state_data.x.item(), state_data.y.item())
        # t.write(state_data.state.item()) or:
        t.write(answer_state)
        #If they got it right:
            #Create a turtle to write the name of th estate at the state's x and y coordinate
# screen.exitonclick()

# Sa

    
# states_to_learn = pandas.DataFrame(data_dict)
# states_to_learn.to_csv("states_to_learn.csv")


# Updating code to not just be a game but an educational tool that generates a csv file of all the states that was missed

# In life, the only certainties are debt and taxes. In programming, the only certainties are bugs and errors
# panda series is like a column from our database. item() is a method on the pandas series. It looks into the underlying data and it grabs the first element