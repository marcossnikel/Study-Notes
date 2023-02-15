#Write a fucntion that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same
#length with the squares of the original integers also sorted in ascending order.

#Brute Force
def sortedSquaredArray(array):
    aray = []
    for index, value in enumerate(array):
        aray.append(value**2)
    return sorted(aray)

    #o(n) space
    #o(n log n) time


#Optimal Solution

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
      smallerValue = array[smallerValueIdx]
      largerValue = array[largerValueIdx]

      if abs(smallerValue) > abs(largerValue):
        sortedSquares[idx] = smallerValue * smallerValue
        smallerValue += 1
      else:
        sortedSquares[idx] = largerValue * largerValue
        largerValue -= 1
      
      return sortedSquares




# o(n) time
# o(n) space

