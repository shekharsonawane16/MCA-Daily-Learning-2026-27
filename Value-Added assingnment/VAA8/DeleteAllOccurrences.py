def deleteAllOccurrences(arr, x):
    result = []

    for i in arr:
        if i != x:
            result.append(i)

    return result

print(deleteAllOccurrences([1, 2, 3, 2, 4, 2, 5], 2))  # Output: [1, 3, 4, 5]   