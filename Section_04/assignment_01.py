# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""
def twelver(a,b):
    if a ==12 or b==12 or a+b==12:
        return True
    else:
        return False

out1=twelver(3, 12)
out2=twelver(4, 9) 
out3=twelver(9, 3) 

print(out1,out2,out3)