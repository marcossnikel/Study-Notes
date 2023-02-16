#really useful

mySet = set() #constant time , insert values in constant time -> no duplicates
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(3 in mySet)


mySet.remove(2) #constant time
print(2 in mySet)


#list to set -> initialize an set w values
print(set([1,2,3]))

#set comprehension
mySet = {i for i in range(5)}
print(mySet)