# Q1. Calculate Array Sum

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

total = 0
for x in arr:
    total += x

print("Sum:", total)
