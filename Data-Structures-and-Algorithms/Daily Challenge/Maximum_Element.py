def findMax(nums):
    largest =nums[0]
    for n in nums:
        if n>largest:
            largest=n
    return largest

print(findMax([1, 5, 3, 9, 2]))
print(findMax([-10, -3, -20, -1]))
print(findMax([42]))