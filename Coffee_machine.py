# coffee machine
from Coffee_factory import coffee_flavors
from os import system


machine_milk = 200
machine_water = 300
machine_coffee = 100
machine_coin = 0

OVER_IT = False
while not OVER_IT:
    system("cls")
    deal = input("Want to make a deal Yes or No : ").capitalize()
    if deal == "No":
        OVER_IT = True
    elif deal == "Yes":
        need = input("\nChoose your need\nNOTE: Type repo for machine report \n      Type coffee for more options : ").capitalize()
        if need == "Repo":
            system("cls")
            print(f"""\tMACHINE REPORT
                Water: {machine_water} ml
                Milk: {machine_milk} ml
                Coffee: {machine_coffee} ml
                Coin: ${machine_coin}""")
            system("pause")
            system("cls")
        elif need == "Coffee":
            system("cls")
            want_coffee = input("Choose your flavor espresso/latte/cappuccino\n\nCoffee:  ").capitalize()
            if (coffee_flavors[want_coffee]["water_used"] > machine_water) or (
                    coffee_flavors[want_coffee]["coffee_used"] > machine_coffee) or (
                    coffee_flavors[want_coffee]["milk_used"] > machine_milk):
                print(f"Sorry! We are out of resources to provide you {want_coffee}\nAmount refunded")
                continue
            you_pay_amount = float((int(input("Enter Quarters : ")) * 0.25))
            you_pay_amount = float(you_pay_amount + (int(input("Enter Dimes : ")) * 0.10))
            you_pay_amount = float(you_pay_amount + (int(input("Enter Nickles : ")) * 0.05))
            you_pay_amount = float(you_pay_amount + (int(input("Enter Pennys : ")) * 0.01))
            you_pay_amount=round(you_pay_amount,2)
            if you_pay_amount < coffee_flavors[want_coffee]["price"]:
                print(f"Not enough money to buy a {want_coffee}")
                system("pause")
                system("cls")
                continue
            print(f"{want_coffee} cost you ${you_pay_amount}\n\n")
            you_pay_amount = you_pay_amount - coffee_flavors[want_coffee]["price"]
            machine_coin += you_pay_amount
            machine_milk -= coffee_flavors[want_coffee]["milk_used"]
            machine_water -= coffee_flavors[want_coffee]["water_used"]
            machine_coffee -= coffee_flavors[want_coffee]["coffee_used"]
            
            print(f"Here is your pay back amount ${you_pay_amount}\n\n")
            print(f"Enjoy your {want_coffee} ☕")
            system("pause")
            system("cls")
        else:
            print("You made some typo TRY AGAIN!")
            system("pause")
            system("cls")
    else:
        print("Requested action not found")
        system("pause")
