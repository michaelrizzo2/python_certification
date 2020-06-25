# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""
def last2(my_string):
    string_to_check=my_string[-2:]
    #Now we need to check how many time sthis string shows up.
    count=0
    for i in range(len(my_string)-2):
        if my_string[i:i+2] ==string_to_check:
            count+=1
    return count
out1=last2('hixxhi') 
out2=last2('xaxxaxaxx') 
out3=last2('axxxaaxx') 
print(out1,out2,out3)