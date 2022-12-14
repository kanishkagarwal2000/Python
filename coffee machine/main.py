from data import MENU, resources
def coin_calc():
    """gives total value of coins inserted by user"""
    print("Insert coins:")
    quarters = float(input("How many quarters?:").lower())                            # 0.25
    dimes = float(input("How many dimes?:").lower())                                  # 0.10
    nickels = float(input("How many nickels?:").lower())                              # 0.05
    pennies = float(input("How many pennies?:").lower())                              # 0.01         
    return quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

def resource_sufficient(o_ingredients):
    """Checks whether resources are sufficient or not to complete the order"""
    for item in o_ingredients:
        if o_ingredients[item] > resources[item]:
            print(f"Sorry!! There is not enough {item}")
            return False
    return True


def transaction_successful(payed, d_cost):
    if payed > d_cost:
        change = round(payed - d_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += d_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order, d_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in d_ingredients:
        resources[item] -= d_ingredients[item]
    print(f"Here is your {order} ☕️. Enjoy!")


def coffee():
    isOn = True
    while isOn:
        order = input("What would you like? (espresso/latte/cappuccino):").lower() 
        if order == "off":
            isOn = False
        elif order == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[order]
            if resource_sufficient(drink['ingredients']):
                total_money = coin_calc()
                if transaction_successful(total_money, drink['cost']):
                    make_coffee(order, drink['ingredients'])

# start here  
profit = 0      
coffee()

