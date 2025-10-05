class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

from collections import deque

# brute force method, see how it looks like DFS preorder

def bfs(root):
    queue = deque()

    if not root:
        return []
    
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        # check children
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

root = [3,9,20,null,null,15,7]
