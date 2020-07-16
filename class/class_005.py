class Planet:
    all_moons = []
 
    def __init__(self, name):
        self.name = name
        self.moons = []
 
 
earth = Planet("Earth")
jupiter = Planet("Jupiter")
 
earth.moons.append("Moon")
earth.all_moons.append("Moon")
 
jupiter.moons.append("Io")
jupiter.moons.append("Europa")
jupiter.all_moons.append("Io")
print(jupiter.moons)