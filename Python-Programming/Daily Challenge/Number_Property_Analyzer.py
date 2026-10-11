
def analyzeNumber(n):
    prime = n > 1

    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    return {
        "is_even": n % 2 == 0,
        "is_positive": n > 0,
        "is_prime": prime,
        "is_perfect_square": n >= 0 and int(n ** 0.5) ** 2 == n,
        "digit_count": len(str(abs(n)))
    }


print(analyzeNumber(25))
print(analyzeNumber(7))
print(analyzeNumber(-16))
