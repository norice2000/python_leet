# Input: 
# "INFO: Server started|ERROR: Connection failed|WARNING: High memory usage|INFO: Request processed|ERROR: Database timeout"

# Output:
# {"INFO": 2, "ERROR": 2, "WARNING": 1}

def count_log_levels(log_string):

    # use split to remove |
    try:
        entries = log_string.split("|")
        # empty dictionary
        status_count = {}

        for log_str in entries:
            server_status = log_str.split(":", 1)[0] # prints INFO:Server Started, https://docs.python.org/3/tutorial/introduction.html#strings using string method
            # print(parts[0])
            # if == INFO matches incrent
            server_status = server_status.strip()

            # d[key] Return the item of d with key key. Raises a KeyError if key is not in the map.
            status_count[server_status] = status_count.get(server_status, 0) + 1
        return status_count
            
    except Exception as e:
        print(f"Unable to process {e}")
        return {}

# Test it
log_data = "INFO: Server started|ERROR: Connection failed|WARNING: High memory usage|INFO: Request processed|ERROR: Database timeout"
result = count_log_levels(log_data)
print("Final result:", result)
