#an abstract class cannot be used to create an instance of an object.
#you can only use inheritance for an abstract class.

class animal:
    def __init__(self,name):
        self.animal_name=name
    def eat(self):
        raise NotImplementedError("Child class should be implementing this")
class monkey(animal):#The method need to be in the child class only
    pass

my_animal=animal("sdb")
my_animal.eat()
