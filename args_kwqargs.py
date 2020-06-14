def my_sum(*args):
    """
    This will take a unlimited` number of arguements and add them all together.
    We will not have to rewrite the code for a different number of arguements
    """
    init_sum=0
    for value in args:
        print(value)
        init_sum+=value
    return init_sum
out=my_sum(1,2,3,4,5,6,7,8,9,0,4,46,56,56,56,56,56,56,76,56,45,34,56)
print(out)
