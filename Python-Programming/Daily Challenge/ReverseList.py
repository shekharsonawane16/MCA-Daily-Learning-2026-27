
def reverseList(nums):
    result = []

    for n in nums:
        result.insert(0, n)

    return result

print(reverseList([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]