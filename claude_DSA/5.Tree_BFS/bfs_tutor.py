# Binary tree
class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)
    
#       1
#     2   3
#   4  5  10

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(10)

from collections import deque

#Level order Traversal (BFS)

def level_order(root):
    queue = deque()
    queue.append(root)

    while queue:
        root = queue.popleft()
        print(root)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

print(f"level_order: {level_order(root)}")
# 1
# 2
# 3
# 4
# 5
# 10



