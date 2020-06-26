class Vehicle:
    color="Red"#This is a class variable that should not be changed.This is a global class variable
    def __init__(self,body,make):
        self.body=body
        self.make=make
#we are going to show how to change this.
Vehicle.color="green"#The red changed to green.
my_vehicle=Vehicle("saturn","ion")
my_other_vehicle=Vehicle("Toyota","Corolla")
#We can create as many vehicles as we want based off of one class
print(my_vehicle.body,my_vehicle.make)
print(my_other_vehicle.body,my_other_vehicle.make)
print(my_other_vehicle.color,my_vehicle.color)