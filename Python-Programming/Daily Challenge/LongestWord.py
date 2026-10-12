def longestWord(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longestWord("The quick browns fox jumps over the lazy dog."))