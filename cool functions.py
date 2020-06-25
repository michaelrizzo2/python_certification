from random import randint,shuffle
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

print(max(list_1))

print(min(list_1))

char_list=["a","b","c","d","e","f"]

print(max(char_list))
print(min(char_list))#Max and min also work for characters

#we are going to generate a random number
print(randint(0,1000))#the last number of the range will not be inclusive.

#we are going to learn how the shuffle method works.
shuffle(list_1)
print(list_1)#shuffle will randomly move the contents around of a list.

#create a list from 1 to 100 ands shuffle all of the numbers.
out_list=[]
for i in range(1,101):
    out_list.append(i)

shuffle(out_list)
print(out_list)