class Dog:
    def __init__(self, name, race, color):
        self.name = name
        self.race = race
        self.color = color 
    # Method info
    def info(self):
        print(f'Name: {self.name}')
        print(f'Race: {self.race}')
        print(f'Color: {self.color}')

dog1 = Dog('Bella', 'Pomerania', 'Beige')
print(dog1.info())
