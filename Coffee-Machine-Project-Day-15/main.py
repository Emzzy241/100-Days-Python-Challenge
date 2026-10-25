MENU = {
    "espresso": 
    {
        "ingredients": 
        {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
       "ingredients":  
       {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": 
        {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# TODO: 1. Print report of all coffee machine resources

# for resource in resources:
#     print(f"resource: {resource}, you have: {resources[resource]} left.")
# print(resources)

# TODO: 2. Check if resources is sufficient before making the order.
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    # is_enough = True or return True and False
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            # is_enough = False
            return False
        
    return True # can be done alternatively with the commented out is_enough variables
        # print(order_ingredients[item])
        # order_ingredients[item]

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(amount_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if amount_received >= drink_cost:
        # To be able to access profit, which is a global scope inside a local scope, the is_transaction_successful variable, we need
        change = round(amount_received - drink_cost, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕, Enjoy!")
        # 🍵🍵
        # 

is_on = True

while is_on:
# TODO: 3. Prompt user by asking "What would you like (espresso/latte/cappuccino)"
    user_input = input("What would you like (espresso/latte/cappuccino): ").lower()

    # TODO: 4. (in note, it is 2). Turn off the coffee machine
    if user_input == "off":
        is_on = False

    if user_input == "report":
        # for resource in resources:
            # print(f"Resource {resource}, you have: {resources[resource]} left.")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Milk: {resources['coffee']}g")
        print(f"Money: ${profit}")
            # print(f"Water: {resources['resource']}ml")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])














    # # Mine Try:
    # isResourceSufficient(drinkToMake):
    # # find the coffee we want to make:
    # coffeeToBeMade = MENU[drinkToMake]
    # amount_of_water_needed_for_drink = coffeeToBeMade["ingredients"]["water"]
    # if amount_of_milk_needed_for_drink:
    #     amount_of_milk_needed_for_drink = coffeeToBeMade["ingredients"]["milk"]
    # amount_of_coffee_needed_for_drink = coffeeToBeMade["ingredients"]["coffee"]

    # if resources["water"] < amount_of_water_needed_for_drink:
    #     # return "Insufficient Water, more water needed to make this drink"
    #     return False
    # if resources["milk"] < amount_of_milk_needed_for_drink:
    #     return False
    # if resources["coffee"] < amount_of_coffee_needed_for_drink:
    #     return False
    # # for resource in resources:
    # #     # if resource
    # #     print(resource[0])

    # # print(coffeeToBeMade["ingredients"]["water"])
    # # print(f"You need {amount_of_coffee_needed_for_drink} amount of coffee for a{drinkToMake}")
    # # for ingredient in coffeeToBeMade:
    # #     print(f"{ingredient}")
    # #     # if drinkToMake[ingredient] 
    # if (user_input == "espresso"):
    #         print("The Drink to be made is espresso")
    #         if isResourceSufficient(user_input):
    #             penny = int(input("Enter the amount in penny: ")) * 0.01
    #             nickel = int(input("Enter the amount in nickel: ")) * 0.05
    #             dime = int(input("Enter the amount in dime: ")) * 0.1
    #             quarter = int(input("Enter the amount in quarter: ")) * 0.25
    
    #             sum = penny + nickel + dime + quarter
    #             # getting amount of drink ordered to see if user has a change
    #             # if sum > MENU["drinkToMake"]
    #             print(MENU["drinkToMake"])
    
    #             print(f"You paid: {sum}")
    #         else:
    #             print("There is insufficient resources")
    #     elif user_input == "latte":
    #         print("The Drink to be made is latte")
    #     elif user_input == "cappuccino":
    #         print("The Drink to be made is cappuccino")
    #     # else:
    #     #     print("Sorry, I did not get that actually")
    
# print(isResourceSufficient("cappuccino"))
    # find the coffee we want to make:
