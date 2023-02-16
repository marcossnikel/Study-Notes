#division is decimal by default
print(5/2)

#integer division -> double slash
print(5//2)

#careful: most languages round towards 0 by default so negative numbers will round down
print(-3//2)
#negative round down upper.
#solution to this is use de decimal division and then covert to an int
print(int(-3/2))


#module operator similar to other languages
print(10%3)
#negative values are fuckes
print(-10%3)

#be consistent
import math
print(math.fmod(-10,3))

#math helpers
print(math.floor(3/2)) #round down
print(math.ceil(3/2)) # round up
print(math.sqrt(2)) #squared root
print(math.pow(2,3)) #pow

#max or min number
float('inf')
float('-inf')

print(math.pow(2,200))
print(math.pow(2,200) < float('inf'))