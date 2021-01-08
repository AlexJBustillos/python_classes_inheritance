# Class

class Car():
    """ This is a car class that will display the make, model and color """
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.gas = 100

    def __str__(self):
        return "{}, {}, {}".format(self.make, self.model, self.color)

    def drive(self):
        self.gas -= 10
        

    def fill_tank(self):
        self.gas = 100 
        

    def check_gas(self):
        print(f"Gas handle: {self.gas}")

car1 = Car('Mercedes', 'G class', 'Matte Black')

car1.drive()
car1.drive()
car1.check_gas()
car1.fill_tank()
car1.check_gas()

class Anime():
    """ This is a anime class that will display the title, character, and power of an anime show and character """
    def __init__(self, title, character, power):
        self.title = title
        self.character = character
        self.power = power
        self.life = 100

    def __str__(self):
        return "{}, {}, {}".format(self.title, self.character, self.power)

    def damage(self):
        self.life -= 5

    def one(self):
        self.life = 100

    def two(self):
        print(f"Current health: {self.life}")
    
anime1 = Anime('HXH', 'Gon', 'Strength')

anime1.damage()
anime1.damage()
# anime1.one()
anime1.two()
# anime1.one()
