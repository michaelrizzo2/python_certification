# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""
def sum78(my_list):
    my_sum=0
    continue_sum=True
    for number in my_list:
        if number==7:
            continue_sum=False
        if continue_sum==True:
            my_sum+=number
        if number==8:
            continue_sum=True
    return my_sum

out1=sum78([1, 2, 2]) 
out2=sum78([1, 2, 2, 7, 99, 99, 8]) 
out3=sum78([1, 1, 7, 8, 2]) 
print(out1,out2,out3)
