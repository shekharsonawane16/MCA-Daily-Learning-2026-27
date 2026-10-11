
def classifyTriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"

    x, y, z = sorted([a, b, c])

    if x*x + y*y == z*z:
        return "Right Scalene"
    return "Scalene"


print(classifyTriangle(5, 5, 5))
print(classifyTriangle(3, 4, 5))
print(classifyTriangle(1, 2, 3))
print(classifyTriangle(5, 5, 8))
