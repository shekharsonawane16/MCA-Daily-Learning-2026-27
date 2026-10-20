def numberOfSteps(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        count += 1
    return count

print(numberOfSteps(14))  # Output: 6 14-> 7->6->3->2->1->0
print(numberOfSteps(8))   # Output: 4 8->4->2->1->0
print(numberOfSteps(123)) # Output: 12 123->122->61->60->30->15->14->7->6->3->2->1->0