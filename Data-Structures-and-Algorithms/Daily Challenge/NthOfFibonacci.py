def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fibonacci(10))  # Output: 55
print(fibonacci(20))  # Output: 6765