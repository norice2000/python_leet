def find_pair_that_adds_to_target(numbers, target):
    # We'll check every possible pair
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # Start j after i to avoid duplicates
            if numbers[i] + numbers[j] == target:
                return [i, j]  # Return the indices of the pair
    
    return None  # No pair found

# Test it
numbers = [2, 7, 11, 15]
target = 9
result = find_pair_that_adds_to_target(numbers, target)
print(f"Indices: {result}")  # Should print [0, 1] 
print(f"Numbers: {numbers[result[0]]} + {numbers[result[1]]} = {target}")