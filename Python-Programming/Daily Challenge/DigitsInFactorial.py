
def digitsInFactorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return len(str(fact))

print(digitsInFactorial(5))  # Output: 3 (since 5! = 120, which has 3 digits)