import os
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Makes ANSI colours work in Windows terminals too
os.system("")

# ---------- Styling helpers (decoration only) ----------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
BROWN = "\033[38;5;130m"
CREAM = "\033[38;5;223m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"

WIDTH = 50


def line(char="─"):
    print(f"{BROWN}{char * WIDTH}{RESET}")


def banner():
    print()
    print(f"{BROWN}╔{'═' * (WIDTH - 2)}╗{RESET}")
    print(f"{BROWN}║{RESET}{BOLD}{CREAM}{'☕  COFFEE MACHINE ☕'.center(WIDTH - 2)}{RESET}{BROWN}║{RESET}")
    print(f"{BROWN}║{RESET}{DIM}{'Fresh • Hot • Made just for you'.center(WIDTH - 2)}{RESET}{BROWN}║{RESET}")
    print(f"{BROWN}╚{'═' * (WIDTH - 2)}╝{RESET}")


def show_menu(items):
    print(f"\n{BOLD}{CREAM}  Today's Menu{RESET}")
    line()
    for item in str(items).strip("/").split("/"):
        if item:
            print(f"  {CYAN}•{RESET} {item.capitalize()}")
    line()
    print(f"  {DIM}Type a drink name, 'report' for status, or 'off' to quit{RESET}\n")


def section(title):
    print(f"\n{BOLD}{YELLOW}▌ {title}{RESET}")
    line("·")


# ---------- Your original logic ----------
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# print(menu.get_items())
# print(menu.find_drink("latte"))

# TODO: 1. Print report of all the coffee machine resources
# print(coffee_maker.report())

# TODO: 2. Check if resources is sufficient before making the order.
# print(coffee_maker.is_resource_sufficient("espresso"))


is_on = True

banner()
show_menu(menu.get_items())

while is_on:
    choice = input(f"{BOLD}{BROWN}☕ Enter the drink you want to take: {RESET}")

    if choice == "off":
        is_on = False
        print(f"\n{CREAM}  Machine shutting down. Goodbye! 👋{RESET}\n")
    if choice == "report":
        section("Machine Report")
        coffee_maker.report()
        money_machine.report()
        line()
    else:
        drink = menu.find_drink(choice)
        print(f"\n{GREEN}✔ You selected:{RESET} {BOLD}{drink.name.capitalize()}{RESET} "
              f"{DIM}(Cost: ${drink.cost}){RESET}")
        # print(coffee_maker.is_resource_sufficient(drink))
        if coffee_maker.is_resource_sufficient(drink=drink):
        # payment = round(money_machine.process_coins(), 2)
        # payment = money_machine.process_coins()
        # break
        # print(payment)
        # print(money_machine.make_payment(drink.cost))
            section("Payment")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print(f"{GREEN}{BOLD}  ✨ Enjoy your drink! ✨{RESET}")
        line("═")
        print()



# Built it by myself, and outsourced little helps here and there 
# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

# menu = Menu()
# coffee_maker = CoffeeMaker()
# money_machine = MoneyMachine()
# # print(menu.get_items())
# # print(menu.find_drink("latte"))

# # TODO: 1. Print report of all the coffee machine resources
# # print(coffee_maker.report())

# # TODO: 2. Check if resources is sufficient before making the order.
# # print(coffee_maker.is_resource_sufficient("espresso"))


# is_on = True

# while is_on:
#     choice = input("Enter the drink you want to take: ")
    
#     if choice == "off":
#         is_on = False
#     if choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         print(f"You selected: {drink.name} (Cost: ${drink.cost})")
#         # print(coffee_maker.is_resource_sufficient(drink))
#         if coffee_maker.is_resource_sufficient(drink=drink):
#         # payment = round(money_machine.process_coins(), 2)
#         # payment = money_machine.process_coins()
#         # break
#         # print(payment)
#         # print(money_machine.make_payment(drink.cost))
#             if money_machine.make_payment(drink.cost):
#                 coffee_maker.make_coffee(drink)
            