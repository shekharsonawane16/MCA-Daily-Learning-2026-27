def longestCommonPrefix(str):
    prefix = str[0]
    for s in str:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"