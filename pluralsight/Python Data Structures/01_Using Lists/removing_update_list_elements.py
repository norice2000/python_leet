# using the pop method to remove and retrieve 
timers = [300, 600, 120, 45]

cancelled = timers.pop(1)
cancelled_last = timers.pop()

print(f"Remained timeres: {timers}")
print(f"Cancelled: {cancelled}")
print(f"Cancelled last: {cancelled_last}")


# remove method

shopping_list = ["egg", "rice", "milk"]

shopping_list.remove("milk")
print(f"Update list with removed milk: {shopping_list}") # Update list with removed milk: ['egg', 'rice']

#clear() to remove the elements

# Updating elements
playlist = ["Song A", "Song B", "Song C"]

playlist[1] = "Song X"

print(f"new playlist: {playlist}") #new playlist: ['Song A', 'Song X', 'Song C']