# Creating Dict View objects with `values()`
uptime = {
    "server1": 120,
    "server2": 98,
    "server3": 143,
    "server4": 0
}

print(uptime.values())
# returns a VIEW only object
# dict_values([120, 98, 143, 0])

# To aggregate we fetched the values since they are more meaningful

values = uptime.values()

print(f"max value: {max(values)}")
print(f"min value: {min(values)}")
print(f"Total Servers (use len): {len(values)}")
print(f"Uptime using sum: {sum(values)}")
print(f"Return False if any value is 0: {all(values)}")
print(f"Return True if at least one is > 0: {any(values)}")