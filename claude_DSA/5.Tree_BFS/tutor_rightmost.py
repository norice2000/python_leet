# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)


from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            length = len(queue)
            level_result = []
            for _ in range(length):
                node = queue.popleft()
                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_result[-1]) # take last value in array
        return result

sol = Solution()
print(sol.averageOfLevels(root))