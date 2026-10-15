
def isPalindrome(n):
    return str(n) == str(n)[::-1]

print(isPalindrome(121))  # Output: True
print(isPalindrome(123))  # Output: False