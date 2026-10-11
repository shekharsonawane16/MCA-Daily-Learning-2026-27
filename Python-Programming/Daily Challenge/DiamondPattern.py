def diamondPattern(n):
    result = []
    k = (n + 1) // 2

    for i in range(1, k + 1):
        result.append(" " * (k - i) + "*" * (2 * i - 1))

    for i in range(k - 1, 0, -1):
        result.append(" " * (k - i) + "*" * (2 * i - 1))

    return result

print(diamondPattern(5)) #Output: ['  *', ' ***', '*****', ' ***', '  *']