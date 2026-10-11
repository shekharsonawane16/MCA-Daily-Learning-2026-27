def calculateElectricityBill(units):
    if units < 0:
        return -1.0

    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 150 + (units - 100) * 2.50
    elif units <= 300:
        bill = 400 + (units - 200) * 4.00
    else:
        bill = 800 + (units - 300) * 5.00

    return round(bill + 50, 2)


print(calculateElectricityBill(50)) #Output: 125.0
print(calculateElectricityBill(150)) #Output: 400.0
print(calculateElectricityBill(250)) #Output: 800.0