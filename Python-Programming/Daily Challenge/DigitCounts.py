class Solution:
    def digitCounts(self, n):
        return len(str(abs(n)))

print(Solution().digitCounts(12345)) #Output: 5