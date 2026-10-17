def numberOfSteps(num):
    steps = 0

    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1

        steps += 1

    return steps

print(numberOfSteps(14))  # Example usage: number of steps to reduce 14 to 0