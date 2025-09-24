# Problem: Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.
# Examples:
# Input: 1 → 2 → 3 → 4 → 5 → None
# Output: 3 → 4 → 5 → None (return node with value 3)

# Input: 1 → 2 → 3 → 4 → 5 → 6 → None  
# Output: 4 → 5 → 6 → None (return node with value 4, the second middle)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # traverse the nodes to count
    current = head
    length = 0

    while current:
        length += 1
        current = current.next

    half_length = length // 2

    # start beginning
    current = head
    for i in range(half_length):
        current = current.next
    return current


# Test case
# Create: 1 → 2 → 3 → 4 → 5 → None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4) 
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = middleNode(node1)
print(f"Middle node value: {result.val}")  # Should print 3