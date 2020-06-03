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

# we will show how the append method will add items to the end of a list
my_list.append(6)
print (f"The result is {my_list}")
#popping an itme off the list will undo an append you just did.
#we can pop the end of a list into another variable
pop_variable=my_list.pop()
print (f"The result of the list being popped is {pop_variable} and the list is now {my_list}")

# The append method will return None
#if we append [10,99,1090] we wil not get each item from the list
my_list.append([10,99,1090])
print (f"The result is {my_list}")
#sort is a method that will sort objects
new_list=[5,1,2,4,3] #by defalut the sort method will return none
new_list.sort()
print(f"THe sorted list will be {new_list}")
#We can also reverse the entiores in a list
new_list.reverse()
print(f"THe list is now {new_list}")