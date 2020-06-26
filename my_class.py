class Vehicle:
    #color="Red"#This is a class variable that should not be changed.This is a global class variable
    vehicle_counter=0
    def __init__(self,body,make,color,engine):
        self.body=body
        self.make=make
        self.color=color
        self.engine=engine
        Vehicle.vehicle_counter+=1
    def get_vehicle(self):
        print(Vehicle.vehicle_counter)
    def get_make(self):
        print(self.make)
    def get_color(self):
        print(self.color)
#we are going to show how to change this.
my_vehicle=Vehicle("saturn","ion","Green","v6")
my_vehicle.get_vehicle()
my_vehicle.get_make()
my_vehicle.get_color()
#we can change the individual color for a car(not a good idea this should be done as an instance variable and not an object variable.)
my_other_vehicle=Vehicle("Toyota","Corolla","Gray","v4")
my_other_vehicle.get_vehicle()
my_other_vehicle.get_make()
my_other_vehicle.get_color()
#We can create as many vehicles as we want based off of one class