#This will show all of the various string methods
my_sentence="This is my test sentence"

#We will make the whole sentence uppercase
print(f"{my_sentence.upper()}")

#we can make the whole sentence lowercase
print(f"{my_sentence.lower()}")

#we can Capitalize the first letter of each word
print(f"{my_sentence.capitalize()}")

#isdigit will return true if the string is a number
print(f'{my_sentence.isdigit()}')

#isalnum will return if a string has numbers or letters it does not recognize spaces.
print(f"{my_sentence.isalnum()}")

#startswith method will check to see if a method starts with a set of characters\
print(f"{my_sentence.startswith("7645")}")