class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    
def visit_all_nodes_preorder(root):
    if root:
        print(f"Visiting Node Pre Order: {root.val}")
        visit_all_nodes_preorder(root.left)
        visit_all_nodes_preorder(root.right)

def visit_all_nodes_inorder(root):
    if root:
        visit_all_nodes_inorder(root.left)
        print(f"Middle node: {root.val}")
        visit_all_nodes_inorder(root.right)

def visit_all_nodes_postorder(root):
    if root:
        visit_all_nodes_postorder(root.left)
        visit_all_nodes_postorder(root.right)
        print(f"Post order: {root.val}")

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

root.left = node2
root.right = node3
node2.left = node4

visit_all_nodes_preorder(root)
visit_all_nodes_inorder(root)
visit_all_nodes_postorder(root)