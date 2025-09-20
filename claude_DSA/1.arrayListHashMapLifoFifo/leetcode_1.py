# Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
# Examples
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1] (because nums[0] + nums[1] = 2 + 7 = 9)

# Input: nums = [3,2,4], target = 6  
# Output: [1,2] (because nums[1] + nums[2] = 2 + 4 = 6)

# Input: nums = [3,3], target = 6
# Output: [0,1] (because nums[0] + nums[1] = 3 + 3 = 6)

def two_sum(nums, target):

    # seen = {}
    # for index, num in enumerate(nums):
    # complement = target - num
    # if complement in seen:
    #    return [seen[complement], index]
    # seen[num] = index  # should create {2: 0}
    #return None

    seen = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return None
# Test your solution  
print(two_sum([2,7,11,15], 9))   # Should return [0,1]
print(two_sum([3,2,4], 6))       # Should return [1,2]
print(two_sum([3,3], 6))         # Should return [0,1]