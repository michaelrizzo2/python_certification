#while something is true do something.
x=1
while x<=10:
    x+=1#We need this to prevent an infinite loop.
    if x==6:
        continue#This will skip over 6
    print(f"The value of x is {x}")

else:
    print("Out of loop")