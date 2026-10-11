# Q4. Search an Element

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter number to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position:", i + 1)
        found = True

if not found:
    print("Element is not present in the array.")
