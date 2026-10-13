
def findMax(nums):
    maximum = nums[0]

    for n in nums:
        if n > maximum:
            maximum = n

    return maximum

print(findMax([3, 5, 1, 8, 2]))  # Output: 8