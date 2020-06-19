employees={"mike":77000,"Robert":100000,"Pikachu":40000}
for key,value in employees.items():
    print(key,value)

for value in employees.values():
    print(value)

for value in employees.keys():
    print(value)

employees=[("mike",77000,2),("Robert",100000,4),("Pikachu",40000,1)]

for key,value,year in employees:#This is how you unpack a tuple.
    print(key,value,year)