MENU = {
    "espresso": {
        "ingredients": {
            "milk":0,
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

bank = {
    "money": 0,
}


def start_coffie_machine():
    Cof_Input = input("What would you like? (espresso / latte / cappuccino):")
    return Cof_Input


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {bank['money']}")


def check_resourses(Input):
    flag = 1
    for res in resources:
        if resources[res] > MENU[Input]['ingredients'][res]:
            flag = 1
        else:
            print("Sorry not enough resources")
            flag = 0
            break
    return flag

def take_money(Input):
    q = float(input('How many quaters: '))
    d = float(input('How many dimes: '))
    n = float(input('How many nickel: '))
    p = float(input('How many pennies: '))
    total_cash = round(0.25*q + 0.10*d + 0.05*n + 0.01*p, 2)
    cost = MENU[Input]['cost']
    if total_cash >= MENU[Input]['cost']:
        change_cash = total_cash - MENU[Input]['cost']
        change_cash = round(change_cash,2)
        print(f'Total money received ${total_cash}')
        print(f'Here is ${change_cash} dollars in change')
        bank["money"] += cost
        return 1
    else:
        print(f'cost of {Input} is ${cost} but money reseived {total_cash}\n please insert more money')
        return 0

def make_coffee(Input):
    st = check_resourses(Input)
    if st == 1:
        mc = take_money(Input)
    if st == 1 and mc == 1:
        for res in resources:
            resources[res] = resources[res] - MENU[Input]['ingredients'][res]
        print(f'Enjoy your {Input}')


state = True

while state:
    In_p = start_coffie_machine()
    if In_p == "off":
        state = False
        break
    if In_p == "report":
        print_report()
    else:
        make_coffee(In_p)


