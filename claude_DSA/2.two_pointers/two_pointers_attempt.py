def find_pair_fast(nums: list, target):
    nums.sort()
    # init two pointers
    # left = 0
    # right = len(num) -1

    left = 0
    right = len(nums) -1

    while left < right: # this is when i know when to stop as means left has iterated throughout
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return [0,0]
    return [0,0]

nums = [1, 3, 5, 7, 2] # care as you need to perform sort!!!
print(find_pair_fast(nums, 12))