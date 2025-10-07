# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level_result = []

            for _ in range(level_size):
                node = queue.popleft()
                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            average = sum(level_result) / len(level_result)
            result.append(average)
        return result
    
sol = Solution()
print(sol.averageOfLevels(root))