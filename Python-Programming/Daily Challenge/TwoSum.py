def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        need = target - nums[i]

        if need in seen:
            return [seen[need], i]

        seen[nums[i]] = i

print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]