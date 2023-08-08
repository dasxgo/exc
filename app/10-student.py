class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course = {}
    
    def add_course(self, course, qualification):
        self.course[course] = qualification
    
    def view_course(self):
        return self.course
    
john = Student('John', 20)
john.add_course('Math', 5.5)
john.add_course('History', 6.4)
print(john.view_course())



