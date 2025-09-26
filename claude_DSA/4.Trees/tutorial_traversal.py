class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        """Leetcode #144 - Binary Tree Preorder Traversal"""
        result = []
        
        def dfs(node):
            if node is None:
                return
            
            result.append(node.val)  # Process BEFORE recursion
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result
    
    def inorderTraversal(self, root):
        """Leetcode #94 - Binary Tree Inorder Traversal"""
        result = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            result.append(node.val)  # Process BETWEEN recursions
            dfs(node.right)
        
        dfs(root)
        return result
    
    def postorderTraversal(self, root):
        """Leetcode #145 - Binary Tree Postorder Traversal"""
        result = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)  # Process AFTER recursions
        
        dfs(root)
        return result

# Test with our example tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print("Preorder:", sol.preorderTraversal(root))   # [1, 2, 4, 5, 3]
print("Inorder:", sol.inorderTraversal(root))     # [4, 2, 5, 1, 3]
print("Postorder:", sol.postorderTraversal(root)) # [4, 5, 2, 3, 1]