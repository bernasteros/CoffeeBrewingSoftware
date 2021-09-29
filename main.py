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

def refill(content_dict):
    def water():
        water = content_dict["water"]
        if water < 300:
            water = 300
            print("Watertank has been refilled to 300ml")
        else:
            print("Watertank already filled")
        return water        

    def milk():
        milk = content_dict["milk"]
        if milk < 200:
            milk = 200
            print("Milk has been refilled to 200ml")
        else:
            print("Already filled 100%")        
        return milk

    def coffee():
        coffee = content_dict["coffee"]
        if coffee < 100:
            coffee = 100
            print("Coffee has been refilled to 100g")
        else:
            print("Already filled 100%")
        return coffee

funds = 0.0

refill(resources)
