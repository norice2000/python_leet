# Scenario: Processing User Requests in Batches

# Your platform needs to handle 10,000 API requests. Instead of processing one-by-one, you batch them!

# def process_in_batches(requests, batch_size=100):
#     #split large array into smaller chunks
#     for i in range(0, len(requests), batch_size):
#         batch = requests[i:i + batch_size] # slice notation for list[start:end], slicing array
#         print(f"Processed batch {i//batch_size + 1}")

# sample_requests = [f"request_{i}" for i in range(10000)]  # 10 sample requests
# process_in_batches(sample_requests, batch_size=3)


# Platform engineering example: Batch processing API requests

def process_batch(batch):
    # mimic scenario: send to database, API, etc.
    print(f"  Processing {len(batch)} items: {batch[0]} to {batch[-1]}")

def process_in_batches(requests, batch_size=10):
    for i in range(0, len(requests), batch_size):
        batch = requests[i:i + batch_size]  # Slice the array
        # process this batch ( send to database)
        process_batch(batch)
        print(f"Processed batch {i//batch_size + 1}")

# Example: 1000 user requests
user_requests = [f"Request_{i}" for i in range(100)]
process_in_batches(user_requests)
# Processes 10 batches of 100 requests each