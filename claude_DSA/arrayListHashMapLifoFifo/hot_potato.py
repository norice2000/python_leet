from collections import deque

def hot_potato(people, step):
    queue = deque(people)
    
    while len(queue) > 1:
        # Pass the potato (move people to back)
        for i in range(step - 1): # this iterates 2 times
            queue.append(queue.popleft())
        
        # Eliminate the person holding potato, only does this once the for i loop ends with 2 iterates
        eliminated = queue.popleft()
        print(f"{eliminated} is eliminated!")
    
    return queue[0]  # Last survivor

# Test
survivors = hot_potato(["Alice", "Bob", "Charlie", "David"], 3)
print(f"Survivor: {survivors}")