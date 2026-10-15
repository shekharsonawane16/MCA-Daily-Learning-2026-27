def isArmstrong(n):
    digits = str(n)
    total = 0
    for d in digits:
        total += int(d) ** len(digits)
    return total == n

print(isArmstrong(153))# TRUE