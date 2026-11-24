def duplicateZeros(arr):
    result = []

    for i in arr:
        result.append(i)
        if i == 0:
            result.append(0)

    return result[:len(arr)]

print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))  # Output: [1, 0, 0, 2, 3, 0, 0, 4]