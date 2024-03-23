class TreeNode:
    def __init__(self, value):
        self.value = value  # Value of the current node
        self.children = []  # Children of the current node

def compute_heights(root):
    
    if root is None:
        return -1  # Base case: Return -1 if the tree is empty
    
    # Postorder traversal to calculate heights bottom-up
    for child in root.children:
        compute_heights(child)
    
    # Calculate height of the subtree rooted at current node
    if root.children:
        root.height = max(child.height for child in root.children) + 1  # Height is maximum height of children + 1
    else:
        root.height = 0  # If node has no children, its height is 0
    
    # Print element and height of current node
    print(f"Element: {root.value}, Height: {root.height}")

# Test the algorithm
if __name__ == "__main__":
    # Example tree
    root = TreeNode(1)
    root.children = [TreeNode(2), TreeNode(3)]
    root.children[0].children = [TreeNode(4), TreeNode(5)]
    root.children[1].children = [TreeNode(6)]
    root.children[1].children[0].children = [TreeNode(7), TreeNode(8)]

    compute_heights(root)
