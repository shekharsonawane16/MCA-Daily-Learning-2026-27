class Solution:
    def moveZeroes(self, nums):
        nums.sort(key=lambda x: x == 0)

nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)