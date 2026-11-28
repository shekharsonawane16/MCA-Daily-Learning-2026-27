def countFrequency(arr):
    freq = [0] * 101

    for i in arr:
        freq[i - 900] += 1

    return freq