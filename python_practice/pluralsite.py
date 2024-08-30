# class AriasFamily:
#     def __init__(self):
#         # self.__dict__["name"] = "Jenny"
#         # self.__dict__["age"] = 41
#         # self.__dict__["role"] = "mom"
#         # self.__dict__["salary"] = 150000

#         self.name = "Jenny"
#         self.age = 41
#         self.role = "mom"
#         self.salary = 150000

# f = AriasFamily()
# print(f.__dict__)

# print(f.name)

# using __dict__ is usually used for debugging purposes or when you want to inspect the dictionary directly


# the above example is hard-coded...
# the __init__ function is responsible for initializing attributes of each new employee object

class AriasFamily:
    def __init__(self, name, age, role, salary):
        # define the function that will initialize attributes
        # name the parameters after the attributes
        self.name = name
        self.age = age
        self.role = role 
        self.salary = salary 

    def increase_salary(member, percent):
        member['salary'] += member['salary'] * (percent/100)

    def member_info(member):
        print(f"{member['name']} is {member['age']} years old. Member is a {member['role']} with the salary of ${member['salary']}")

role1 = AriasFamily("Jenny", 41, "mom", 150000)
role2 = AriasFamily("India", 11, "daughter", 10)
role3 = AriasFamily("Corbin", 9, "son", 5)

# role1/2/3 are new AriasFamily class instances

# print(role1.name)
# print(role2.name)

AriasFamily.increase_salary(role2, 55)
AriasFamily.member_info(role3)

# e189958@Mac-P27PG7L4 Python Course % /usr/local/bin/python3 "/Users/e189958/Desktop/Python Course/pluralsite.py"
# Traceback (most recent call last):
#   File "/Users/e189958/Desktop/Python Course/pluralsite.py", line 48, in <module>
#     AriasFamily.increase_salary(role2, 55)
#   File "/Users/e189958/Desktop/Python Course/pluralsite.py", line 34, in increase_salary
#     member['salary'] += member['salary'] * (percent/100)
#     ~~~~~~^^^^^^^^^^
# TypeError: 'AriasFamily' object is not subscriptable

#            error occurs when running this way because OBJECTS are NOT DICTIONARIES   


class AriasFamily:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role 
        self.salary = salary 

    def increase_salary(member, percent):
        member.salary += member.salary * (percent/100)

    def member_info(member):
        print(f"{member.name} is {member.age} years old. Member is a {member.role} with the salary of ${member.salary}")

        # 'instance functions aka methods'

role1 = AriasFamily("Jenny", 41, "mom", 150000)
role2 = AriasFamily("India", 11, "daughter", 10)
role3 = AriasFamily("Corbin", 9, "son", 5)

AriasFamily.increase_salary(role2, 55)
AriasFamily.member_info(role3)

# can also write
role2.increase_salary(55)
role3.member_info()

# you can indirectly call the function from any instance of that class. instances (ie role2) have access to the functions defined in the class that was used to instantiate them

# code still runs if you don't make first parameter 'self' but by following common practices, we make our code maintainable and easier to read

class AriasFamily:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role 
        self.salary = salary 

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def member_info(self):
        print(f"{self.name} is {self.age} years old. Member is a {self.role} with the salary of ${self.salary}")

role1 = AriasFamily("Jenny", 41, "mom", 150000)
role2 = AriasFamily("India", 11, "daughter", 10)
role3 = AriasFamily("Corbin", 9, "son", 5)

role2.increase_salary(55)
role3.member_info() 
# the instance itself (role1) is always implicitly the first parameter