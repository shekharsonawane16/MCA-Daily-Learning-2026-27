
def subtractProductAndSum(n):
    product = 1
    total = 0

    for digit in str(n):
        product *= int(digit)
        total += int(digit)

    return product - total


print(subtractProductAndSum(234)) #Output: 15
print(subtractProductAndSum(705)) #Output: -12
print(subtractProductAndSum(0)) #Output: 0
