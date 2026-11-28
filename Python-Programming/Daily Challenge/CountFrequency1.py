def countFrequency(arr: List[int]) -> List[int]:
    freq = [0] * 101

    for i in arr:
        freq[i - 900] += 1

    return freq