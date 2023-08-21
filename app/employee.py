class Employee:
    def __init__(self, id_employee, name_employee,
                 salary_employee, dept_employee):
        self.id_employee = id_employee
        self.name_employee = name_employee
        self.salary_employee = salary_employee
        self.dept_employee = dept_employee
    
    def calculate_employee_salary(self, hours_working):
        if hours_working > 40:
            extra_hour = hours_working - 40
            pay_extra_hour = extra_hour * (self.salary_employee / 40)
            self.salary_employee += pay_extra_hour
        return self.salary_employee
    
    def assign_dept(self, dept):
        self.dept_employee = dept

    def print_employee_details(self):
        print(f'ID Employee: {self.id_employee}')
        print(f'Name Employee: {self.name_employee}')
        print(f'Salary Employee: {self.salary_employee}')
        print(f'Dept Employee: {self.dept_employee}')

emp1 = Employee('E7875', 'ADAMS', 50000, 'ACCOUNTING')
emp1.print_employee_details()
emp1.assign_dept('SALES')

print('='*62)

emp1.print_employee_details()






        