class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

# class Tester(Employee):
#     pass

# #The tester class inherits all properties from Employee class, so 'pass' still allows name/age/salary properties and to apply increase_salary function

class Tester(Employee):
    def run_tests(self):
        print(f"Testing is started by {self.name}...")
        print("tests are complete.")

# tester subclass has its own method run_tests but also has access to all of the methods from the Employee class

class Developer(Employee):
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus 

# 'method overriding' = redifining the same method from the parent class inside of the child class

# so you don't have to write the same code twice in superclass fxn and subclass fxn...you can use super fxn

class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus
        

employee1 = Tester("Jenny", 41, 5000)
employee2 = Developer("Wendy", 20, 1000, "React")

employee1.increase_salary(20)
employee2.increase_salary(20, 30)

print(employee1.salary)
print(employee2.salary)
employee1.run_tests()

print(employee2.name)
print(employee2.framework)


# polymorphism ex:
print(isinstance(employee1, Tester))
print(isinstance(employee1, Employee))

print(issubclass(Developer, Employee))
print(issubclass(Employee, object))
print(issubclass(Developer, object))

