MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

off = False

report = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money": 0,
}


def make_coffee():
    global off
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        off = True
        return

    if user_choice == "report":
        print(f"Water: {report['water']} ml")
        print(f"Milk: {report['milk']} ml")
        print(f"Coffee: {report['coffee']} g")
        print(f"Money: ${report['money']}")
        return

    resources_sufficient = True

    if user_choice == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > report["water"]:
            print("Sorry not sufficient water. Please order something.")
            resources_sufficient = False
        elif MENU["espresso"]["ingredients"]["coffee"] > report["coffee"]:
            print("Sorry not sufficient coffee. Please order something.")
            resources_sufficient = False
    elif user_choice == "latte":
        if MENU["latte"]["ingredients"]["water"] > report["water"]:
            print("Sorry not sufficient water. Please order something.")
            resources_sufficient = False
        elif MENU["latte"]["ingredients"]["coffee"] > report["coffee"]:
            print("Sorry not sufficient coffee. Please order something.")
            resources_sufficient = False
        elif MENU["latte"]["ingredients"]["milk"] > report["milk"]:
            print("Sorry not sufficient milk. Please order something.")
            resources_sufficient = False
    elif user_choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] > report["water"]:
            print("Sorry not sufficient water. Please order something.")
            resources_sufficient = False
        elif MENU["cappuccino"]["ingredients"]["coffee"] > report["coffee"]:
            print("Sorry not sufficient coffee. Please order something.")
            resources_sufficient = False
        elif MENU["cappuccino"]["ingredients"]["milk"] > report["milk"]:
            print("Sorry not sufficient milk. Please order something.")
            resources_sufficient = False
    else:
        print("You have made a typo.")

    if resources_sufficient:
        pennies = int(input("How many pennies?: $"))
        nickles = int(input("How many nickles?: $"))
        dimes = int(input("How many dimes?: $"))
        quarters = int(input("How many quarters?: $"))

        total_amount = round((0.01 * pennies) + (0.05 * nickles) + (0.10 * dimes) + (0.25 * quarters))

        if (MENU[user_choice]["cost"]) > total_amount:
            return print("Sorry that's not enough money. Money refunded")
        elif (MENU[user_choice]["cost"]) == total_amount:
            report["water"] -= MENU[user_choice]["ingredients"]["water"]
            report["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            report["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            report["money"] += total_amount
            print(f"Here is your {user_choice}, enjoy.")
        elif (MENU[user_choice]["cost"]) < total_amount:
            change = total_amount - MENU[user_choice]["cost"]
            total_amount -= change
            print(f"Here is the change of ${change}.")
            report["water"] -= MENU[user_choice]["ingredients"]["water"]
            report["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            report["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            report["money"] += total_amount
            print(f"Here is your {user_choice}, enjoy.")


while not off:
    make_coffee()


