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

water_resource = resources["water"]
milk_resource = resources["milk"]
coffee_resource = resources["coffee"]
money = 0

def coin_checker():
    quarter_amount = float(input("how many quarters? "))
    dimes_amount = float(input("how many dimes? "))
    nickles_amount = float(input("how many nickles? "))
    penny_amount = float(input("how many pennies? "))
    total_quarter = quarter_amount * 0.25
    total_dimes = dimes_amount * 0.10
    total_nickles = nickles_amount * 0.05
    total_pennies = penny_amount * 0.01
    grand_total = total_quarter + total_dimes + total_nickles + total_pennies
    return grand_total

def run_machine():
    machine_running = True
    while machine_running:
        global water_resource, money, coffee_resource, milk_resource
        choice = input("What drink would you like? (espresso, latte, cappuccino) ").lower()
        if choice == "report":
            print(f"Water: {water_resource}")
            print(f"Milk: {milk_resource}")
            print(f"Coffee: {coffee_resource}")
            print(f"Money: ${money}")

        elif choice == "espresso":
            grand_total = coin_checker()
            cost = MENU["espresso"]["cost"]
            if grand_total >= cost:
                if MENU["espresso"]["ingredients"]["water"] <= water_resource and MENU["espresso"]["ingredients"]["coffee"] <= coffee_resource:
                    print("Here is your drink! Enjoy!")
                    water_resource -= MENU["espresso"]["ingredients"]["water"]
                    coffee_resource -= MENU["espresso"]["ingredients"]["coffee"]
                    money += cost
                    if grand_total > cost:
                        print(f"Here is your change: {grand_total - cost:.2f}")
                else:
                    print("sorry there are not enough resources.")
            else:
                print("Sorry you didn't insert enough money.")

        elif choice == "latte":
            grand_total = coin_checker()
            cost = MENU["latte"]["cost"]
            if grand_total >= cost:
                if MENU["latte"]["ingredients"]["water"] <= water_resource and MENU["latte"]["ingredients"][
                    "coffee"] <= coffee_resource and MENU["latte"]["ingredients"]["milk"]:
                    print("Here is your drink! Enjoy!")
                    water_resource -= MENU["latte"]["ingredients"]["water"]
                    coffee_resource -= MENU["latte"]["ingredients"]["coffee"]
                    milk_resource -= MENU["latte"]["ingredients"]["milk"]
                    money += cost
                    if grand_total > cost:
                        print(f"Here is your change: {grand_total - cost:.2f}")
                else:
                    print("sorry there are not enough resources.")
            else:
                print("Sorry you didn't insert enough money.")

        elif choice == "cappuccino":
            grand_total = coin_checker()
            cost = MENU["cappuccino"]["cost"]
            if grand_total >= cost:
                if MENU["cappuccino"]["ingredients"]["water"] <= water_resource and MENU["cappuccino"]["ingredients"][
                    "coffee"] <= coffee_resource and MENU["cappuccino"]["ingredients"]["milk"]:
                    print("Here is your drink! Enjoy!")
                    water_resource -= MENU["cappuccino"]["ingredients"]["water"]
                    coffee_resource -= MENU["cappuccino"]["ingredients"]["coffee"]
                    milk_resource -= MENU["cappuccino"]["ingredients"]["milk"]
                    money += cost
                    if grand_total > cost:
                        print(f"Here is your change: {grand_total - cost:.2f}")
                else:
                    print("Sorry there are not enough resources.")
            else:
                print("Sorry you didn't insert enough money.")

        elif choice == "off":
            machine_running = False

        else:
            print("Please type a valid function.")

run_machine()

