class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

root.left = node2
root.right = node3
node2.left = node4

def find_value(root, target):
    # if root is false, return none
    # if root.val == target, return root
    # LEFT
    # left_node = find_value(root.left, target)
    # if left_node: true, return left_node
    # RIGHT
    # right_node = find_value(root.right, target)\
    # if right_node: true, return right_node

    if not root:
        return None
    
    if root.val == target:
        return root.val
    
    left_node = find_value(root.left, target)
    if left_node:
        return left_node
    
    right_ndoe = find_value(root.right, target)
    if right_ndoe:
        return right_ndoe

print(find_value(root, 4))  # Should return the node with value 4