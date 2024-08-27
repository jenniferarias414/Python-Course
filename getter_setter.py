class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)
        # setter fxn allows us to do something before the value gets assigned

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"
    
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )
    
    def get_salary(self):
        # return f"${self.salary}"
        # return round(self.salary, 2)
        # logging.info("Someone accessed the salary attribute.")
        return self._salary 
    
    # @property
    # def salary(self):
    #     return self._salary

    # this is how the getter fxn would look using @property. properties are implemented with a class decorator that uses the descriptor protocol.
    
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary

        # validation logic is inside of the class so users are not able to directly alter salary without validating if above min wage first

employee1 = Employee("Bobby", 38, "developer", 1200)
employee2 = Employee("Jimmy", 44, "tester", 1000)

employee1.set_salary(999)
print(employee1.get_salary())

# self._salary ----- the _ makes it a private attribute, user can still directly access salary but the _ alerts them that it is non-public.   if you use (2) underscores  (ie. self.__salary) and the user tries to run it outside of the scope, they get an error. this is called "name mangling"

print(employee1.salary)
# when you try to retrieve the alue of the salary attribute, the property will call the special salary method and retrieve the non-public salary value



@property
def salary(self):
    return self._salary

employee1.salary 
#don't need to invoke the function, since this method is now a property

@salary.setter
def salary(self, salary):
    if salary < 1000:
        raise ValueError('Minimum wage is $1000')
    self._salary = salary

    # decorator is prepended with the @ and is placed above the function's definition
    # then you change the code in __init__ fxn back to self.salary = salary since you're not using custom setter anymore



@property
def annual_salary(self):
    return self.salary * 12

# computed property

@property
def annual_salary(self):
    if self._annual_salary is None:
        self._annual_salary = self.salary * 12
    return self._annual_salary

# in the __init__ function, add: self._annual_salary = None
# because we don't want to calculate the annual salary unless someone explicitly tries to access if from the specific employee instance. Calculation will only be done if the cached value inside the hidden attribute is None.