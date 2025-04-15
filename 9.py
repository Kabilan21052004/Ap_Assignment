def moveDups(s):
    seen = []
    dups = []

    for i in range(len(s)):
        char = s[i]
        already_seen = False

        for j in range(len(seen)):
            if seen[j] == char:
                already_seen = True
                break

        if already_seen:
            dups.append(char)
        else:
            seen.append(char)

    result = []
    for i in range(len(seen)):
        result.append(seen[i])
    
    if len(dups) > 0:
        result.append('_')
        for i in range(len(dups)):
            result.append(dups[i])

    final = ''
    for i in range(len(result)):
        final += result[i]
    
    return final

print(moveDups("cartoon"))
print(moveDups("network"))
print(moveDups("aabbcc"))
print(moveDups("cccbaaa"))
