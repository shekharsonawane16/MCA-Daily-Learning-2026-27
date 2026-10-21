def anagram(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

print(anagram(123, 321))  # Example usage True
