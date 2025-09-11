instruments = ["guitar", "piano", "drums"]

for instrument in instruments:
    print(f"instrument: {instrument}")

# instrument: guitar
# instrument: piano
# instrument: drums


# Using enumerate() to look with index and value
item = ["mouse", "keyboard", "monitor"]

for index, key in enumerate(item):
    print(f"Index: {index + 1}, Item: {key}") # we have to increment index since it starts at 0

#outputs
# Index: 1, Item: mouse
# Index: 2, Item: keyboard
# Index: 3, Item: monitor

# cleaner version of enumerate(, 1) where the 1 represents the starting digit
for i, k in enumerate(item, 1):
    print(f"Index enum: {i}, item: {k}")

# Index enum: 1, item: mouse
# Index enum: 2, item: keyboard
# Index enum: 3, item: monitor