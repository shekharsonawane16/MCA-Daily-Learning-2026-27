
# Program 3: Find the longest word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest = max(words, key=len)
    print("Words:", words)
    print("Longest word:", longest)
else:
    print("No words entered.")
