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
        return Vehicle.vehicle_counter

    def get_make(self):
        return self.make
        
    def get_color(self):
        return self.color

    def get_body(self):
        return self.body
    
    def drive(self):
        print("Vehicle driving")
    
class Truck(Vehicle):
    #this is method overloading in other languages.
    def drive(self):
        print("Truck Driving")

class Motorcycle(Vehicle):
    def drive(self):
        print("motorcycle going fast")
#having the same method for a different class is called polymorphism