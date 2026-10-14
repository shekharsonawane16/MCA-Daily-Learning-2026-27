
# Program 1: Count vowels in a file

with open("vowels.txt", "w") as f:
    f.write("Hello World")

with open("vowels.txt", "r") as f:
    text = f.read()

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("File content:", text)
print("Total vowels:", count)
