# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""
def string_match(string1,string2):
    #We need to get the length of the shortest string
    positions_matched=0
    short_length=min(len(string1),len(string2))
    for i in range(short_length-1):
        string1_sub=string1[i:i+2]
        string2_sub=string2[i:i+2]
        if string1_sub==string2_sub:
            positions_matched+=1
    return positions_matched

out1=string_match('xxcaazz', 'xxbaaz')
out2=string_match('abc', 'abc')
out3=string_match('abc', 'axc') 
print(out1,out2,out3)