from itertools import count
from tempfile import mkdtemp
from turtle import onclick


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def measure_resources(drink_choice):
    # TODO: insert docstrings
    for item in drink_choice:
        if drink_choice[item] >= resources[item]:
            print(f"Sorry there is not enough {item}to make your drink. :$")
            return False
    return True


def count_coins():
    # TODO: insert docstrings
    print("Please insert your coins.")
    total = int(input("How many quarters have you got?: ")) * 0.25
    total += int(input("How many dimes have you got?: ")) * 0.10
    total += int(input("How many nickles have you got?: ")) * 0.05
    total += int(input("How many pennies have you got?: ")) * 0.01
    return total


def transaction_status(money_paid, cost_price):
    if money_paid >= cost_price:

        change = round(money_paid-cost_price, 2)
        print(f"Here is your ${change} change.")

        global profit
        profit += cost_price
        return True
    else:
        print("Sorry that is not enough money, please get your bread up.")
        return False


def make_drink(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}! Have a nice day\n")

# TODO: In this project,, I will be attempting to create a mini cofee machine.


power = "on"
while power == "on":
    users_order = input(
        "What would you like to drink today?\n An Espresso\n A Latte\n A Cappuccino\n Note: Please enter only your preffered drinks name.\n Your order: ").lower()

    if users_order == "power":
        power = input(
            "Would you like to turn off this cofee machine or keep it on? (on/off)")

    elif users_order == "report":
        # TODO: print all resources
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money:{profit}\n")

    else:
        drink_choice = MENU[users_order]
        # print(drink_choice)
        print(f"One {users_order} coming up!\n")
        # print(drink_choice["ingredients"])

        if measure_resources(drink_choice["ingredients"]):
            payment = count_coins()
            if transaction_status(payment, drink_choice["cost"]):
                make_drink(users_order, drink_choice["ingredients"])

# TODO: Clear screen after every session.
