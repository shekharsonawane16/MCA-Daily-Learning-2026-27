
def isArmstrong(n):
    digits = str(n)
    total = sum(int(d) ** len(digits) for d in digits)
    return total == n

print(isArmstrong(153))  # Output: True