# Constructor - Parameterized

class Family:
    members=5
    def __init__(self, count):
        print('this is parametrized constructor')
        self.members = count
    def show(self):
        print("No. Of members is", self.members)
object = Family(10)
object.show()
print('='*64)

# Non - Parameterized constructor

class Fruits:
    favourite = 'Apple'

    def __init__(self):
        self.favourite = 'Orange'
    
    # a method

    def show(self):
        print(self.favourite)

obj = Fruits()

# calling the instance method using the object obj

obj.show()
print('='*64)


# Default Constructor

class Assignaments:
    check = 'not done'
    # a method
    def is_done(self):
        print(self.check)

# crating an object of the class
obj = Assignaments()

# Clalig tthe instance method using the objectt obj
obj.is_done()




