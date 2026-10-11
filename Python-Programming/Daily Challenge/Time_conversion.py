
def convertSeconds(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


print(convertSeconds(3661))
print(convertSeconds(60))
print(convertSeconds(0))
