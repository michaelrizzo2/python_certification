# Assignment 9

"""
We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with
the associated value of that email looked up from the dictionary d.
If the dictionary does not contain the email found in the list, add a new entry
in the dictionary for the email found in the fr list. The value for this new email key
will be the next highest value number in the dictionary in string format.

Once the dictionary is populated with this new email key and a new number value,
replace that email's occurrence in the fr list with the number value.

The output of running your completed code should be the following:

Value of fr:
['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
Value of d:
{'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}

"""

# Don't manually change fr and d.
fr = [
'7@comp1.COM|4|11|GDSPV',
'7@comp1.COM|16|82|GDSPV',
'13@comp1.COM|12|82|GDSPV',
'26@comp1.COM|19|82|GDSPV'
]

d= {
'7@comp1.COM': '199',
'8@comp4.COM': '200',
'13@comp1.COM': '205'
}


# Your Code below:
# --------------------------------------
my_out_line=[]
#We need to split the line by |
for line in fr:
    columns=line.split("|")
    #We need to check if the value exists in the dictionary
    # we need to get the look up value for this to work.
    value=columns[0]
    if value in d.keys():
        columns[0]=d.get(value)
        my_out_line.append("|".join(columns))
    else:
        #we need to get the value
        next_number=int(max((d.values())))+1
        d[value]=str(next_number)
        columns[0]=str(next_number)
        my_out_line.append("|".join(columns))

    
# don't change the below:
# --------------------------------------
print("Value of fr: ")
print(fr)
print("Value of d:")
print(d)















