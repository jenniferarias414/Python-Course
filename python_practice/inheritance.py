# define parent class - all robots walk and say their name
class Robot:

    def __init__(self, name):
        self.name = name 
        self.position = [0,0]
        print("My name is", self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New position:", self.position)

    def eat(self):
        print("I'm hungry!")


# creating the child class
class Robot_Dog(Robot):

    def make_noise(self):
       print("Woof Woof!")

    def eat(self):
        super().eat() 
        # method overriding- i like bacon would print only UNLESS you add super() which will print the parent's eat function too
        print("I like bacon!")

# Main program

my_robot_dog = Robot_Dog('Buddy')
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()