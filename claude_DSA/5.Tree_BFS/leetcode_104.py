# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #     3
    #    / \
    #   9   20
    #      /  \
    #     15   7
# TRee
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

from collections import deque
class Solution:
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

sol = Solution()
print(sol.maxDepth(root))