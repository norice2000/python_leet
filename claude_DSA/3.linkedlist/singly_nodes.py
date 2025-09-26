class SinglyNodes():
    def __init__(self, value, next=None):
        self.value = value
        self.next= next

    def __str__(self): #prints the output instead of the Object type
        return str(self.value)

# Instantiated nodes
Head = SinglyNodes(1)
node_a = SinglyNodes(3)
node_b = SinglyNodes(4)
node_c = SinglyNodes(7)

# link the singly nodes
Head.next = node_a
node_a.next = node_b
node_b.next = node_c

#print
print(Head) #outputs: 1

# to print them all we need to traverse the list them
current = Head
while current:
    print(current)
    current = current.next
# Outputs
# 1
# 3
# 4
# 7

# Display link list 
def display(head):
    current = head
    elements = []

    while current:
        elements.append(str(current.value))
        current = current.next
    print(' -> '.join(elements))

print(display(Head))

# Search for a node value
def search(head, value):
    current = head
    while current:
        if value == current.value:
            return True
        current = current.next
    return False

print(search(Head, 7))