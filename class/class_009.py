# class and its methods
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
 
    def sail(self):
        print("{} has sailed!".format(self.name))
        
 	def convert_cargo(self):
        return self.cargo * 1000
 
# function
def sail_function(name):
    print("{} has sailed!".format(name))

# creating an instance of the class Ship
# and calling the method sail
black_pearl = Ship("Black Pearl", 800)
black_pearl.sail()
# prints "Black Pearl has sailed!"
 
 
# calling the function sail_function
sail_function(black_pearl.name)
# also prints "Black Pearl has sailed!"

print(black_pearl.convert_cargo())  