def isAnagram(s, t):
    return sorted(s) == sorted(t)

print(isAnagram("listen", "silent"))  # Output: True
print(isAnagram("hello", "world"))    # Output: False