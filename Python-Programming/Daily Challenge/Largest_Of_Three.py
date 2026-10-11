def largestOfThree(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


print(largestOfThree(10, 25, 15))
print(largestOfThree(-5, -2, -10))
print(largestOfThree(7, 7, 3))