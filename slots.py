class Developer:
    __slots__ = ("name", "age", "salary", "framework")

    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework

employee1 = Developer("India", 12, 1000, "Python")

print(employee1.__slots__)

# provide instance with faster attribute access, save space in memory because each instance doesn't have to store its own dictionary BUT you can't add attributes dynamically anymore