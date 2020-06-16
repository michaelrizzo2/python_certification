# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
# Your Code Below:
def multi_merge(list_a,my_str):
    return list_a+my_str.split()+list(my_str)

print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
