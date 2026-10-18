# import random
# from art import logo

# # Also assuming we have an infinite deck, when a card is drawn we know there is high probability of that same card occuring again.
# # But in a real casino, they have maybe 6 or 8 decks of card, so a finite deck, there is a much lower probability of same card 
# # re-occurring again and again. This is how professional card counters, the people that the casinos hate the most 
# # actually go about trying to improve their chances... But in our game, we will keep things simple. We assume that each of these cards in our game have 
# # an equal chance of re-occurring.
# # normal, hard, extra hard, and expert.
# # There is a flowchart also to break down the game actually.

# # Let us now begin, shall we begin? Yes we shall.


# def deal_card():
#     """Reruns a random card from the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
#     random_card = random.choice(cards)
#     # print(random_card)
#     return random_card

# def calculate_score(cards):
#     """Takes a list of cards and return the score calculated from the cards"""
#     if sum(cards) == 21 and len(cards) == 2: # or: if 11 in cards and 10 in cards and len(cards) == 2:, saying: a hand with only 2 cards that contains 11 & 10
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(u_score, c_score):
#     if u_score == c_score:
#         return "Draw"
#     elif c_score == 0:
#         return "Lose, Opponent has a Blackjack"
#     elif u_score == 0:
#         return "You win, you have a Blackjack"
#     elif u_score > 21:
#         return "You lose, you went over"
#     elif c_score > 21:
#         return "You win, computer went over"
#     elif u_score > c_score:
#         return "You win, you were closer"
#     else:
#         return "You lose, computer was closer"

# # Step-5: Deal User and computer 2 cards each using the deal_card() function.
# # user_cards = []
# # computer_cards = []
# # is_game_over = False
# # computer_score = -1 # Ensuring computer_score always have a value
# # user_score = -1 # Ensuring user_score always have a value
    
# # # Remember: if, elif statements read from top-to-bottom. Look at the order. If computer score is = 0, it will never get to the 5th 
# # # elif statements because we would have broken out of the function before that condition is reached.

# # for _ in range(2):
# #     user_cards.append(deal_card())
# #     computer_cards.append(deal_card())
# #     # Instead of 4 lines of code, we have 2 lines of code instead
# #     # new_card = deal_card()
# #     # user_cards.append(new_card)

# # while not is_game_over:

# #     # print(f"user cards: {user_cards}, computer cards: {computer_cards}")
# #     # Hint 6: A function called calculate_score() that takes a list of cards as input and returns the sum of all the cards in the list as the score.
# #     # Google the sum() function if need be.

# #     # def calculate_score():
# #     #     user_cards_sum = sum(user_cards)
# #     #     computer_cards_sum = sum(computer_cards)

# #     #     return f"User score is {user_cards_sum} and Computer score is {computer_cards_sum}"

# #     # print(calculate_score())

# #     # What was expected is:
# #     # def calculate_score():
# #     #     return sum(cards)

# #     # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards ace + 10) and return 0 instead of the actual score. 
# #     # 0 will represent a blackjack in our game.
# #     # We already established it that11 will represent our ace.
# #     # Updating the calculate_score() function now

# #     # def calculate_score(cards):
# #     #     if sum(cards) == 21 and len(cards) == 2: # or: if 11 in cards and 10 in cards and len(cards) == 2:, saying: a hand with only 2 cards that contains 11 & 10
# #     #         return 0
# #     #     return sum(cards)

# #     # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 from the cards,
# #     # and replace it instead with a 1. Remember, an ace can either be 1 or 11. list.remove() searches for the first occurrence of a number in a list and removes it.


# #     # Hint 9: Call the calculate_score() function if the computer or the user has a blackjack (0) or if the user's score is over 21. Then the game ends
# #     # We cleaned up our code by moving calculate_score() to the top. Remember to add a doc string in your functions for documentation """"""

# #     user_score = calculate_score(user_cards)
# #     computer_score = calculate_score(computer_cards)

