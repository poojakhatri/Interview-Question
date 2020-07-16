class River:
    all_rivers = []
 
    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)
 
    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))