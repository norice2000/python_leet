from collections import deque

def printer_simulation(jobs):
    queue = deque()
    results = []

    for job in jobs:
        if job.startswith("PRINT"):
            queue.append(job)
        elif job == "PROCESS":
            if queue:
                processed = queue.popleft() # removes the front
                results.append(processed)
                print(f"Processed: {processed}")
            else:
                print('Queue is empty')
    return results

jobs = ["PRINT doc1.pdf", "PRINT doc2.pdf", "PROCESS", "PRINT doc3.pdf", "PROCESS", "PROCESS"]
printer_simulation(jobs)