# Node definition assuming binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Non-recursive tree traversal method
def traverse_tree(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=" ")  # Process the node
        current = current.right

# Create an example unbalanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(7)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(6)

# Test the non-recursive traversal method
traverse_tree(root)
