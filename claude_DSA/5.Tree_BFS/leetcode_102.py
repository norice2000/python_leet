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
        # edge case if not root return []
        # array result init
        # queue = deque([root])
        # while queue:
        ## level_length = len(queue)
        ## current_level = []
        ## for _ in range(level_length)
        ### node = queue.popleft()
        ### current_level.append(node.val)
        ### check children
        ### if node.left:
        #### queue.append(node.left)
        ### if node.right:
        #### queue.append(node.right)
        ## result.append(current_level)
        # return result

        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            current_level = []
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
    
sol = Solution()
print(sol.levelOrder(root))