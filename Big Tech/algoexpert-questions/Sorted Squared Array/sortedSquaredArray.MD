# video explanation tips

# considerate negatives

# optimal solution
# [-7,-5,-4,3,6,8,9]

since the input array is going to be sorted , should allow us to solve the problem in linear time.
only work because it is sorted.
empty array -> as we go further left in the negative numbers and further right in the positivies of the array, the squares
became larger. we can look at the absolute value of the right and left , compare them, higher(higher square).

is possible to look the values at the beggining and the last of the array, compare those values and determinated which is larger, this tell us which position we should append to the new array.

we always 'compete' these values and them add in the new array the square of the highest number.

and so we go to the next element....

- compare the absolute values and them add the square of the number in the last position of our array.
- create the array by the end