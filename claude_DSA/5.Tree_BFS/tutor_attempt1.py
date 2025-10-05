from collections import deque
# Step 1: Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Step 2: Helper function to build a tree
def build_tree():
    # """
    # Build this tree:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    # """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def bfs(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []

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

# Build the tree
tree = build_tree()

# Example 1: BFS with detailed steps
print(bfs(tree)) # [[1], [2, 3], [4, 5, 6]]