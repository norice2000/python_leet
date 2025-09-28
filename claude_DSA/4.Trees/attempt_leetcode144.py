# Test with our example tree
#       1
#      / \
#     2   3
#    / \
#   4   5
        # """Leetcode #144 - Binary Tree Preorder Traversal"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Construct tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Solutiohn
class Solution:
    def preorderTraversal(self, root):
        # init result array
        #dfs(root)
        ## if not root: return None
        ## result.append(root.val)
        ## dfs(root.left)
        ## dfs(root.right)
        #dfs(root)
        #return result
        
        result = []

        def dfs(root):
            if not root:
                return None
            
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return result


sol = Solution()
print("Preorder:", sol.preorderTraversal(root))   # [1, 2, 4, 5, 3]