def highestOccurringElement(nums):
    return min(set(nums), key=lambda x: (-nums.count(x), x))
print(highestOccurringElement([1,2,2,2,3,3]))