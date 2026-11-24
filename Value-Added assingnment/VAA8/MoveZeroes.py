def moveZeroes(arr):
    result = []

    for i in arr:
        if i != 0:
            result.append(i)

    for i in range(len(arr) - len(result)):
        result.append(0)

    return result

print(moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]