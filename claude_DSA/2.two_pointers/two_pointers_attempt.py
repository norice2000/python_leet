def find_pair_fast(nums, target):
    
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if target == total:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return None
nums = [1, 3, 5, 7] # care as you need to perform sort!!!

print(find_pair_fast(nums, 12))