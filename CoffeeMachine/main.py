from pickle import GLOBAL

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
PROFIT=0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def print_report():
    print(f"Water : {resources['water']}ml \nMilk : {resources['milk']}ml \nCoffee : {resources['coffee']}g \nMoney : ${PROFIT} \n")


def is_enough_resources(user_choice):
    for key in MENU[user_choice]['ingredients']:
        if MENU[user_choice]['ingredients'][key]>resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def process_coins():
    quarters=float(input("how many quarters?: "))
    dimes=float(input("how many dimes?: "))
    nickles=float(input("how many nickles?: "))
    pennies=float(input("how many pennies?: "))
    total= (0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
    return total


def transaction_successful(user_choice,money_received):
    global PROFIT  # Explicitly declare the global variable
    if MENU[user_choice]['cost']>money_received:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif MENU[user_choice]['cost']<=money_received:
        change=round(money_received-MENU[user_choice]['cost'],2)
        print(f"Here is {change} dollars in change.")
        PROFIT = PROFIT + MENU[user_choice]['cost']
        return True


def make_coffee(user_choice):
    for key in MENU[user_choice]['ingredients']:
        resources[key]-=MENU[user_choice]['ingredients'][key]
    print(f"Here is your {user_choice}. Enjoy!")


while(1<2):
    users_choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if users_choice=='report':
        print_report()
    elif users_choice=='off':
        exit()
    else:
        if is_enough_resources(users_choice)==True:
            money_received=process_coins()
            if transaction_successful(users_choice,money_received)==True:
                make_coffee(users_choice)

