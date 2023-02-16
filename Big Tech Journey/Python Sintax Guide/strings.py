#similar to arrays
s = "hihi"
print(s[0:2])


#they are immutable
# s[0] = 'A' #CANT


#updating the stream -> creates a new one
s += 'vasco'
print(s)
#modify string -> n time operation.


#strings can be converted to integers and integers added
print(int("123") + int("123"))

#integers can also be converted to strings
print(str(123)+ str(123))


#if you need the asc value of the char
print(ord("a"))
print(ord("A"))

#combine a list of strings (with an empty string delimitor)
strings = ["ab","cd","ef"]
print("_".join(strings))