def firstLetters(s):
    result = ""
    length = 0
    for _ in s:
        length += 1

    if length == 0:
        return result

    if s[0] != ' ':
        result += s[0]

    i = 1
    while i < length:
        if s[i - 1] == ' ' and s[i] != ' ':
            result += s[i]
        i += 1

    return result

# Test cases
print(firstLetters("bad is nice"))       
print(firstLetters("hello other world"))  
