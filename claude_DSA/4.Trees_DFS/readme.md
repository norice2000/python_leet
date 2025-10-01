##Trees - Linked Lists with Branches

Key difference from linked lists:

Linked List: Each node has 1 pointer → linear path
Binary Tree: Each node has 2 pointers → branching paths

### TreeNode Structure
```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    # Left child
        self.right = right  # Right child
```

Create this tree structure:
      1
     / \
    2   3
   /
  4