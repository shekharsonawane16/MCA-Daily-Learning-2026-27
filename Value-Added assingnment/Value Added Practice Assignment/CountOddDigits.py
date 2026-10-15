
def countOddDigits(n):
    count = 0
    for d in str(n):
        if int(d) % 2 != 0:
            count += 1
    return count

print(countOddDigits(12345))  # Output: 3
print(countOddDigits(2468))   # Output: 0