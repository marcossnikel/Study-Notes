#also calleds lists in python

arr = [1,2,3]
print(arr)

#can be used as stack
arr.append(4)
arr.append(5)
print(arr)
arr.pop()
print(arr)
#insert in the middle
#o(n)
arr.insert(1,7)
print(arr)

#reassigned -> o(1)
arr[0] = 0
arr[3] = 0
print(arr)

#initialize arr of size n with default value of 1
n = 5
arr = [1]* n
print(arr)
print(len(arr))
print(arr[-1]) #returns the last value

#indexing -2 is the second to last value , etc.
print(arr[-2])

#subslists [aka slicing array]
arr = [1,2,3,4]
print(arr[1:3]) #values of index 1 into index 3 but not including index 3.


#similar to for loop ranges ,last index is non inclusive
print(arr[0:4])


#unpacking -> each variable an element in array
a,b,c = [1,2,3]
#go through list of pair
#need to match number of variables and elements in array


#loop through arrays.
nums = [1,2,3]

#using index 
for i in range(len(nums)):
    print(nums[i])

#without index
for i in nums:
    print(i)

#with index and value
for index , value in enumerate(nums):
    print(index,value)

#loop through multiple arrays simultaneosly with unpacking
#zip would take both arrays and combine them in an array of pairs and them unpack them
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1,n2 in zip(nums1,nums2):
    print(n1,n2)


#reverse
nums=[1,2,3]
nums.reverse()
print(nums)

