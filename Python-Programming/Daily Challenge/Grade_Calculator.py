def calculateGrade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(calculateGrade(95))
print(calculateGrade(82))
print(calculateGrade(58))
print(calculateGrade(110))