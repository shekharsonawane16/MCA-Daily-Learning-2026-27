def primesInRange(start, end):
    primes = []
    for n in range(start, end + 1):
        if n > 1:
            prime = True
            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break
            if prime:
                primes.append(n)
    return primes

print(primesInRange(10, 50)) #Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]