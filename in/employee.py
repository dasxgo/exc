# employee.py
class Employee:
    def __init__(self, name, company, age, is_on_vacation):
        self.name = name
        self.company = company
        self.age = age
        self.is_on_vacation = is_on_vacation

    def working(self):
        print(f"{self.name} is working")

