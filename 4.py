class UpperCaseException(Exception):
    pass

def evenIndexCapital(s):
    lowercase_s = ""
    for char in s:
        if 'A' <= char <= 'Z':
            lowercase_s += chr(ord(char) + 32)  
        else:
            lowercase_s += char

    result = ""
    length = 0
    for _ in lowercase_s:
        length += 1

    i = 0
    while i < length:
        if i % 2 == 0:
            result += chr(ord(lowercase_s[i]) - 32)  
        else:
            result += lowercase_s[i]
        i += 1

    return result

# Test cases
print(evenIndexCapital("school")) 
print(evenIndexCapital("ScHool"))   
