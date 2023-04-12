from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

while machine_on:
    coffee_choice = input(f" What would you like? {menu.get_items()}:").lower()
    if coffee_choice == "off":
        machine_on = False
    elif coffee_choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        item = menu.find_drink(coffee_choice)
        if coffee_machine.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_machine.make_coffee(item)