def rotateArray(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k > 0 else nums

print(rotateArray([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]