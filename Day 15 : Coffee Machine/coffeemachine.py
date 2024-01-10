cup = """                                                                            
                            ██        ██▓▓                                  
      ██      ██            ██          ██                                  
      ██      ██            ████        ██                                  
      ██      ██              ████      ████                                
      ████    ████              ██        ██                                
        ████    ████            ██        ██                                
          ██      ██                                                        
          ██      ██                                                        
                                    ▒▒                                      
                                    ██                                      
                                                                            
    ██████████████████████████████████████████████      ████████████        
  ██████████████████████████████████████████████████  ████████████████      
  ██████████████████████████████████████████████████████████████████████    
  ██████████████████████████████████████████████████████████    ██████████  
  ████████████████████████████████████████████████████████        ████████  
  ██████████████████████████████████████████████████████            ██████▒▒
  ████████████████████████████████████████████████████                ██████
  ██████████████████████████████████████████████████                  ██████
  ██████████████████████████████████████████████████                  ██████
  ██████████████████████████████████████████████████                  ██████
  ██████████████████████████████████████████████████                  ██████
  ██████████████████████████████████████████████████                  ██████
  ████████████████████████████████████████████████████              ██████▒▒
  ██████████████████████████████████████████████████████▒▒      ▒▒████████  
  ████████████████████████████████████████████████████████▒▒▒▒██████████    
  ██████████████████████████████████████████████████▒▒██████████████████    
    ██████████████████████████████████████████████    ░░░░██████████        
      ██████████████████████████████████████████                            
      ▒▒████████████████████████████████████████                            
"""


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

def enter_coins():
    print("Please insert coins.")
    quarter = int(input("How many quarters? : "))
    dime = int(input("How many dimes? : "))
    nickel = int(input("How many nickels? : "))
    penny = int(input("How many pennies? : "))
    total = (quarter*25) + (dime*10) + (nickel*5) + (penny)
    return total

change = 0
money = 0

resources_finished = False

print(cup)

while not resources_finished:
    choice = input("What would you like? (Espresso/Latte/Cappuccino) : ").lower()

    if choice == "report":
        print(f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : ${money}")

    elif choice == "latte":
        total = enter_coins()
        if total >= MENU['latte']['cost']:
            change = total - MENU['latte']['cost']
            print(f"Here's ${change} in change.")
            print("Here's your latte! Enjoy")
        else:
            print("Insufficient Amount! Money refunded.")
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        money += change

    elif choice == "espresso":
        total = enter_coins()
        if total >= MENU['espresso']['cost']:
            change = total - MENU['espresso']['cost']
            print(f"Here's ${change} in change.")
            print("Here's your espresso! Enjoy")
        else:
            print("Insufficient Amount! Money refunded.")
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        money += change

    elif choice == "cappuccino":
        total = enter_coins()
        if total >= MENU['cappuccino']['cost']:
            change = total - MENU['cappuccino']['cost']
            print(f"Here's ${change} in change.")
            print("Here's your cappuccino! Enjoy")
        else:
            print("Insufficient Amount! Money refunded.")
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        money += change

    else:
        print("Enter a valid choice!")

    if resources['water'] < 0 or resources['coffee'] < 0 or resources['milk'] < 0:
        print(resources)
        print("Out of Resources!")
        resources_finished = True
