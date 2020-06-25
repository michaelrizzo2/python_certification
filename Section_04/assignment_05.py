
# Assignment 5

"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.


first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False

"""

def first3(my_list):
    for i in my_list[0:4]:
        if i ==6:
            return True
    return False

out1=first3([1, 2, 6, 3, 4]) 
out2=first3([1, 2, 3, 4, 6]) 
out3=first3([1, 2, 3, 4, 5]) 
print(out1,out2,out3)