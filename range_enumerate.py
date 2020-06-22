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