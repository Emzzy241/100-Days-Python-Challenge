import os
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Makes ANSI colours work in Windows terminals too
os.system("")

# ---------- Styling helpers (decoration only) ----------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
PURPLE = "\033[38;5;141m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

WIDTH = 54


def line(char="─", colour=PURPLE):
    print(f"{colour}{char * WIDTH}{RESET}")


def banner():
    print()
    print(f"{PURPLE}╔{'═' * (WIDTH - 2)}╗{RESET}")
    print(f"{PURPLE}║{RESET}{BOLD}{CYAN}{'🧠  PYTHON & TECH QUIZ  🧠'.center(WIDTH - 2)}{RESET}{PURPLE}║{RESET}")
    print(f"{PURPLE}║{RESET}{DIM}{'Answer True or False. Good luck!'.center(WIDTH - 2)}{RESET}{PURPLE}║{RESET}")
    print(f"{PURPLE}╚{'═' * (WIDTH - 2)}╝{RESET}")
    print()


def result_message(score, total):
    percent = (score / total) * 100 if total else 0
    if percent == 100:
        return f"{GREEN}🏆 Perfect score! You're a genius!{RESET}"
    elif percent >= 70:
        return f"{GREEN}🎉 Great job! Well done!{RESET}"
    elif percent >= 40:
        return f"{YELLOW}👍 Not bad! A little more practice and you'll ace it.{RESET}"
    return f"{RED}📚 Keep learning, you'll get there!{RESET}"


# ---------- original logic ----------
# TODO: Create a question bank:
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

banner()

while quiz.still_has_question():
    #if quiz still has questions remaining:
    quiz.next_question()
    line("·")


print()
line("═")
print(f"{BOLD}{CYAN}  ✅ You've completed the Quiz{RESET}")
print(f"{BOLD}  Your final score was: {GREEN}{quiz.score}{RESET}{BOLD}/{quiz.question_number}{RESET}")
print(f"  {result_message(quiz.score, quiz.question_number)}")
line("═")
# Above can also be done like the one below since the length of our question data is going to be the same with our final question number
# print(f"Your final score was: {quiz.score}/len(question_data)")
print()



# Before game beautification
# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain

# # TODO: Create a question bank:
# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_question(): 
#     #if quiz still has questions remaining:
#     quiz.next_question()


# print("You've completed the Quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
# Above can also be done like the one below since the length of our question data is going to be the same with our final question number
# print(f"Your final score was: {quiz.score}/len(question_data)")


# print(question_bank[0].text)

# QuizBrain

# How I solved it initially, I totally got what the actual task was, I totally got it wrong.
# questionIdx = 0
# for question in question_data:
#     # print(question_data[questionIdx]["text"])
#     # questionIdx += 1
#     # print(qu)
#     game_question = Question(question_data[questionIdx]["text"], question_data[questionIdx]["answer"])
#     questionIdx += 1
    # print(game_question.answer)

    # question_data[0]["text"]


# print(question)