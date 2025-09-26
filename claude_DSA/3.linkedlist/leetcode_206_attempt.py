# Problem: Given the head of a singly linked list, reverse the list, and return the new head.
# Visual Example
# Input:  1 → 2 → 3 → 4 → 5 → None
# Output: 5 → 4 → 3 → 2 → 1 → None

# Another Example:
# Input:  1 → 2 → None  
# Output: 2 → 1 → None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    # instantiate prev as none
    # current as head

    prev = None
    current = head

    while current:
        new_node = current.next
        current.next = prev
        prev = current
        current = new_node
    return prev

# Test helper function
def print_list(head):
    current = head
    while current:
        print(current.val, end=" → " if current.next else " → None\n")
        current = current.next
        
# Test cases
# Create: 1 → 2 → 3 → None
node1 = ListNode(1)
node2 = ListNode(2) 
node3 = ListNode(3)
node1.next = node2
node2.next = node3

print("Original:")
print_list(node1)

# Create 3 2 1 none
# node3.next = node2
# node2.next = node1

reversed_head = reverseList(node1)
print("Reversed:")
print_list(reversed_head)