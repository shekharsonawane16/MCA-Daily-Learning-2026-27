# Q6. Remove Duplicate Elements

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

print("Array without duplicates:", unique)
