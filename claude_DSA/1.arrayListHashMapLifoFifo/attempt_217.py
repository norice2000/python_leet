# Problem: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true (1 appears twice)

# Input: nums = [1,2,3,4] 
# Output: false (all unique)

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true (many duplicates)

def containsDuplicate(nums: list) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test your solution
print(containsDuplicate([1,2,3,1]))        # Should return True
print(containsDuplicate([1,2,3,4]))        # Should return False  
print(containsDuplicate([1,1,1,3,3,4]))    # Should return True