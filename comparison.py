#A comparison operator will return True or False
print(10==10)
print(10!=10)

#String comparison
print("Hello"=="Hello")
print("Hello"=="hello")

#Sorting and integer comparison
print(10=='10')# a comparison operator also looks at the type of the data along with the quantity
#5 will be equal to 5.00 but not 5.01
#We will show the greater than and less than operator

print(5<10)#This will be True
print(5>10)#This will be False 

#we will show the greater than or eqaul to and less than or equal to operator
print(5<=10)#This will be True
print(5>=10)#This will be False 

#we will show the not equal to operator(aka negation operator)
print(5!=5)#This will be False 
print(5!=6)#This will be True
#we will show that we can use this for strings
print("5"!=5)#This should be True
print("Hello"!="Hello")#This should be False
#We can also combine this with the or keyword
print("Hello"!="Hello" or "5"!=5)#This should be True(False or True will give us True)
print("Hello"!="Hello" or "5"==6)#This should be False(False or False will give us False)
# we can also combine this with and
print(("Hello"!="Hello" or "5"==6) and True)#This should be False(False and True will give us False)
print(("Hello"!="Hello" or 6==6) and True)#This should be True(True and True will give us True)
#something=something will return true otherwise it is false
#we will show how to use the not keyword(not is the same as the negation operator)
print(not 5)#this will show False
print(not False)#This should be true
#All of the above could be assigned to variable.
condition =not (5==5)
print(f"The condition is {condition}") #This will be a boolean type
