class Solution:
    def replaceCharacter(self, s, oldChar, newChar):
        return s.replace(oldChar, newChar)

print(Solution().replaceCharacter("hello world", "o", "a"))  # Output: "hella warld"