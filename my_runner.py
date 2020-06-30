from my_class import Vehicle,Truck,Motorcycle

truck_1=Truck("Saturn","ion","Green","v6")
vehicle_1=Vehicle("Saturn","ion","Green","v6")
motorcycle=Motorcycle("Yamaha","motorcycle","Green","400hp")
#
#out1=vehicle_1.get_color()
#out2=vehicle_1.get_make()
#out3=vehicle_1.get_vehicle()
#out4=vehicle_1.get_body()
#print(out1,out2,out3,out4)

out1=truck_1.get_color()
out2=truck_1.get_make()
out3=truck_1.get_vehicle()
out4=truck_1.get_body()
vehicle_1.drive()
truck_1.drive()
motorcycle.drive()
print(out1,out2,out3,out4)

for v in [truck_1,motorcycle,vehicle_1]:
    v.drive()
