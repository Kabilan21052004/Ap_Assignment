def separate(s):
    if len(s) == 0:
        return []

    result = []
    current_group = s[0]

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_group += s[i]
        else:
            result.append(current_group)
            current_group = s[i]

    result.append(current_group)
    return result

print(separate("cartoon"))
print(separate("network"))   
print(separate("aabbcc"))   
print(separate("cccbbbaaa")) 
