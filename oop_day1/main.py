from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cofee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

power = 1
while power == 1:
    options = menu.get_items()
    users_drink_choice = input(
        f"Good evening, what would you like to drink today? ({options}) \nPlease type in only one menu item: ")

    if users_drink_choice == "off":
        power = 0

    if users_drink_choice == "report":
        cofee.report()
        money.report()

    else:
        drink = menu.find_drink(users_drink_choice)
        checking_resources = cofee.is_resource_sufficient(drink)
        if checking_resources:
            print("Alright, time to pay.")
            if money.make_payment(drink.cost):
                cofee.make_coffee(drink)
