def insertZero(arr):
    result = []

    for i in arr:
        result.append(i)
        result.append(0)

    return result

print(insertZero([1, 2, 3, 4, 5]))  # Output: [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]