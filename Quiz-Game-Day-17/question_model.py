# TODO: 1. Create the Question module have
# It might contain text, and answer.... should be initialized ith a value whenever a new object is created from it.
# e.g., new_q = Question("2+3=5", "True")... The name of our class is Question, because we are modeling what a question should be like in our game

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# Next section is to create a question bank
