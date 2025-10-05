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

# Step 3: BFS with detailed step-by-step explanation
def bfs_with_steps(root):
    if not root:
        return []
    
    print("=== BFS STEP-BY-STEP VISUALIZATION ===\n")
    
    queue = deque([root])
    result = []
    step = 1
    
    print(f"Initial: queue = [{root.val}]\n")
    
    while queue:
        # Show current queue state
        queue_values = [node.val for node in queue]
        print(f"Step {step}:")
        print(f"  Queue before processing: {queue_values}")
        
        # Process front node
        node = queue.popleft()
        result.append(node.val)
        print(f"  → Dequeue and process: {node.val}")
        
        # Add children to queue
        children_added = []
        if node.left:
            queue.append(node.left)
            children_added.append(f"left child ({node.left.val})")
        if node.right:
            queue.append(node.right)
            children_added.append(f"right child ({node.right.val})")
        
        if children_added:
            print(f"  → Enqueue: {', '.join(children_added)}")
        
        queue_values = [node.val for node in queue]
        print(f"  Queue after processing: {queue_values}")
        print(f"  Result so far: {result}\n")
        
        step += 1
    
    print(f"FINAL RESULT: {result}")
    return result

# Step 4: Simple BFS (clean version)
def bfs_simple(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Step 5: BFS Level by Level (returns nested lists)
def bfs_level_order(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []

    
    while queue:
        level_size = len(queue)  # Number of nodes at current level, # tells us how many nodes we need to go through in the current level
        current_level = []
        
        for _ in range(level_size):  # Process all nodes at this level
            node = queue.popleft()
            current_level.append(node.val) #temporarily hold the value in the current level
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Run all examples
if __name__ == "__main__":
    # Build the tree
    tree = build_tree()
    
    # Example 1: BFS with detailed steps
    bfs_with_steps(tree)
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Simple BFS output
    print("Simple BFS (single list):", bfs_simple(tree))
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Level order (nested lists)
    print("Level Order (by levels):", bfs_level_order(tree))