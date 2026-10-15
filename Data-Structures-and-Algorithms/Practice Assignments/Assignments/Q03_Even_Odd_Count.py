# Q3. Count Even and Odd Numbers

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

even = 0
odd = 0

for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
