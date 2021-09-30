from menu import MENU, resources

def report_menu(content_dict, money):
    """Displays the resources of the machine"""
    print("= Resources available =")
    for resource in content_dict:
        if resource == "coffee":
            print("{}: {}g".format(resource,content_dict[resource]))
        else:    
            print("{}: {}ml".format(resource,content_dict[resource]))
    print("money: €{}".format(money))

def refill(material):
    """Refills """      
    selection = input("What do you want to refill? >>> ").lower()    
    
    if selection == "water":
      if material < 300:
        material = 300
        print("Watertank has been refilled to 300ml")
      else:
          print("Watertank already filled")         
    elif selection == "milk":
        if material < 200:
            material = 200
            print("Milk has been refilled to 200ml")
        else:
            print("Already filled 100%")        
        return material

    elif selection == "coffee":
        if material < 100:
            material = 100
            print("Coffee has been refilled to 100g")
        else:
            print("Already filled 100%")
    else:
        print("Error: No such material to refill")    
    return material

# Programm Start from here
funds = 0.0

refill(resources)
