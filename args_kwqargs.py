def my_sum(*args):
    """
    This will take a unlimited` number of arguements and add them all together.
    We will not have to rewrite the code for a different number of arguements
    """
    init_sum=0
    for value in args:
        init_sum+=value
    return init_sum
out=my_sum(1,2,3,4,5,6,7,8,9,0,4,46,56,56,56,56,56,56,76,56,45,34,56)
print(out)


def key_value_func(**kwargs):
    print(kwargs)
    #we can print the keys
    print(kwargs.keys())
    #we can print the values 
    print(kwargs.values())
    #We can get a specific key
    print(kwargs.get("weight"))
    print(kwargs.get("Fur"))# a key that does not exist will get the value of none.

key_value_func(name="Mike",weight=200,age=32)#This will take care of multiple default arguements(This will result in a dictionary)
