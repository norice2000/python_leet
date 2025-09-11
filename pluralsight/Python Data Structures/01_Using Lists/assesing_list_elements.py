# create list with list = []

notifications = ["Updates available", "New message", "Battery low", "Backup completed"]

print(f"First notification: {notifications[0]}")
print(f"First notification: {notifications[-1]}")
print(f"Using len method of last of the lists: {len(notifications) - 1}") #this outputs 3, which is index 3, this is an alternative way of doing it


meeting = ["Team sync", "Client call", "Project review"]

try:
    print(f"Meeting: {meeting[3]}")
except IndexError:
    print(f"Error:")