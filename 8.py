def delvowels(s):
    v="aeiou"
    str01=" "
    for char in s:
        if char not in v:
            str01+=char
    return str01
A=delvowels('Paeiou')
print(A)
