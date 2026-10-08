# Q12. Find Longest and Shortest Words

sentence = input("Enter a sentence: ")
words = sentence.split()

if not words:
    print("No words entered.")
else:
    longest = max(words, key=len)
    shortest = min(words, key=len)

    print("Longest word:", longest)
    print("Shortest word:", shortest)
