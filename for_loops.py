#we are going to do iteration in python
farm_animals=["Goat","Horse","Pig","Sheep","Duck","Cow"]
#for animal in farm_animals:
    #print (f"The animal is {animal}")
    #print(f"The {animal} is safe in the farm.")

counter=0

for animal in farm_animals:
    counter+=1
    print(f"{counter} {animal} is safe in our farm")

greeting="Hello My name is Michael"

for char in greeting:#This will iterate character by character
    if char=="n":
        continue#This will move on to the next element. break will break out of a specific loop.
    else:
        print(f"The character is {char}")