number_list=[]

for number in range(1,6,2):#The last number in the range is not inclusive.
    number_list.append(number)

print(number_list)

#Now we wil show off the zip function.
list_1=[1,2,3,4,5]
list_2=["My","name","is","Michael","rizzo"]
out=zip(list_1,list_2)#This will give us a collection of tuples.


for item in out:
    print(f"The item is {item}")
new_list=[]
for item_1,item_2 in zip(list_1,list_2):
    new_list.append(item_1)#append will always only take one arguement.
    new_list.append(item_2)

print (new_list)    
#we wil show off the enumerate function.
for index,entry in enumerate(list_2):
    print(index,entry)
#Enumerate will generate a index along with the value automatically.

#The zip function will do the highet nmber of elements that are in each list. If you have a list of 3 entries and a list of 5 entries. The zip function will do only 3 entries.