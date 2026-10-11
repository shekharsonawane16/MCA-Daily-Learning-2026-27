def sumUpToN(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sumUpToN(10)) #Output: 55
print(sumUpToN(123)) #Output: 7626