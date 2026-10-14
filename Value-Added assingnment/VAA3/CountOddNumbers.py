def countOddNumbers(n, array):
    count = 0
    for num in array:
        if num % 2 != 0:
            count += 1
    return count

print(countOddNumbers(5, [1, 2, 3, 4, 5]))  # Output: 3