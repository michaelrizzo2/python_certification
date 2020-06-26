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