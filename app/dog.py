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

my_dog = Dog('Bella', 'Pomerania', 'Beige')
print(my_dog.info())
