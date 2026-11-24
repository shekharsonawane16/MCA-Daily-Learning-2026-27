def rotateArray(arr, r):
    r = r % len(arr)
    return arr[-r:] + arr[:-r] if r else arr

print(rotateArray([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]