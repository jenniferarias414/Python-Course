from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

def main():
    my_company = Company()

    employee1 = Employee("Jenny", 'Arias', 90000)
    my_company.add_employee(employee1)
    employee2 = Employee("Cuppers", 'Arias', 10000)
    my_company.add_employee(employee2)
    employee3 = Employee("India", 'Arias', 75000)
    my_company.add_employee(employee3)

    print(my_company.employees)    

main()