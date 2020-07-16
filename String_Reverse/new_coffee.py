water = 400
milk = 540
beans = 120
cups = 9 
money = 550

print("The coffee machine has:")
print("%d of water" % water)
print("%d of milk" % milk)
print("%d of coffee beans" % beans)
print("%d of disposable cups" % cups)
print("%d of money" % money)

print("Write action(buy, fill, take):")
action = input()

if action== "buy":
	print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino :")
	op_ = int(input())
	if op_ == 3:
		water = water - 200
		milk = milk - 100
		beans = beans - 12
		cups = cups -1
		money = money + 6
		print("The coffee machine has:")
		print("%d of water" % water)
		print("%d of milk" % milk)
		print("%d of coffee beans" % beans)
		print("%d of disposable cups" % cups)
		print("%d of money" % money)
	if op_ == 2:
		water = water - 350
		milk = milk - 75
		beans = beans - 20
		cups = cups -1
		money = money + 7
		print("The coffee machine has:")
		print("%d of water" % water)
		print("%d of milk" % milk)
		print("%d of coffee beans" % beans)
		print("%d of disposable cups" % cups)
		print("%d of money" % money)
	if op_ == 1:
		water = water - 250
		beans = beans - 16
		cups = cups -1
		money = money + 4
		print("The coffee machine has:")
		print("%d of water" % water)
		print("%d of milk" % milk)
		print("%d of coffee beans" % beans)
		print("%d of disposable cups" % cups)
		print("%d of money" % money)

if action == "fill":
	c_water = int(input("Write how many ml of water do you want to add:"))
	c_milk = int(input("Write how many ml of milk do you want to add:"))
	c_beans = int(input("Write how many grams of coffee beans do you want to add:"))
	c_cups = int(input("Write how many disposable cups of coffee do you want to add:"))

	n_water = water + c_water
	n_milk = milk + c_milk
	n_beans = beans + c_beans
	n_cups = cups + c_cups

	print("The coffee machine has:")
	print("%d of water" % n_water)
	print("%d of milk" % n_milk)
	print("%d of coffee beans" % n_beans)
	print("%d of disposable cups" % n_cups)
	print("%d of money" % money)

if action == "take":
	print("I gave you %d" % money)
	money = money - 550
	print("The coffee machine has:")
	print("%d of water" % water)
	print("%d of milk" % milk)
	print("%d of coffee beans" % beans)
	print("%d of disposable cups" % cups)
	print("%d of money" % money)
