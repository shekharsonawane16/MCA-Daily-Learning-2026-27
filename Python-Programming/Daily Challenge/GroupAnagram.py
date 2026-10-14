def groupAnagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)

    return sorted([sorted(g) for g in groups.values()])

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))