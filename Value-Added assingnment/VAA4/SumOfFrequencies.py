def sumOfFrequencies(arr):
    f = {}
    for x in arr:
        f[x] = f.get(x, 0) + 1
    return max(f.values()) + min(f.values())

print(sumOfFrequencies([1,2,2,3,3,3]))