def swapNumbers(a: int, b: int) -> list[int]:
    a, b = b, a
    return [a, b]
print("Swapping two numbers:")
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")
a, b = swapNumbers(a, b)
print(f"After swapping: a = {a}, b = {b}")