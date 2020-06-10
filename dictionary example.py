#The basic of a dictionary is a key is linked to a value
my_dict={"k1":"My data",7:"other data"}
#Dictionaries are key oriented not index oriented
#Lists and tuples are index oriented
print(my_dict["k1"])

print(my_dict[7])
#you cna change a dictionary unlike a tuple
my_dict[7]="ivbiebvav"
print(my_dict[7])

people_weight={"rastachu":34,"Regular pikachu":17,"Ash":140}
print(people_weight)
people_weight["rastachu"]=20
print(people_weight)

#We want to get rid of Ash
people_weight.pop("Ash")
print(people_weight)
#we can clear out a dictionary using the clear method
people_weight.clear()
print(people_weight)

# we can also add a new key to a dict
people_weight["aquachu"]=10
print(people_weight)

#The value for a key can be another list
people_weight["nuclearchu"]=[10,30]
print(people_weight["nuclearchu"][0])
print(people_weight["nuclearchu"][1])

#We are going to have a dictionary inside a list inside of a dictionary
new_dict={"Michael": "Rizzo","items":[1,{"my_key":1}]}
print(f"The result i am looking for is {new_dict['items'][1]['my_key']}")

#we are going to add a new tuple to the dictionary
new_dict["my_tuple"]=(1,2,3,4)

#we are going to remove thre tuple from the dictionary
new_dict.pop("my_tuple")
print (new_dict)