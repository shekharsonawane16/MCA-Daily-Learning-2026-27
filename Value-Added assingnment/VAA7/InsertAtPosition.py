def insertAtPosition(arr, x, p):
    return arr[:p] + [x] + arr[p:]

print(insertAtPosition([1, 2, 3, 4, 5], 99, 2))