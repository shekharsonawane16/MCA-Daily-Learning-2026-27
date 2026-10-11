def centeredPyramidPattern(n):
    result = []
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        line = " " * spaces + "*" * stars
        result.append(line)
    return result

print(centeredPyramidPattern(5)) #Output: ['    *', '   ***', '  *****', ' *******', '*********']