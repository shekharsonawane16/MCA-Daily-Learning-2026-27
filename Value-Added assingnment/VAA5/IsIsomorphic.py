def isIsomorphic(s, t):
    return len(set(s)) == len(set(t)) and len(set(zip(s, t))) == len(set(s))

print(isIsomorphic("egg", "add"))  # Output: True
print(isIsomorphic("foo", "bar"))  # Output: False