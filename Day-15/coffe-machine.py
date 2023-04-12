import inventory

machine_on = True

def check_resource(coffee_choice):
    for i in inventory.MENU[coffee_choice]["ingredients"]:
        if inventory.MENU[coffee_choice]["ingredients"][i] > inventory.resources[i]:
            # print("enough")
            print(f"Sorry not enough {i}")
            return False
    return True

def process_coins(coffee_choice):
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))*0.25
    dimes = int(input("how many dimes?:"))*0.10
    nickles = int(input("how many nickles?:"))*0.05
    pennies = int(input("how many pennies?:"))*0.01
    total = quarters+dimes+nickles+pennies
    if total > inventory.MENU[coffee_choice]["cost"]:
        change = total - inventory.MENU[coffee_choice]["cost"]
        inventory.resources["money"] += inventory.MENU[coffee_choice]["cost"]
        print(f"Here is the ${round(change, 2)}.")
        return True
    elif total == inventory.MENU[coffee_choice]["cost"]:
        inventory.resources["money"] += inventory.MENU[coffee_choice]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_choice):
    for i in inventory.MENU[coffee_choice]["ingredients"]:
        inventory.resources[i] -= inventory.MENU[coffee_choice]["ingredients"][i]
    print(f"Here is your {coffee_choice} ☕️. Enjoy!")



def report():
    print(f'Water: {inventory.resources["water"]}ml\nMilk: {inventory.resources["milk"]}ml\nCoffee: {inventory.resources["coffee"]}g\nMoney: ${inventory.resources["money"]}  ')


while machine_on:
    coffee_choice = input(" What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_choice == "off":
        machine_on = False
        exit()
    elif coffee_choice == "report":
        report()
    elif coffee_choice == "latte" or "espresso" or "cappuccino":
        if check_resource(coffee_choice):
            if process_coins(coffee_choice):
                make_coffee(coffee_choice)