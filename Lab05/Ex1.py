def inorderNext(p):
    if p.right is not None:
        # Case 1: If p has a right child, return the leftmost node in the right subtree
        current = p.right
        while current.left is not None:
            current = current.left
        return current
    else:
        # Case 2: If p does not have a right child, backtrack to find the nearest ancestor
        #         that has a right child.
        while p.parent is not None and p == p.parent.right:
            p = p.parent
        # Return the parent node of the input node, which is either the nearest ancestor
        # with a right child or None if the input node is the rightmost node in the tree.
        return p.parent

# Example test case
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.parent = root
root.right = TreeNode(3)
root.right.parent = root
root.left.left = TreeNode(4)
root.left.left.parent = root.left
root.left.right = TreeNode(5)
root.left.right.parent = root.left

# Testing the algorithm
print(inorderNext(root.left.left).val)  # Output should be 2
print(inorderNext(root.left).val)       # Output should be 5
print(inorderNext(root.left.right).val) # Output should be 1
