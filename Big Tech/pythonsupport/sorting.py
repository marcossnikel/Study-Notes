#sorting
nums =[ 5,4,6,3,7]
nums.sort() #ascending order by default
print(nums)
#sorting in reverse order
nums.sort(reverse=True)
print(nums)

#sort list of strings
arr = ['bob','alice','jane','doe']
arr.sort() #default alphabetical order
print(arr)

#custom sort (length of string)
arr.sort(key=lambda x: len(x)) #key that is used to order
print(arr)

