def shuffleArray(arr, n):
    result = []

    for i in range(n):
        result.append(arr[i])
        result.append(arr[i + n])

    return result

print(shuffleArray([2, 5, 1, 3, 4, 7], 3))  # Output: [2, 3, 5, 4, 1, 7]