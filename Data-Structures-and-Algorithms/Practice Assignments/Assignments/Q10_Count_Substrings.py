# Q10. Find All Occurrences of a Substring

text = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub == "":
    print("Substring cannot be empty.")
else:
    positions = []

    for i in range(len(text) - len(sub) + 1):
        if text[i:i + len(sub)] == sub:
            positions.append(i)

    print("Occurrences:", len(positions))
    print("Positions (starting from 0):", positions)
