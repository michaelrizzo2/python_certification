# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""
def grow_string(my_string):
    result=''
    for i in range(len(my_string)):
        result+=my_string[0:i+1]
    return result

out1=grow_string('Code') 
out2=grow_string('abc') 
out3=grow_string('ab') 
print(out1,out2,out3)