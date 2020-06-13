#print in python 3 is a function instead of a ststement in python 3
print("Hello World")#"Hello world is the arguement"

#To define a function we use the def command
def greet_person(name="Name Here"):
    '''
    This function will return a greeting
    The only input is the name
    '''
    print("This is the body of a function")
    return "Hello this is a greeting from "+name

#Do not forget to call the function
greeting1=greet_person()
greeting2=greet_person("michael")
#we need to define the function before we call the function,otherwise we will get an error saying the function does not exist 
#you can also set a default value for the arguement
#to convert a interger to a string do str(variable)
# we add return to a function so we can use the function for multiple things without having to rewrite the function each time.
print(f"The first result is {greeting1} and the second result is {greeting2}")

def remainder(number1,number2):
    result=number1% number2
    return result
out=remainder(3,2)
print(f" The result is {out}")

#Python runs code from the top to the bottom and the indentation needs to be consistent(do not mix tabs and spaces.)