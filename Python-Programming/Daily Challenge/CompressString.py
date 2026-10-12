def compressString(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    if s:
        result += s[-1] + str(count)

    if len(result) < len(s):
        return result
    return s

print(compressString("aaabbbcc"))# a3b3c2