def floydsTriangle(n):
    result = []
    num = 1

    for i in range(1, n + 1):
        line = ""
        for j in range(i):
            line += str(num) + " "
            num += 1
        result.append(line.strip())

    return result

print(floydsTriangle(5)) #Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']