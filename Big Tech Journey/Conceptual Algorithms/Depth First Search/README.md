

# Depth First Search `:rocket:`

sibling of *breath first search*

Considered an **easy algorithm** `:heavy_check_mark:`


:: Really Important to know how to implement. `:zap:`



#### Treverse/explore an graph

- graph could be represented as an tree like data structure with a bunch of nodes, and each node has a **name** that is an letter in the alfabet and optionally he can have an child node

![[Pasted image 20230216193501.png]]


:: the goal is **treverse the graph** and as we traverse , we put the names in an array and return an array.

in this case -> **[ABEFIJCDGKH]**

How it works ?

1. We go deep as we can in each branch before exploring the next branch , the next branch, go deep again,....

2. Can be implemented in an beautiful way using recursion in each child node.

3. Add the first vertice name to the array.

4. When you get in some specific node.

5. Add him to the array (his name)

6. For every child in his child, call the dps function and pass the final array.



### Space and Time Complexity

:: We deal with ***vertices*** and ***edges*

vertices ==== node in the graph
edges ==== connected lines ***(e) variable***


###### Time : O(V+E)
V - Number of Vertices [aka nodes]
E - Number of Edges

::: Iterating to the childs ::: > for loop ::: loop complexity = *n of childs*


###### Space : O(V)
Worst case scenario :::: O(V) space :::: we are adding a bunch of frames to the call stack, as we go deeper , we add frames to the call stack.


```python

# This implementation of DPS is foward to the question in algo expert

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
            array.append(self.name)
            for child in self.children:
                child.depthFirstSearch(array)
            return array
```

