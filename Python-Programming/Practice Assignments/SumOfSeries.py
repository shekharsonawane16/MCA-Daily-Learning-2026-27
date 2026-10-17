def sumOfSeries(n, a, d):
    last = a + (n - 1) * d
    return n * (a + last) // 2

print(sumOfSeries(5, 2, 3))  # Example usage: sum of first 5 terms of the series starting with 2 and common difference 3