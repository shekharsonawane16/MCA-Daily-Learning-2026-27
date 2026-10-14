def maxSubArray(nums):
    current = nums[0]
    maximum = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        maximum = max(maximum, current)

    return maximum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6