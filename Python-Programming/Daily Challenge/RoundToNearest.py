
def roundToNearest(s):
    n = int(s)
    return n // 10 * 10 + (10 if n % 10 > 5 else 0)

print(roundToNearest(23))  # Output: 20
print(roundToNearest(25))  # Output: 30