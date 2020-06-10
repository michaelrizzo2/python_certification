#The difference between a list and a tuple is the tuple cannot be edited.
my_list=[1,2,3]
my_list[0]=2
print(f" my list is now {my_list}")

my_tuple=(1,2,3,4,56,76,768)
#my_tuple[0]=2#doing this will give us the error that tuple values cannot be reassigned
my_count=my_tuple.count(2)
print(my_count)
#tuple slicing is the same as list slicing.
print(my_tuple[1:])