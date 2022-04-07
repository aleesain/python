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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
Water = resources["water"]
Milk = resources["milk"]
Coffee = resources["coffee"]
want_coffee = True
while want_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        want_coffee = False
    elif choice == "report":
        print(f'Water: {Water}')
        print(f'Milk: {Milk}')
        print(f'Coffee: {Coffee}')
        print(f'Money: ${money}')
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if choice == "espresso":
            if Water < MENU["espresso"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                continue
        if choice == "latte":
            if Water < MENU["latte"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                continue
        if choice == "cappuccino":
            if Water < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                continue
        print("Please insert coins")
        quarters = int(input("how many quarters: "))
        dimes = int(input("how many dimes: "))
        nickles = int(input("how many nickles: "))
        pennies = int(input("how many pennies: "))
        a_cost = (0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies)
        if choice == "espresso":
            if a_cost < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                change = round(a_cost - MENU["espresso"]["cost"], 2)
                money += MENU["espresso"]["cost"]
                Water -= 50
                Coffee -= 18
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
        elif choice == "latte":
            if a_cost < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                change = round(a_cost - MENU["latte"]["cost"], 2)
                money += MENU["latte"]["cost"]
                Water -= 200
                Milk -= 150
                Coffee -= 24
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
        elif choice == "cappuccino":
            if a_cost < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                change = round(a_cost - MENU["cappuccino"]["cost"], 2)
                money += MENU["cappuccino"]["cost"]
                Water -= 250
                Milk -= 100
                Coffee -= 24
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
    else:
        print("Please write correctly")
