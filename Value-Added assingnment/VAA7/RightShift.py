def rightShift(arr, k):
    n = len(arr)

    if k >= n:
        return [0] * n

    return [0] * k + arr[:n-k]


result = rightShift([10, 20, 30, 40, 50], 2)
print(result)