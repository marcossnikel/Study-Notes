# My tought about this question
Well , have an BST :
-> Binary Search Tree
So , the tree is completed balanced, that means :

- Each BST node has an integet value , a left child node , and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property : its value is strictly greater than the values of every node to is left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None/Null.

So the question is :
**Write a function that takes in a Binary Search Tree(BST) and a target integer value and returns the cloest value to that target value in the BST**
*You can assume that always will have one closest value*

### My Toughts
1. We can split the tree in the half of every single check, for an example : if our target is 23 and our root of the tree is 15, we know that we need to go to the right of the tree, and we can remove the second part.
2. We need to keep doing this split in the half until we found the closest value. 
3. Variable to keep track the closest value
4. I stop here because my lack of knowledge writing tree sintax :(

# Clement Conceptual Overview
 example :
 tree :
         10
        /  \
       5      15
       / \   /  \
       2  5 13   22
      /      \
     1       14
target : 12
-> gives an bst and an target value, you wanna find the closest value to the target value in the bst.

1. Create an variable to keep track of the closest value in the bst. And continually updated.

At the beggining -> [closest = infinity.] or null or anything.

2. look for the difference between our target and our tree node. (absolute value) (10!=12) => 2.
3. the abs value its smaller them our closest node and our target node ?
4. if ye , we compute infinity - 12 = infinity
5. that says to us that 10 are closest to 12 them infinity to twelve.
6. that means that our currentNode is closer to our target them our curentClosest ,so :
7. closest = currentNode. (10)

and just now

1. Compare 10 to 12 (is equal ? greather ? less ?)
2. 10 is smaller , all the numbers to the right of 10 are greather or equal, and in the left, are smaller.
3. we just delete the left and because its far away to the target.
4. now we go to the 15 (back to the pass 2 (compare abs)) (now its 2, but now is 3) that means: that 15 are more far away from 12 them 10, we dont update our closest.
5. compare 15 to 12 , we know that 12 is less them 15 so now we need to go to the left of the node. [eliminate 22]

and now
1. we are at the node at value 13 (compare abs value)(1) -> update closest
2. compare current value(13) with the target, and happens that 12 is smaller them 13, so we elimate the entire right way of the tree (14). and we go down to the left, however, it will be Null/None.
3. at this point , we are done , we just return the closest value.

edge case : if we ever get until an point the abs value the diff is 0, we stop there because the number is in the three.

**Space and time complexity**
Time : Avarage :  O(log n ) // n -> number of nodes in the tree || Worst Case Scenario : O(n) -> only has one branch.

Space : Two possibilities:
*Recursive* : On avarage , the same of time O(log n) || worst o(n)
*Interative* : O(1) Constant Space || Always


# Recursive Solution Code
```python
def findClosestValueInBst(tree, target):

    return findClosestValueInBstHelper(tree,target,float("inf"))

  
  

def findClosestValueInBstHelper(tree,target,closest):

    if tree is None:

        return closest

    if abs(target - closest) > abs(target - tree.value):

        closest = tree.value

  

    if target < tree.value:

        return findClosestValueInBstHelper(tree.left,target,closest)

    elif target > tree.value:

        return findClosestValueInBstHelper(tree.right,target,closest)

    else:

        return closest
```


# Interactive Solution Code

```python
def findClosestValueInBst(tree, target):

    return findClosestValueInBstHelper(tree,target,float("inf"))

  
  

def findClosestValueInBstHelper(tree,target,closest):

    currentNode = tree

    while currentNode is not None:

        if abs(target - closest) > abs(target - currentNode.value):

            closest = currentNode.value

  

        if target < currentNode.value:

            currentNode = currentNode.left

        elif target > currentNode.value:

            currentNode = currentNode.right

        else:

            break

    return closest
```