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