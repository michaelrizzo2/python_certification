class Vehicle:
    def __init__(self,body,make):
        self.body=body
        self.make=make

my_vehicle=Vehicle("saturn","ion")
my_other_vehicle=Vehicle("Toyota","Corolla")
#We can create as many vehicles as we want based off of one class
print(my_vehicle.body,my_vehicle.make)
print(my_other_vehicle.body,my_other_vehicle.make)