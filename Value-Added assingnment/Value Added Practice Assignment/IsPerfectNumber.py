
def isPerfectNumber(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

print(isPerfectNumber(6))  # Output: True