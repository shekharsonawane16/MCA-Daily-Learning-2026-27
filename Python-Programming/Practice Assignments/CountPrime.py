
def countPrimes(n):
    count = 0

    for num in range(2, n + 1):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            count += 1

    return count

print(countPrimes(10))  # Output: 4 (2,3,5,7 are prime numbers)