def countVowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print(countVowels("Hello, World!")) #Output: 3