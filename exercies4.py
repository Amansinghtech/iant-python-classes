# polymorphism
# duck typing
# if it looks like a duck, swims like a duck and quacks like a duck, then its is probably a duck.

# method overloading
# method overloading is used perform diffrent types of tasks depending upon the inputs or paramerter that are passed

# method overriding
# it takes over the predefine method of the parent class and creates a new definition of it

# operator overloading
# with the help of operator overloading we can redifine the functionality of an operator like +, -, *, /, etc.

class Duck:
    def quack(self):
        print("hi i am duck and i do quack")


class Cow:
    def quack(self):
        print("hi i am cow and i do moooooo..")


class Zoo:
    def __init__(self, bird) -> None:
        bird.quack()


duck1 = Cow()  # Duck()

animal = Zoo(duck1)
