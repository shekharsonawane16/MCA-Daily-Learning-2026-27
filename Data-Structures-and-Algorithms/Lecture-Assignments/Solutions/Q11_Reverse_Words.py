# Q11. Reverse Words in a Sentence
# Example: the sky is blue -> eht yks si eulb

sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

print("Reversed words:", " ".join(reversed_words))
