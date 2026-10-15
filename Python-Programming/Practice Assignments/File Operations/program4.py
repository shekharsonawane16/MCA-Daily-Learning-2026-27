
# Program 4: Count total and unique words

with open("words.txt", "w") as f:
    f.write("Python is easy and Python is powerful")

with open("words.txt", "r") as f:
    words = f.read().split()

print("Words:", words)
print("Total words:", len(words))
print("Unique words:", sorted(set(words)))
