# Input: root = [3,9,20,null,null,15,7]

#        3
#       / \
#      9  20
#        /  \
#       15   7

# Output: [[3],[20,9],[15,7]]  ← Notice level 1 is reversed!

# Level 0: left to right → [3]
# Level 1: right to left → [20, 9]
# Level 2: left to right → [15, 7]

# Step 1: Define TreeNode class
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
    def bfs_zigzag(self, root):
        # edge case if not root return []

        #queue = deque([root])
        # result = []
        # while queue:
        ## zigzag = 0
        ## level_length = len(queue)
        ## level_result = [] #substring
        ## for _ in range(level_length)
        ### node popleft
        ### level_result.append(node,val)
        ### check for children
        ### for node.left:
        #### add to queue
        ## if node.right:
        ### add to queue

        ### if zigzag % 2 == 1:
        ### reverse the result
        ## result.append(level_length)
        ## level += 1
    # return result
        if not root:
            return []
        
        queue = deque([root])
        result = []
        zigzag = 0

        while queue:

            level_length = len(queue)
            level_result = []
            for _ in range(level_length):
                node = queue.popleft()
                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if zigzag % 2 == 1:
                level_result.reverse()
            result.append(level_result)
            zigzag += 1
        return result

sol = Solution()
print(sol.bfs_zigzag(root))