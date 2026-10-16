
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        v = [s.count(c) for c in vowels]
        c = [s.count(ch) for ch in set(s) if ch not in vowels]
        return max(v + [0]) + max(c + [0])

print(Solution().maxFreqSum("hello"))  # Output: 2 (1 vowel 'e' and 1 consonant 'l') 