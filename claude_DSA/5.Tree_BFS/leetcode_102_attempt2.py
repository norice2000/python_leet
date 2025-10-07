class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree
    #    3
    #   / \
    #  9  20
    #    /  \
    #   15   7
#Output: [[3],[9,20],[15,7]]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_length = len(queue)
            level_result = []

            for _ in range(level_length):
                node = queue.popleft()
                level_result.append(node.val)

                # check children exists
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_result)
        return result


sol = Solution()
print(sol.levelOrder(root))