# #     print(f"User's cards: {user_cards} and user's current score: {user_score}")
# #     print(f"Computer's first card: {computer_cards[0]}")

# #     if user_score == 0 or computer_score == 0 or user_score > 21:
# #         is_game_over = True
# #     else:
# #         user_should_deal = input("Would you like to draw another card? enter 'y' for yes or 'n' for no: ")

# #     if user_should_deal == 'y':
# #         user_cards.append(deal_card())
# #         # user_score = calculate_score(user_cards)
# #         # print(f"User's cards: {user_cards} and user's current score: {user_score}")
# #     else:
# #         is_game_over = True

# # while computer_score != 0 and computer_score < 17:
# #     computer_cards.append(deal_card())
# #     computer_score = calculate_score(computer_cards)

# # # Calling compare() function here after both the user and the computer are done with drawing up cards.
# # print(f"Your final hand: {user_cards}, final score: {user_score}")
# # print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
# # print(compare(user_score, computer_score))

# def play_game():
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#     computer_score = -1
#     user_score = -1
        
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#     while not is_game_over:

#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)

#         print(f"User's cards: {user_cards} and user's current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Would you like to draw another card? enter 'y' for yes or 'n' for no: ")

#         if user_should_deal == 'y':
#             user_cards.append(deal_card())
#         else:
#             is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     print("\n" * 20)
#     play_game()


# # Hint-10:  If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function
# # to add another card to the user_cards List. If no, then the game has ended.

# # if is_game_over != True:
# #     print"w

# # Hint 11: The score will need to be rechecked upon every new card drawn and the checks in Hint 9 need to be repeated until the game ends

# # Hint 12: Once user is done, it is time to let computer play, the computer should keep trying cards as long as it has a score < 17

# # So the while loop is responsible for as long as the user keeps wanting to play and drawing up cards, and once that is done, 
# # we can now focus on the computer.

# # Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
# # If the computer & user both have the same score, then its a draw.
# # If the computer has a blackjack (0), then the user loses
# # If the user has a blackjack (0), then the user wins
# # If the user_score is over 21, then the user loses
# # If the computer_score is over 21, then the computer loses.
# # If none of the above, then the player with the highest score wins.

# # Hint-14: Ask the user if they want to restart the game, if they answer yes, clear the console and restart the game






# Beautifying the game now with Claude. What I built step-by-step is up. What I am to study, the better UI is down:


import random

# ---------------------------------------------------------------------------
#  UI HELPERS  (display only - none of this touches the game rules)
# ---------------------------------------------------------------------------

# ANSI colour codes. Most terminals support them (VS Code, macOS, Linux, Windows Terminal).
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"

SUITS = ["♠", "♥", "♦", "♣"]

BANNER = [
    r" ,******,                                                    ",
    r"|A_    _.|      _     _             _      _             _   ",
    r"|K V )...|     | |__ | | __ _  __  | |__  (_) __ _  __  | |__",
    r"|\ /|K /\|     | '_ \| |/ _` |/ _| | / /  | |/ _` |/ _| | / /",
    r"| V |/ \ |     |_.__/|_|\__,_|\__| |_\_\ _/ |\__,_|\__| |_\_\ ",
    r"'....|\ / |                             |__/                 ",
    r"     | V K|                                                  ",
    r"     '****'                                                  ",
]


def clear_screen():
    """Wipes the terminal (replaces the old print("\\n" * 20))."""
    print("\033[2J\033[H", end="")


def show_banner():
    for line in BANNER:
        print(f"{GREEN}{BOLD}{line}{RESET}")
    print()


def show_title_bar():
    """A slim header used while a game is in progress."""
    print(f"{GREEN}{BOLD}♠ ♥  B L A C K J A C K  ♦ ♣{RESET}")
    print(f"{DIM}{'─' * 40}{RESET}")


