#tuples -> similar to arrays
#parentheses to initialize and immutable
tup = (1,2,3)
print(tup)
#can´t modify

#mainly used as key in hashmap/set
map = {(1,2) : 3} #hashable key
print(map)

myset = set()

myset.add((1,2))
print(myset)
print((1) in myset)
#lists can´t be keys