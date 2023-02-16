# Node Depths 🌲⚙

### Topic : TREE

# QUESTION
- The distance between a node in a Binary Tree and the tree´s root is called the node´s depth.

- Write a function that takes in a Binary Tree and returns the sum of it´s nodes depths

- Each Binary Tree node has an integer value, a left child node , a right child node. Children nodes can either be Binary Tree or None/Null



#### Notes:

- IMPOSSIBLE TO KNOW THE DEPTH OF AN SPECIFIC NODE WITHOUT HAVE ACCESS TO THE REST OF THE TREE :mega:
- Is necessary to us have information about all parent nodes of the specific child.
- We know the root depth (0) , and with this information we know the depth of both child nodes (depth + 1) and so on and so far.
- So, the thing is, tell to all childs of nodes this quote *Your depth is my own depth plus 1*
- If don´t have children nodes -> **STOP**



**RECURSIVE SOLUTION**

1. Call the recursive function in the childs of our root.
2. We pass the root depth (0) and say to the child that his depth is `root depth + 1`
3. our function stay something like that :
    - F(Node,Depth) = depth + F(leftNode,depth+1) + F(rightNode,depth+1)

**INTERACTIVE SOLUTION**

1. We use an stack to traverse the tree
    1. Our stack keeps an HashMap with the node and his depth `[{"node" : root, "depth" : 0}]`
2. Add the root node in the top of the stack.
3. *So long we have nodes in the stack, pop them off the stack and apply the algorithm*
4. Keep track of the 'runningSum' -> when pop add the popped num to the sum.
5. Look their children -> púsh to the top of the tree stack.
6. Give the parent depth, make depth + 1 and add to the runningSum.
## Complexity

**Time :** O(N) *N is the total of nodes in the binary tree*

**Space :** O(H) *Complicated -> H is the height of the binary tree. || in balanced trees, O(H) seems like O(log n)*


# Recursive Solution Code

- Outside Function

```python
def nodeDepths(root):

    if root is None:

        return 0

  

    calculateDepth(root,0)

  

def calculateDepth(node,depth):

    return depth + calculateDepth(node.right, depth + 1) + calculateDepth(node.left, depth + 1)
```

- Direct Recursion in the function

```python
def nodeDepths(root,depth = 0):
	if root is None:
		return 0

	return depth + nodeDepths(root.left,depth + 1 ) + nodeDepths(root.right,depth + 1)
```


# Interactive Solution Code

```python
def nodeDepths(root):

    #interactive

    sumOfDepths = 0

    stack = [{"node": root, "depth" : 0}] #initializing in the root node , we need to put his node and the depth

  

    while len(stack) > 0:

        nodeInfo = stack.pop()

        node, depth = nodeInfo["node"], nodeInfo["depth"]

        if node is None:

            continue

        sumOfDepths += depth

        stack.append({"node": node.left, "depth" : depth + 1})

        stack.append({"node": node.right, "depth" : depth + 1})

    return sumOfDepths
```
