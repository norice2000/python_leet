# Create a linked list that represents: Apples → Bananas → Carrots → None
# Linked list nodes are memory address
 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Your mission: Create and connect these nodes!
# Step 1: Create three separate nodes
apple_node = ListNode("Apples")
banana_node = ListNode("Bananas")
carrot_node = ListNode("Carrots")

# Step 2: Connect them with arrows
# apple_node should point to banana_node
# banana_node should point to carrot_node  
# carrot_node should point to None
apple_node.next = banana_node
banana_node.next = carrot_node

# Step 3: Test your linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" → " if current.next else " → None\n")
        current = current.next

print_list(apple_node)  # Should print: Apples → Bananas → Carrots → None

# Find a value (searching)
def find_node(head, target):
    current = head
    while current:
        if current.val == target:
            return current # found it
        current = current.next
    return None #not found

print(find_node(apple_node, "Bananas"))

# Append front
def add_to_front(head, new_val):
    new_node = ListNode(new_val)
    new_node.next = head
    return new_node

new_head = add_to_front(apple_node, "Milk")
print_list(new_head)  # Should print: Milk → Apples → Bananas → Carrots → None

# short notation
# def add_to_front(head, new_val):
#     return ListNode(new_val, head) #val=new_val, next=head