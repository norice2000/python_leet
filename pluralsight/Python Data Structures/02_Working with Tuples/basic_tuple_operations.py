#dimensions
room_1 = (3, 4)
room_2 = (3.2, 2.5)
room_3 = (4, 3.3)

#concat
concat_room = room_1 + room_2 + room_3
print(f"concat room: {concat_room}")

# Iterate a tuple
for i in concat_room:
    print(f"room: {i}") # this iterates room_1 as 3 and 3 respectively
# room: 3
# room: 4

# count and index
print(f"Counting the concat_room: {concat_room.count(3)}, and the index of it: {concat_room.index(3)}") #counts how many rooms has 3

# Checking if a specific element exists
find_size = 3.3
if find_size in concat_room:
    print("Found!")

# Aggregate functions
print(f"Max size: {max(concat_room)}")
print(f"Min size: {min(concat_room)}")
print(f"Sum of the rooms: {sum(concat_room)}")