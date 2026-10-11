def multiplicationTable(n, limit):
    return [n * i for i in range(1, limit + 1)]

print(multiplicationTable(5, 10)) #Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]