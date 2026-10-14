
# Program 2: Read lines from a file

lines = [
    "Python is easy.\n",
    "Files store data.\n",
    "Lists store values.\n",
    "Close files after use.\n"
]

with open("lines.txt", "w") as f:
    f.writelines(lines)

with open("lines.txt", "r") as f:
    lines = f.readlines()

print("Total lines:", len(lines))
print("2nd line:", lines[1].strip())
print("4th line:", lines[3].strip())
