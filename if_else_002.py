# Write your code here
water = int(input("how many ml of water the coffee machine has:"))
milk = int(input("how many ml of milk the coffee machine has:"))
beans = int(input("how many grams of beans the coffee machine has:"))
cups = int(input("how many cups of coffee you will need : "))
water_ = 200
milk_ = 50
beans_ = 15

if cups == 0:
    print("Yes, I can make that amount of coffee")

if water == 0 and milk == 0 and beans == 0 and cups != 0:
    print("No, I can make only 0 cups of coffee")

c_water =  water// water_
c_milk =  milk // milk_
c_beans = beans // beans_
c_coffee = min(c_water, c_milk, c_beans)

if c_coffee == 1:
    print("Yes, I can make that amount of coffee")

if c_coffee > 1:
    if cups > c_coffee:
        print("No, I can make only %d cups of coffee" %c_coffee )
    else:
        c_cup = c_coffee - cups
        print("Yes, I can make that amount of coffee (and even %d more than that)" %c_cup)