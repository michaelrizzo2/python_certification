sentence="i'm coming home"

new_sentence="i'm coming \n home"

next_sentence="This is my new sentence"

print(sentence)

print(new_sentence)

#We are now going to print the first character

#The first index will start at zero.

print(f"The first character is {next_sentence[0]}")

#The first inedx will start at zero and will increase  by one

#We are going to print to print the last character(This is for when you know the length of the sentence)

print(f"The last character is {next_sentence[22]}")

#What if we do not know how long the sentence is.This will show negative indexing positions

print(f"The last character is {next_sentence[-1]}")

#Negative Indexing will go from -1,-2,-3 all the way to the beginning.

#We are going to show slicing of a string

#The second value in a slicing is not inclusive.It will always be one less than the last index.
print (f"slicing string will result in {next_sentence[0:4]}")

#To get the word is
print (f"{next_sentence[5:7]}")

# to get every other character
print (f"The result is {next_sentence[0:len(next_sentence):2]}")

#The last thing
#we want to show 
print(f"The result is {next_sentence[3:]}")

print(f"The result is {next_sentence[-3:]}")