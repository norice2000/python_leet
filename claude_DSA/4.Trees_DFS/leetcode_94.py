# Test with our example tree
#       1
#      / \
#     2   3
#    / \
#   4   5
        # """Leetcode #94 - Binary Tree InOrder Traversal"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#Create soltiion
class Solution:
    def inorderTraversal(self, root):
        # result array

        # def dfs(root)
        ## if not root: return None
        ## dfs(root.left)
        ## result.append(root.val)
        ## dfs(root.right)

        #dfs(root)
        #return result

        result = []

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)

        dfs(root)
        return result

sol = Solution()
print("Inorder:", sol.inorderTraversal(root))     # [4, 2, 5, 1, 3]