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
    maintenance = True
    while maintenance:
        clear()
        print(logo)
        print("= Resource Management =\n")
        for resource in content_dict:

            if resource == "coffee":
                print("{}: {}g\n".format(resource,content_dict[resource]))
            else:    
                print("{}: {}ml\n".format(resource,content_dict[resource]))
        if input("Want to refill a resource? (y/N) >>").lower() == "y":
            content_dict = refill(content_dict)
        else:
            maintenance = False
            return content_dict

def refill(content_dict):
    """Tailor made function for coffee machine. The user tipps in the resource they want to refill. If the resource is at max, or it does not exist, it returns without changing anything"""

    need = input("What do you want to refill? >>> ").lower()    
    for resource in content_dict:
        if need not in content_dict:
            print("Error: No such material to refill, please make a valid choice!")
            sleep(3)
            return content_dict
        else:
            if need == "water" and content_dict[need] < 300:
                content_dict[need] = 300
                print("Watertank has been refilled to 300ml")
       
            elif need == "milk" and content_dict[need] < 200:
                content_dict[need] = 200
                print("Milk has been refilled to 200ml")       
            elif need == "coffee" and content_dict[need] < 100:
                content_dict[need] = 100
                print("Coffee has been refilled to 100g")
            else:
                print("Already filled 100%")
            
            sleep(2) 
            return content_dict

def resource_check(materials, menu_dict):
    """Compares the materials in the machine with the menue plan. If there is at least one drink with more resource needs than available it puts out a warning"""
    for drink in menu_dict:
        coffee_ingridient = menu_dict[drink]["ingredients"]
        for ingridient in coffee_ingridient:
            for stock in materials:
                if stock == ingridient and materials[stock] < coffee_ingridient[ingridient]:
                    print("Warning: Low "+ ingridient +" !")
                    return

            

def coffee_menu(menu_dict):
    clear()
    print(logo)
    print("Coffee Menu - Please make your choice!\n")
    counter = 0
    for coffee in menu_dict:
        counter += 1
        for cost in menu_dict[coffee]:
            if cost == "cost":
                print(f"{counter}. {coffee} - EUR {menu_dict[coffee][cost]}\n")

# Programm Start from here
funds = 0.0

selection = True
while selection:
    coffee_menu(MENU)
    resource_check(resources,MENU)

    select = input("Please select Coffee Number: ")
    if select == "0":
        report_menu(resources)
