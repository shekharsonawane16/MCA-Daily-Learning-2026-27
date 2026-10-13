
def secondLargest(nums):
    nums = sorted(set(nums))
    return nums[-2] if len(nums) > 1 else -1

print(secondLargest([10,20,30])) #