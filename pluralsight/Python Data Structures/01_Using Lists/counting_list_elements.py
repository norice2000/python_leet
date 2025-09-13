statuses = ["online", "offline", "online", "error", "online"]

# Using Count methods shows you how many time something appears
count_online = statuses.count("online")
print(f"Online counter: {count_online}") #Online counter: 3


# Find the First occurence of a value, finding elements in a list
tasks_queue = ["backup", "scan", "update", "scan"]

# Get index info
first_scan = tasks_queue.index("scan")
print(f"Index position for scan: {first_scan}") #Index position for scan: 1


# Check if elements exists. use the "in" operator to find it
features = ["dark_mode", "notification"]

if "notification" in features:
    index = features.index("notification")
    print(f"Notification found! in index: {index}")

# Check if element is absent
if "SSD" not in features:
    print(f"SSD not found!")