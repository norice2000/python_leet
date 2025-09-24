class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return str(self.value)
    
# Instantiate Nodes
head = tail = DoublyNode(1)
# print(head) #outputs 1
# print(tail) #outputs 1

# display by creating list
def display(head):
    current = head
    elements = []

    while current:
        elements.append(str(current.value))
        current = current.next
    print(' <->'.join(elements))

display(head)


# Insert value at the beginning of the node
def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value, next=head) #reassign the new node where it will be the nead
    head.prev = new_node # assign 1 as previous
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)

def insert_end(head, tail, value):
    new_node = DoublyNode(value, prev=tail)
    tail.next = new_node
    return new_node, head

head, tail = insert_end(head, tail, 7)
display(head)