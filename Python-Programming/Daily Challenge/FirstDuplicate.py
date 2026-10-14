def firstDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return -1

print(firstDuplicate([2, 1, 3, 5, 3, 2]))  # Output: 3