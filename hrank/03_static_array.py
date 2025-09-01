# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length <= capacity:
        arr[length] = n
        print(f" Inserted: {n} at position: {length}")
    else:
        print(f"✗ Cannot insert {n}. Array is full!")

# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
# def removeEnd(arr, length):
#     if length > 0:
#         # Overwrite last element with some default value.
#         # We would also the length to decreased by 1.
#         arr[length - 1] = 0

# # Insert n into index i after shifting elements to the right.
# # Assuming i is a valid index and arr is not full.
# def insertMiddle(arr, i, n, length):
#     # Shift starting from the end to i.
#     for index in range(length - 1, i - 1, -1):
#         arr[index + 1] = arr[index]
    
#     # Insert at i
#     arr[i] = n

# # Remove value at index i before shifting elements to the left.
# # Assuming i is a valid index.
# def removeMiddle(arr, i, length):
#     # Shift starting from i + 1 to end.
#     for index in range(i + 1, length):
#         arr[index - 1] = arr[index]
#     # No need to 'remove' arr[i], since we already shifted

def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])


# # Test 1: Normal insertion
# print("=== TEST 1: Normal Insertion ===")
# # Create a static array (simulate with Python list)
capacity = 6
arr = [0] * capacity  # [0, 0, 0, 0, 0, 0]
length = 0  # Currently empty

print("Initial array:")
printArr(arr, capacity)

# Insert some values
insertEnd(arr, 10, length, capacity)
length += 1  # Important: Update length after insertion!

insertEnd(arr, 20, length, capacity) 
length += 1

insertEnd(arr, 30, length, capacity)
length += 1

print(f"After insertions (length = {length}):")
printArr(arr, capacity)

# print("\n=== TEST 2: Test Array Full ===")
# # Fill remaining spots
# insertEnd(arr, 40, length, capacity); length += 1
# insertEnd(arr, 50, length, capacity); length += 1  
# insertEnd(arr, 60, length, capacity); length += 1

# print(f"Array full (length = {length}):")
# printArr(arr, capacity)

# # Try to insert when full - this should fail!
# insertEnd(arr, 99, length, capacity)
# print("Length is still:", length)

# print("\n=== KEY INSIGHT ===")
# print(f"Capacity: {capacity} (never changes)")
# print(f"Length: {length} (tracks actual elements)")
# print(f"Next insertion would go at index: {length}")
# print("But length equals capacity, so no room!")