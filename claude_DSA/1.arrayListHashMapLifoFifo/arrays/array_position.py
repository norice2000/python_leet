def find_smallest_index(numbers):
    smallest_index = 0  # Start assuming first position has smallest
    
    # We need to check each position, not just each number
    for i in range(len(numbers)):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i
    
    return smallest_index

# Test it
numbers = [3, 7, 2, 9, 1]
result = find_smallest_index(numbers)
print(f"Smallest number is at index {result}")  # Should say index 4
print(f"The number there is {numbers[result]}")  # Should say 1

# What if we want to know WHERE the smallest number is, not just what it is?

def find_largest_index(numbers):
    largest_index = 0

    for i in range(len(numbers)): # this prings the length as indexes
        if numbers[i] > numbers[largest_index]: # checks index 0 is > index 0 (largest_index) and keeps comparing the index values till it appends
            largest_index = i
    return largest_index


numbers = [3, 7, 2, 9, 1]
result = find_largest_index(numbers)
print(f"Largest number is at index {result}")  # Should say index 3
print(f"The number there is {numbers[result]}")  # Should say 9