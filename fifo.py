from collections import deque

my_queue = deque()

# Adding elements (enqueue)
my_queue.append("First")
my_queue.append("Second")
my_queue.append("Third")

print(my_queue) # Output: deque(['First', 'Second', 'Third'])

# Removing elements (dequeue)
first_item = my_queue.popleft()
print(first_item) # Output: First

print(my_queue) # Output: deque(['Second', 'Third'])

second_item = my_queue.popleft()
print(second_item)
print(my_queue)

# output
# deque(['First', 'Second', 'Third'])
# First
# deque(['Second', 'Third'])
# Second
# deque(['Third'])