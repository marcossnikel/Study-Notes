# Branch Sums 🌲⚙


# Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.  

## A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.  

### Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.










### Topic : TREE

#### Notes:

- Recursive function in each node in the three , starting at the root node. **DFS**
    - Left side of the tree and them the right side

- Keep track of an **running sum** -> obtained in node above us.
- Functions need to run until have right or left nodes.

- LeafNodes : Neighter left node or right node -> Sum the current value of the **running sum** to an array of sums **ListSums**



**RECURSIVE SOLUTION**
 1. Recursive function receveing the node , the running sum and the list of sums.
 2. Declare an empty list.
 3. Keep track of the running sum. *Running Sum = sum of all nodes above it*
 4. In the function , calculate the new running sum `newRunningSum = runSum + node.value`
 5. Check if are an leaf node. (*no left or right nodes*) and append the new Sum.
 6. If not in leaf node:
       - Call the function in both nodes (right,left) passing the newRunningSum.
 7.  Return the sums list. 

 *EDGE CASE :* If we have just one child (right or node) we don´t want to look for `None.value`so we need to have an check in the top of our algorithm `if node is none: return`

## Complexity
**Time :** O(N) *N is the total of nodes in the binary tree*

**Space :** O(N) *Complicated -> afected by the list of branch sums and also effect by the recursive nature of the solution 'callstack'*

```python
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    resultArray = []
    calcBranch(root,0,resultArray)
    return resultArray


def calcBranch (node,runningSum,resultArray):

    if node is None:
        return
    
    newSum = runningSum + node.value

    if not node.left and not node.right:
        resultArray.append(newSum)
    
    calcBranch(node.left,newSum,resultArray)
    calcBranch(node.right,newSum,resultArray)
    

#complexity
# :: time => o(n)
# :: space => o(n)

```