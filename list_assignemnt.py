list_1=["b","d","a","z",'x']
list_2=[1,2,3,4,5]

#we want to sort each list in reverse and then get the last 3 entries.
#list_2.sort().reverse()[-3:-1]
#list_1.sort().reverse()[-3:-1]
list_1.sort()
list_1.reverse()

list_2.sort()
list_2.reverse()

print(list_1[2:]+list_2[2:])
#['d', 'b', 'a', 3, 2, 1]