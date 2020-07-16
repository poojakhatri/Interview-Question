class Person:
    def __init__(self, name):
        self.name = name

	def greet(self):
    	return (f'Hello, I am {self.name}!')

obj = Person.greet(input())
