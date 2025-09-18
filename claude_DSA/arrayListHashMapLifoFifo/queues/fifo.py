from collections import deque

queue = deque()

# add to back of line (enqueue)
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")
print(queue)

# FIFO
first_person = queue.popleft() # Alice gets served first fifo
print(first_person)
print(queue)

# Why use deque instead of regular list? Because list.pop(0) is slow - it has to shift all elements. deque.popleft() is instant!

# Stack (LIFO): Last in, First out
stack = []
stack.append(1); stack.append(2); stack.append(3)
print(stack.pop())  # 3 (last one added)

# Queue (FIFO): First in, First out  
queue = deque()
queue.append(1); queue.append(2); queue.append(3)
print(queue.popleft())  # 1 (first one added)