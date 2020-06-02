my_list=[1,2,3,4,5]

#Now we will print the contents of my list

print (f" my list is {my_list}")

#NOw we are going to show the type of the list
print (f"The type of the list is {type(my_list)}")

#We are going to show the pop method and what it does to a list
#my_list.pop()
print (f"The result is {my_list}")# pop will remove the last element from a list 

#we can pop specific values
my_list.pop(0)
print (f"The result is {my_list}")# pop will remove the first element from a list 

#we will show how to change items in an list
my_list[0]="asvdfu"
print (f"The result is {my_list}")

#We can have a list inside another list
my_list[0]=["hello","furry"]
print (f"The result is {my_list}")
