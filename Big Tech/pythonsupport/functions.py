def func(n,m):
    print(n+m)

func(2,4)


#nasted functions -> really helpful in recursion problems
#the inner functino have access to all outer functions values.
def outer(a,b):
    c = 'c'

    def inner():
        return a + b +c
    return inner()

print(outer("a","b"))


#can modify objects but not reassign unless usign nonlocal keyword
def double(arr,val):
    def helper():
        #modify array works
        for i , n in enumerate(arr):
            arr[i] *= 2

            #however ,will only modify val in the helper scope
            # val*=2

            #this will modify val outside helper scope
            nonlocal val
            val *=2
    helper()
    print(arr,val)

nums = [1,2,3]
val = 3
double(nums,val)