
def subtractProductAndSum(n):
    product = 1
    total = 0

    for digit in str(n):
        product *= int(digit)
        total += int(digit)

    return product - total


print(subtractProductAndSum(234))
print(subtractProductAndSum(705))
print(subtractProductAndSum(0))
