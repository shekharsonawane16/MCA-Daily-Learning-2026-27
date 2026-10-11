def hollowPyramidPattern(n):
    result = []
    for i in range(1, n + 1):
        if i == n:
            result.append("*" * (2 * n - 1))
        elif i == 1:
            result.append(" " * (n - 1) + "*")
        else:
            result.append(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
    return result

print(hollowPyramidPattern(5))