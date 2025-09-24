# Problem: Given a 1-indexed array of integers numbers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target. 
# Return the indices of the two numbers, 1-indexed.

def twoSum(numbers, target):
    # instantiate index numbers
    left = 0
    right = len(numbers) -1  # since we are counting indexes

    while left < right:
        current_total = numbers[left] + numbers[right]
        if current_total == target:
            return [left + 1, right + 1]
        elif current_total < target:
            left += 1
        else:
            right -= 1
        
    return None

# Test cases
print(twoSum([2,7,11,15], 9))    # Should return [1,2] (1-indexed!)
print(twoSum([2,3,4], 6))        # Should return [1,3] 
print(twoSum([-1,0], -1))        # Should return [1,2]