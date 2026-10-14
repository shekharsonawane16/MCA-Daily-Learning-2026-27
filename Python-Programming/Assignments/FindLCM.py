
def findLcm(n1, n2):
    a, b = n1, n2

    while b:
        a, b = b, a % b

    return (n1 * n2) // a

print(findLcm(4, 6))  # Output: 12 