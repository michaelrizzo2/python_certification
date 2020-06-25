# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

def sequence(my_list):
    for i in range(len(my_list)-2):
        if my_list[i]==1 and my_list[i+1]==2 and my_list[i+2]==3:
            return True
    return False

out1=sequence([1, 1, 2, 3, 1]) 
out2=sequence([1, 1, 2, 4, 1]) 
out3=sequence([1, 1, 2, 1, 2, 3]) 
out4=sequence([1, 2]) 
out5=sequence([]) 
print(out1,out2,out3,out4,out5)