def card_lines(value, index=0, hidden=False):
    """Returns the 5 text rows that draw one card.
    The deck only stores numbers, so the suit is picked from the value and
    position - purely cosmetic, but stable between redraws."""
    if hidden:
        return [f"{BLUE}{row}{RESET}" for row in
                ["┌─────┐", "│░░░░░│", "│░░░░░│", "│░░░░░│", "└─────┘"]]

    rank = "A" if value in (11, 1) else str(value)
    suit = SUITS[(value + index) % 4]
    colour = RED if suit in "♥♦" else WHITE
    rows = [
        "┌─────┐",
        f"│{rank:<2}   │",
        f"│  {suit}  │",
        f"│   {rank:>2}│",
        "└─────┘",
    ]
    return [f"{colour}{row}{RESET}" for row in rows]


def render_hand(cards, hide_after=None):
    """Draws a whole hand side by side. If hide_after is set, every card from
    that position onwards is shown face-down."""
    drawn = []
    for i, card in enumerate(cards):
        hidden = hide_after is not None and i >= hide_after
        drawn.append(card_lines(card, i, hidden))
    return ["  " + " ".join(card[row] for card in drawn) for row in range(5)]


def format_score(score):
    """The game uses 0 to mean Blackjack, so show that in words."""
    if score == 0:
        return f"{YELLOW}{BOLD}BLACKJACK!{RESET}"
    if score > 21:
        return f"{RED}{BOLD}{score} (bust){RESET}"
    return f"{BOLD}{score}{RESET}"


def show_hand(title, colour, cards, score_text, hide_after=None):
    print(f"{colour}{BOLD}{title}{RESET}  {DIM}│{RESET}  Score: {score_text}")
    for line in render_hand(cards, hide_after):
        print(line)
    print()


def show_result(message):
    """Prints the outcome in a coloured box."""
    if message.startswith("You win"):
        colour = GREEN
    elif message == "Draw":
        colour = YELLOW
    else:
        colour = RED
    width = len(message) + 4
    print(f"{colour}{BOLD}╔{'═' * width}╗")
    print(f"║  {message}  ║")
    print(f"╚{'═' * width}╝{RESET}")
    print()


# ---------------------------------------------------------------------------
#  GAME LOGIC  (unchanged)
# ---------------------------------------------------------------------------

def deal_card():
    """Reruns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    random_card = random.choice(cards)
    # print(random_card)
    return random_card

def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2: # or: if 11 in cards and 10 in cards and len(cards) == 2:, saying: a hand with only 2 cards that contains 11 & 10
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent has a Blackjack"
    elif u_score == 0:
        return "You win, you have a Blackjack"
    elif u_score > 21:
        return "You lose, you went over"
    elif c_score > 21:
        return "You win, computer went over"
    elif u_score > c_score:
        return "You win, you were closer"
    else:
        return "You lose, computer was closer"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # --- screen: your hand face-up, computer's second card hidden ---
        clear_screen()
        show_title_bar()
        show_hand("COMPUTER", CYAN, computer_cards, f"{DIM}?{RESET}", hide_after=1)
        show_hand("YOU", GREEN, user_cards, format_score(user_score))

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(f"{YELLOW}Draw another card?{RESET} "
                                     f"{DIM}[y = yes, n = no]{RESET} ")

        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # --- final screen: everything revealed ---
    clear_screen()
    show_title_bar()
    show_hand("COMPUTER", CYAN, computer_cards, format_score(computer_score))
    show_hand("YOU", GREEN, user_cards, format_score(user_score))
    show_result(compare(user_score, computer_score))


# ---------------------------------------------------------------------------
#  MAIN LOOP
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    clear_screen()
    show_banner()
    while input(f"{YELLOW}Do you want to play a game of Blackjack?{RESET} "
                f"{DIM}[y / n]{RESET} ") == "y":
        play_game()
        print(f"{DIM}{'─' * 40}{RESET}")