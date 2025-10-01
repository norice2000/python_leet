#       1
#      / \
#     2   3
#    /
#   4
class TreeNode:
    def __init__(self, val=0, left=None, right=None): # default if not specified
        self.val = val
        self.left = left
        self.right = right

# Step 1: Create the nodes (like linked list!)
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

# Step 2: Connect them - YOUR TASK!
# root should have left=node2, right=node3
# node2 should have left=node4, right=None
# node3 should have left=None, right=None  
# node4 should have left=None, right=None

# Your connections here:
root.left = node2
root.right = node3
node3.left = None
node3.right = None
node2.left = node4
node2.right = None
node4.left = None
node4.right = None

## Note, no need to specify the `None` values since it is the default

# tree traversal
def print_tree_inorder(root):
    if root:
        print_tree_inorder(root.left)
        print(root.val)
        print_tree_inorder(root.right)

print_tree_inorder(root)
# outputs
# 4
# 2
# 1
# 3
# Reason:
# Go to leftmost node (4) → print 4
# Back to parent (2) → print 2
# Back to root (1) → print 1
# Go to right child (3) → print 3