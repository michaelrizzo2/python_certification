list_1=[1,2,3,4,5,6]
list_2=["hi","my","Name","is","Michael","Rizzo"]
list_3=[7,8,9,10,11,12]

#We can iterate through three lists at the same time

for item1,item2,item3 in zip(list_1,list_2,list_3):
    print(item1,item2,item3)

# We can probably extend this through multiple lists.
#We can also do this

for a,b,c in list(zip(list_1,list_2,list_3)):
    print(a,b,c)

print('z' in list_1)#This will return a boolean vaslue of false.

print ("John" in {'John':140})#THis will return a boolean value of true Only a key gets checked for the in statement for a dictionary.

print(140 in {"john":140})
print(140 in {"john":140}.values())