latte_price=1.50
espresso_price=2.50
capuccino_price=3.00
penny=0.01
dime=0.10
nickel=0.05
quarter=0.2
water=300
milk=200
coffee=100
money=0
dict={"a":"espresso","b":"latte","c":"cappuccino","d":"nothing"}

def coffee_details():
    dict={"Espresso":{"Water":"50ml","Coffee":"18g"},"Latte":{"Water":"200ml","Coffee":"24g","Milk":"150ml"},"Capuccino":{"Water":"250ml","Coffee":"24g","Milk":"100ml"}}
    for i in dict:
        print(f"The ingredients required for {i} are {dict[i]}")

def coin_details():
    coin={"Penny":"1cent $0.01","Dime":"10cents $0.10","Nickel":"5cents $0.05", "Quarter":"25cents $0.25"}
    for i in coin:
        print(f"The value of {i} is {coin[i]}")
def coffee_prices():
    print(f"The price of the latte is ${latte_price}")
    print(f"The price of the espresso is ${espresso_price}")
    print(f"The price of the capuccino is ${capuccino_price}")
def report(water,coffee,milk,money):
    print(f"Current available resource are:\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
def espresso(water,coffee,milk,money):
    if water<50 or coffee<18:
        print(f"Sorry inadequate resources, available resources are: water-{water}ml,coffee-{coffee}g,milk-{milk}ml,money-${money} but espresso requires Water:50ml,Coffee:18g" )
        user_second_choice = input("Do you wanna see the available resources now?Yes or No:")
        if user_second_choice == "yes":
            report(water, coffee, milk, money)
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
        else:
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
    else:
        print("please insert the coin.")
        nickles_count = int(input("How many Nickles:"))
        dimes_count = int(input("How many Dimes:"))
        pennies_count = int(input("How many Pennies:"))
        quarter_count = int(input("How many Quarter:"))
        total_price = (nickles_count*nickel + dimes_count*dime + pennies_count*penny + quarter_count*quarter)
        total_price = round(total_price, 2)
        if total_price > espresso_price:
            refund = total_price - espresso_price
            refund = round(refund, 2)
            print(f"The total amount you have given is ${total_price} but the price of the espresso is ${espresso_price}")
            print(f"Here is your refund ${refund}")
            print("Enjoy your espresso☕")
        elif total_price < espresso_price:
            print(f"Sorry! you have given less amount which is ${total_price} but the price of espresso is ${espresso_price}")
        elif total_price == espresso_price:
            print("Enjoy your espresso☕")
        water=water-50
        coffee=coffee-18
        milk=milk
        money=espresso_price+money
        user_second_choice = input("Do you wanna see the available resources now?Yes or No:")
        if user_second_choice == "yes":
            report(water, coffee, milk, money)
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
        else:
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
def latte(water,coffee,milk,money):
    if water<200 or coffee<24 or milk<150:
        print(f"Sorry inadequate resources, available resources are: water-{water}ml,coffee-{coffee}g,milk-{milk}ml,money-${money} but latte requires Water:200ml,Coffee:24g,Milk:150ml" )
        user_second_choice = input("Do you wanna see the available resources now?Yes or No:")
        if user_second_choice == "yes":
            report(water, coffee, milk, money)
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
        else:
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
    else:
        print("please insert the coin.")
        nickles_count = int(input("How many Nickles:"))
        dimes_count = int(input("How many Dimes:"))
        pennies_count = int(input("How many Pennies:"))
        quarter_count = int(input("How many Quarter:"))
        total_price = (nickles_count*nickel + dimes_count*dime + pennies_count*penny + quarter_count*quarter)
        total_price=round(total_price,2)
        if total_price > latte_price:
            refund = total_price - latte_price
            refund = round(refund, 2)
            print(
                f"The total amount you have given is ${total_price} but the price of the latte is ${latte_price}")
            print(f"Here is your refund ${refund}")
            print("Enjoy your latte☕")
        elif total_price < latte_price:
            print(f"Sorry! you have given less amount which is ${total_price} but the price of latte is ${latte_price}")
        elif total_price == latte_price:
            print("Enjoy your latte☕")
        water = water - 200
        coffee = coffee - 24
        milk = milk - 150
        money =latte_price+money
        user_second_choice = input("Do you wanna see the available resources now?Yes or No:")
        if user_second_choice == "yes":
            report(water, coffee, milk, money)
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
        else:
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
                exit()
def cappuccino(water,coffee,milk,money):
    if water<250 or coffee<24 or milk<100:
        print(f"Sorry inadequate resources, available resources are: water-{water}ml,coffee-{coffee}g,milk-{milk}ml,money-${money} but cappuccino requires Water:250ml,Coffee:24g,Milk:100ml" )
        user_second_choice = input("Do you wanna see the available resources now?Yes or No:")
        if user_second_choice == "yes":
            report(water, coffee, milk, money)
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
        else:
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
    else:
        print("please insert the coin.")
        nickles_count = int(input("How many Nickles:"))
        dimes_count = int(input("How many Dimes:"))
        pennies_count = int(input("How many Pennies:"))
        quarter_count = int(input("How many Quarter:"))
        total_price = (nickles_count*nickel + dimes_count*dime + pennies_count*penny + quarter_count*quarter)
        total_price = round(total_price, 2)
        if total_price > latte_price:
            refund = total_price - capuccino_price
            refund=round(refund,2)
            print(
                f"The total amount you have given is ${total_price} but the price of the capuccino is ${capuccino_price}")
            print(f"Here is your refund ${refund}")
            print("Enjoy your cappuccino☕")
        elif total_price < capuccino_price:
            print(f"Sorry! you have given less amount which is ${total_price} but the price of capuccino is ${capuccino_price}")
        elif total_price == capuccino_price:
            print("Enjoy your cappuccino☕")
        water = water - 250
        coffee = coffee - 24
        milk = milk - 100
        money =capuccino_price+money
        user_second_choice = input("Do you wanna see the available resources now?Yes or No:")
        if user_second_choice == "yes":
            report(water, coffee, milk, money)
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
        else:
            user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
            user_choice.lower()
            if dict[user_choice] == "espresso":
                espresso(water, coffee, milk, money)
            elif dict[user_choice] == "latte":
                latte(water, coffee, milk, money)
            elif dict[user_choice] == "cappuccino":
                cappuccino(water, coffee, milk, money)
            elif dict[user_choice] == "nothing":
                exit()
report(water,coffee,milk,money)
print("\n")
coin_details()
print("\n")
coffee_prices()
print("\n")
user_choice = input("What would you like?\na:espresso\nb:latte\nc:cappuccino\nd:nothing\ninput:-")
user_choice.lower()
if dict[user_choice]=="espresso":
   espresso(water,coffee,milk,money)
elif dict[user_choice]=="latte":
    latte(water,coffee,milk,money)
elif dict[user_choice]=="cappuccino":
    cappuccino(water,coffee,milk,money)
elif dict[user_choice] == "nothing":
    exit()



