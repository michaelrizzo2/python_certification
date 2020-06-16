#we are going to discuss variable scope in this lesson
age=27#This age is a global variable

def increase_age():
    age=30#This age is a local variable.
    def add_4_to_age(age):
        age+=4
        print(f"Nested Method and the age is {age}")
    add_4_to_age(age)
    print(age)#This will print 30 because the only age we have is 30
print(age)#This will print the 27 due to the fact that we do not have access to the function right now

print(increase_age())#This will give us 30 because we are accessing the age inside the function. 

#We are going to continue with scope and nested functions
#globalvalue -> function value-> inner function value
