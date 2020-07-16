
water = 400
milk = 540
beans = 120
cups = 9
money = 550

choice = "FALSE"
# print("The coffee machine has:")
# print("%d of water" % water)
# print("%d of milk" % milk)
# print("%d of coffee beans" % beans)
# print("%d of disposable cups" % cups)
# print("%d of money" % money)
while choice != "TRUE":

    print("Write action(buy, fill, take, remaining, exit):")
    action = input()
    
    if action == "remaining":
        remain()

    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino :")
        op_ = int(input())
        if op_ == 3:
            water = water - 200
            milk = milk - 100
            beans = beans - 12
            cups = cups - 1
            money = money + 6
            min_ = min(water, milk, beans, cups, money)
            if min_ >= 0:
                print("I have enough resources, making you a coffee!")
            else: 
                if water < 200:
                    print("Sorry, not enough water!")
                elif milk < 100:
                    print("Sorry, not enough milk!")
                elif beans <12:
                    print("Sorry, not enough beans!")
                elif cups <1:
                    print("Sorry, not enough cups!")
        if op_ == 2:
            water = water - 350
            milk = milk - 75
            beans = beans - 20
            cups = cups - 1
            money = money + 7
            min_ = min(water, milk, beans, cups, money)
            if min_ >= 0:
                print("I have enough resources, making you a coffee!")
            else: 
                if water < 350:
                    print("Sorry, not enough water!")
                elif milk < 75:
                    print("Sorry, not enough milk!")
                elif beans <20:
                    print("Sorry, not enough cups!")
                elif cups <1:
                    print("Sorry, not enough cups!")
          
        if op_ == 1:
            water = water - 250
            beans = beans - 16
            cups = cups - 1
            money = money + 4
            min_ = min(water, milk, beans, cups, money)
            if min_ >= 0:
                print("I have enough resources, making you a coffee!")
            else: 
                if water < 250:
                    print("Sorry, not enough water!")
                elif beans <16:
                    print("Sorry, not enough cups!")
                elif cups <1:
                    print("Sorry, not enough cups!")
         

    if action == "fill":
        c_water = int(input("Write how many ml of water do you want to add:"))
        c_milk = int(input("Write how many ml of milk do you want to add:"))
        c_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        c_cups = int(input("Write how many disposable cups of coffee do you want to add:"))

        water = water + c_water
        milk = milk + c_milk
        beans = beans + c_beans
        cups = cups + c_cups


    if action == "take":
        print("I gave you %d" % money)
        money = money - 550
      

    if action == "exit":
        quit()

def remain():
    global water
    global milk
    global beans
    global cups
    global money
    print("The coffee machine has:")
    print("%d of water" % water)
    print("%d of milk" % milk)
    print("%d of coffee beans" % beans)
    print("%d of disposable cups" % cups)
    print("%d of money" % money)