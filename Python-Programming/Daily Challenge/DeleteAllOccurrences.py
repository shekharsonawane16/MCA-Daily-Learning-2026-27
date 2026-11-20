def deleteAllOccurrences(arr, X):
    result = []

    for num in arr:
        if num != X:
            result.append(num)

    while len(result) < len(arr):
        result.append(0)

    return result

print(deleteAllOccurrences([1, 2, 3, 2, 4], 2))  # Output: [1, 3, 4, 0, 0]