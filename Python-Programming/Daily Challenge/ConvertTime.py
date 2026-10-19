def convertTime(day, hours, minutes):
    if day < 1 or hours < 0 or hours >= 24 or minutes < 0 or minutes >= 60:
        return [-1, -1, -1]

    total = hours * 60 + minutes + 570
    return [day + total // 1440, (total // 60) % 24, total % 60]

print(convertTime(15,10,45)) 
