
def reverseInteger(x):
    sign = -1 if x < 0 else 1
    rev = int(str(abs(x))[::-1]) * sign

    if rev < -2147483648 or rev > 2147483647:
        return 0

    return rev


print(reverseInteger(123)) #Output: 321
print(reverseInteger(-123)) #Output: -321
print(reverseInteger(120)) #Output: 21
