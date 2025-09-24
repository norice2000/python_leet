# 2.2.1 Problem
# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1
# Input: [1,1,0,1,1,1]

# Output: 3

# Explanation: The first two or last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        ones = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                max_ones = max(max_ones, ones)
                ones = 0
        return max(max_ones, ones)




nums = [1,1,0,1,1,1]

solutions = Solution()
print(solutions.findMaxConsecutiveOnes(nums))