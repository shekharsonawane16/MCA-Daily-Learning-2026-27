def countFreq(n):
    return [str(n).count(str(i)) for i in range(10)]

print(countFreq(1223334444))  # Example usage [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]