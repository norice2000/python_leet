from collections import deque
import time

def process_task(task):
    print(f"Processing task: {task}")
    time.sleep(0.2)

# Creating bounded deque with maxlen
# so if you it mandates maxlen it can accept, so that means task1 is removed
task_queue = deque(["task1", "task2", "task3"], maxlen=2)
print(task_queue)
# Processing task: task2
# Processing task: task3

while task_queue:
    process_task(task_queue.popleft())


