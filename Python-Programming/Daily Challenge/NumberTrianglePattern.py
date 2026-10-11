def numberTrianglePattern(n):
    return [" ".join(str(i) for i in range(1, row + 1)) for row in range(1, n + 1)]

print(numberTrianglePattern(5)) #Output: ['1', '1 2', '1 2 3', '1 2 3 4', '1 2 3 4 5']