def secondHighestOccurringElement(arr):
    f = {}
    for x in arr:
        f[x] = f.get(x, 0) + 1

    c = sorted(set(f.values()), reverse=True)
    if len(c) < 2:
        return -1

    return min(x for x in f if f[x] == c[1])

print(secondHighestOccurringElement([1,2,2,3,3,3]))