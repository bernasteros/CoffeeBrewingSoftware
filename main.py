from menu import MENU, resources
from art import logo
from os import system, name
from time import sleep


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def report_menu(content_dict):
    """Displays the resources of the machine"""

    while True:
        clear()
        print(logo)
        print("= Resource Management =\n")
        for resource in content_dict:
            sleep(0.1)
            if resource == "coffee":
                print("{}: {}g\n".format(resource, content_dict[resource]))
            else:
                print("{}: {}ml\n".format(resource, content_dict[resource]))
        if input("Want to refill a resource? (y/N) >>").lower() == "y":
            content_dict = refill(content_dict)
        else:
            return content_dict


def refill(content_dict):
    """Tailor made function for coffee machine.
    The user tips in the resource they want to refill.
    If the resource is at max, or it does not exist, it returns without changing anything"""

    need = input("What do you want to refill? >>> ").lower()
    for resource in content_dict:
        if need not in content_dict:
            print("Error: No such material to refill, please make a valid choice!")
            sleep(3)
            return content_dict
        else:
            if need == "water" and content_dict[resource] < 300:
                content_dict[resource] = 300
                print("Watertank has been refilled to 300ml")

            elif need == "milk" and content_dict[resource] < 200:
                content_dict[resource] = 200
                print("Milk has been refilled to 200ml")
            elif need == "coffee" and content_dict[resource] < 100:
                content_dict[resource] = 100
                print("Coffee has been refilled to 100g")
            else:
                print("Already filled 100%")
            sleep(2)
            return content_dict


def resource_check(materials, menu_dict):
    """Compares the materials in the machine with the menu plan.
    If there is at least one drink with more resource needs than available it puts out a warning"""
    for drink in menu_dict:
        coffee_ingredient = menu_dict[drink]["ingredients"]
        for ingredient in coffee_ingredient:
            for stock in materials:
                if stock == ingredient and materials[stock] < coffee_ingredient[ingredient]:
                    print("Warning: Low " + ingredient + " !")
                    return


def coffee_menu(menu_dict):
    clear()
    print(logo)
    print("Coffee Menu - Please make your choice!\n")
    counter = 0
    for coffee in menu_dict:
        sleep(0.1)
        counter += 1
        for cost in menu_dict[coffee]:
            if cost == "cost":
                print(f"{counter}. {coffee} - EUR {menu_dict[coffee][cost]}\n")


def move_money(credit):
    transaction = True

    while transaction:
        clear()
        print(logo)
        print("Credit Menu\n")

        if credit == 0.0:
            direction = "i"
        else:
            direction = input("(i)nsert or (w)hitdraw Credits? > ").lower()

        if direction == "i":
            print("Please insert Coins:")
            coins = {
                "tens": 0.10,
                "twenties": 0.20,
                "fifties": 0.50,
            }

            for cents in coins:
                try:
                    insert = float(input("How much " + cents + " ?\n>> "))
                    insert *= coins[cents]
                    credit += insert
                except ValueError:
                    print("Sorry, invalid input, continuing...")
                    sleep(1)
            return credit
        elif direction == "w":
            credit = 0.0
            print("Returning money...")
            sleep(1)
            return credit
        else:
            print("Unknown input...")


def show_funds(credit):
    sleep(0.1)
    print("|| Current Credits available: EUR " + str(credit) + "\n")


def make_coffee(credit, resource, menu_dict, coffee_name):
    """Main function that produces the coffee of choice, given that money and resources are sufficient"""
    coffee_cost = menu_dict[coffee_name]["cost"]
    # TODO Implement Resource Check and money withdrawal


# Program Start from here
money = 0.0

selection = True
while selection:
    coffee_menu(MENU)
    resource_check(resources, MENU)
    show_funds(money)
    # TODO Fill in the cases
    # TODO Implement a "off" function
    # TODO Reformat Text in Option Display
    select = input("Please select Coffee Number\n or 'm' for credit menu: ")
    if select == "0":
        report_menu(resources)
    elif select == "1":
        pass
    elif select == "2":
        pass
    elif select == "3":
        pass
    elif select == "m":
        money = move_money(money)
    else:
        if money != 0.0:
            print("\nReturning money...")
            money = 0.0
            sleep(1)
        print("\nShutting down machine...")
        sleep(1)
        print("Thank you for dropping by :)")
        selection = False
