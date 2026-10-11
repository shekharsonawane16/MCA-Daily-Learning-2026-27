# Q7. Move Zeros to the End

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

result = [x for x in arr if x != 0]
result.extend([0] * arr.count(0))

print("Array after moving zeros:", result)
