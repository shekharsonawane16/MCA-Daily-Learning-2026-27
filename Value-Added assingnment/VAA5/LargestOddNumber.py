def largestOddNumber(s):
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 != 0:
            return int(s[:i + 1])
    return ""

print(largestOddNumber("123456"))  # Output: 12345