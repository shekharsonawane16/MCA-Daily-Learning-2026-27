
def reverseInteger(n):
    return int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)

print(reverseInteger(123))  # Output: 321
print(reverseInteger(-456))  # Output: -654