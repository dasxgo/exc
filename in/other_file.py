# other_file.py
from employee import Employee

def create_employee():
    print('Employee is starting their job...')
    employee1 = Employee(name='Blake', company='ILoveCode Inc.', age=30, is_on_vacation=True)
    employee1.working()
    
create_employee()