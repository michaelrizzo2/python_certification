#print in python 3 is a function instead of a ststement in python 3
print("Hello World")#"Hello world is the arguement"

#To define a function we use the def command
def greet_person(name="Name Here"):
    print("This is the body of a function")
    print("Hello this is a greeting from "+name)

#Do not forget to call the function
greet_person()
greet_person("michael")
#we need to define the function before we call the function,otherwise we will get an error saying the function does not exist 
#you can also set a default value for the arguement
#to convert a interger to a string do str(variable)