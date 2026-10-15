# Q5. Reverse the Array Without Changing the Original Array

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)
print("Reversed array:", arr[::-1])
