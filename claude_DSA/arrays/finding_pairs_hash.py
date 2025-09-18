def find_pair_faster(numbers, target):
    seen = {}  # Dictionary to store numbers we've seen
    
    for i, num in enumerate(numbers):
        complement = target - num  # What number would complete the pair?
        
        if complement in seen:
            return [seen[complement], i]  # Found the pair!
        
        seen[num] = i  # Remember this number and its index
    
    return None

# Test it
numbers = [2, 7, 11, 15]
target = 9
result = find_pair_faster(numbers, target)
print(f"Indices: {result}")  # Should print [0, 1]