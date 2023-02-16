def nodeDepths(root):
    if root is None:
        return 0

    calculateDepth(root,0)
    

def calculateDepth(node,depth):
    return depth + calculateDepth(node.right, depth + 1) + calculateDepth(node.left, depth + 1)


