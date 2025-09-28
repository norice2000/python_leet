# Test with our example tree
#       1
#      / \
#     2   3
#    / \
#   4   5
# Leetcode #145 - Binary Tree Postorder Traversal 
class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

# Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

class Solution:
    def postorderTraversal(self, root):
        # init result array

        # def dfs(root)
        ## if not root, return None
        ## dfs(root.left)
        ## dfs(root.right)
        ## result.append root val

        result = []

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)

        dfs(root)
        return result

sol = Solution()
print("Postorder:", sol.postorderTraversal(root)) # [4, 5, 2, 3, 1]
