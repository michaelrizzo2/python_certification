# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
class animal:

    def __init__(self):
        print("animal Constructed")
    
    def move(self):
        print("animal moving")
    
    def eat(self):
        print("animal eating")

class dog(animal):
    def __init__(self,dog_name,dog_age):
        animal.__init__(self)
        self.dog_name=dog_name
        self.dog_age=dog_age
    def move(self):
        print("dog running")

class bird(animal):
    def __init__(self,bird_name,bird_age):
        animal.__init__(self)
        self.bird_name=bird_name
        self.bird_age=bird_age
    def move(self):
        print("Bird Flying")

class fish(animal):
    def __init__(self,fish_age,fish_name):
        animal.__init__(self)
    def move(self):
        print("Fish Swimming")

mydog = dog(3, "wolfy")
mydog.move()
mydog.eat()

myfish = fish(1, "nemo")
myfish.move()
myfish.eat()

mybird = bird(3, "jojo")
mybird.move()
mybird.eat()

