def armstrongInRange(start, end):
    result = []
    for n in range(start, end + 1):
        digits = str(n)
        total = 0
        for d in digits:
            total += int(d) ** len(digits)
        if total == n:
            result.append(n)
    return result

print(armstrongInRange(100, 999)) #Output: [153, 370, 371, 407]