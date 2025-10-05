# Binary tree
class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)
    
#       1
#     2   3
#   4  5  10

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(10)

class Solution:
    def pre_order(self, root):
        # if root is none, return None
        #recursive function
        # create array result
        #def dfs(root)
        # append result
        # pre_order(root.left)
        # pre_order(rooght.right)
        # return result
        #call dfs(root)
        # return result
        
        result = []

        def dfs(root):
            if not root:
                return None
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return result
    
    def in_order(self, root):
        # init result array
        #create recursive fucntion
        # def dfs(root)
        # h pattern where parent print inbteween
        ## dfs(root.left)
        ## result.append(root.val)
        ## dfs(root.right)
        ## return result
        #dfs(root)
        #return result

        result = []

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
            return result
        dfs(root)
        return result

    def post_order(self, root):
        # init array result
        #recursive function
        # go thorugh like an L
        #def dfs(root)
        ## if not root return None
        ## dfs(root.left)
        ## dfs(root.right)
        ## result.append(root.val)
        ## return result
        #dfs(root)
        #return result

        result = []

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)

            return result
        dfs(root)
        return result

sol = Solution()
print(f"inorder: {sol.pre_order(root)}")
print(f"inorder: {sol.in_order(root)}")
print(f"postorder: {sol.post_order(root)}")


# Iterative Pre order traversal (DFS)
def pre_order_iternative(node):
    stack = [node]
    
    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        print(node)

print(f"pre order iternative: {pre_order_iternative(root)}")


