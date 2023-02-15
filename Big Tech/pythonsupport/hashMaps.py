#most common [dict]
#no duplicates keys
map = {} 
map['bob'] = 25
print(map)
print(len(map))

map['bob'] = 12

print('bob' in map) #search
map.pop('bob')  #remove
print(map)

#key,value
map = {"alice" : 90 , "bob" : 70}
print(map)

#dict comprehension
map = {i: 2*i for i in range(3)} #graph problems
print(map)

#loop through maps
map = {"alice" : 90 , "bob" : 70}
for key in map: #default
    print(key,map[key])

#values
for val in map.values():
    print(val)

#unpacking
for key, val in map.items():
    print(key,val)