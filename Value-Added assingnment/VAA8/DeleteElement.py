def deleteElement(arr, index):
    if 0 <= index < len(arr):
        arr.pop(index)
    return arr

print(deleteElement([1, 2, 3, 4, 5], 2))  # Output: [1, 2, 4, 5]    