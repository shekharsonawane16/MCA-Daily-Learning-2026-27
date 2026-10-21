def countFreq(n, k):
    result = []
    for i in range(10):
        if str(n).count(str(i)) >= k:
            result.append(i)
    return result

print(countFreq(1223334444, 2))  # Example usage [2, 3, 4]