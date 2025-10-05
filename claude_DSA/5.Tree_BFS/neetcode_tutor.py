from collections import deque

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print(f"level: {level}")
        for i in range(len(queue)): # iterates the inner loop in each row
            current = queue.popleft()
            print(current.val)
            if current.left: # check if left child is null, take note you are popping them as node itself, even tho this may appear as a stack
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        level += 1

root = [1,2,3]
bfs(root)