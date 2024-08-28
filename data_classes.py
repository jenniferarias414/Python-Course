from dataclasses import dataclass

# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name 
#         self.payment = payment
#         self.client = client

#     def __repr__(self):
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"

@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

    # decorate the Project class with the dataclass decorator to turn it into a data class. then all you need to do is define which attributes will be preesent in each instance of this class....creates __init__ fxn in the background and provides wrapper method

    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}...")
    
class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

p = Project("Flask app", 75000, "Southwest Airlines")
# the project instance is an attribute of the Employee instance aka "composition", often used instead of inheritance
e = Employee("Timmy", 15, 1000, p)
print(e.project)

# when you run this print statement, you get the formatted response from the wrapper fxn

# --------------------------------------------------------------------------------

# from typing import Any

# @dataclass
# class Project:
#     name: Any 
#     payment: Any 
#     client: Any 