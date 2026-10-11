def isPalindrome(s):
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama")) #Output: True