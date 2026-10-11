from typing import Union

def calculate(a: int, b: int, op: str) -> Union[int, float, str]:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return "Division by zero" if b == 0 else round(a / b, 2)
    if op == "//":
        return "Division by zero" if b == 0 else a // b
    if op == "%":
        return "Division by zero" if b == 0 else a % b
    if op == "**":
        return a ** b

print(calculate(10, 5, "+"))  # Output: 15
print(calculate(10, 5, "-"))  # Output: 5
print(calculate(10, 5, "*"))  # Output: 50
print(calculate(10, 5, "/"))  # Output: 2.0
print(calculate(10, 0, "/"))  # Output: Division by zero
print(calculate(10, 5, "//"))  # Output: 2
print(calculate(10, 0, "//"))  # Output: Division by zero
print(calculate(10, 5, "%"))  # Output: 0
print(calculate(10, 0, "%"))  # Output: Division by zero
print(calculate(10, 5, "**"))  # Output: 100000