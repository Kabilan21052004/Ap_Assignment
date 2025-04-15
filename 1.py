def checkpalindrome(s): 
    lowercase_s=""
    for char in s:
        if "A"<= char<="Z":
            lowercase_s+=chr(ord(char)+32)
        else:
            lowercase_s+=char
    reversed_s=""
    for i in range(len(lowercase_s)-1,-1,-1):
        reversed_s+=lowercase_s[i]
    return reversed_s==lowercase_s
a="Malayalam"
print(checkpalindrome(a))

