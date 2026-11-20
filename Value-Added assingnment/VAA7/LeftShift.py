def leftShift(arr, k):
    n = len(arr)

    if k >= n:
        return [0] * n

    return arr[k:] + [0] * k

print(leftShift([1, 2, 3, 4, 5], 2))
