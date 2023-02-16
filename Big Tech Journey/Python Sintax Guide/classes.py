class MyClass:
    def _init_(self,nums):
        #member variables
        self.nums : nums
        self.size = len(nums)

    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()