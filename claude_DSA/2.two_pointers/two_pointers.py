# think of a array that is num = [1, 2, 3, 4, 5], where:
# left = num[0]
# right = num[-1]
# and then they eventually come together as they compare as the sequence follows
# left = num[1]
# right = num[-2]
# then they meet together and stop the two point
# left = num[2]
# right = num[-3]
# hence referred to as two points, remember this as SQUEEZE, where both ends try to squeeze to each ohter

def find_pair_fast(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# nums = [2, 7, 11, 15]
# print(find_pair_fast(nums, 9))
nums = [1, 3, 5, 7]
print(find_pair_fast(nums, 8))