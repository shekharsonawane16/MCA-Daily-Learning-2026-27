def rightTrianglePattern(n):
    return ["*" * i for i in range(1, n + 1)]
print(rightTrianglePattern(5)) #Output: ['*', '**', '***', '****', '*****']