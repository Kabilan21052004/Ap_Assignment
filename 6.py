def distchart(str1,str2):
    req_string=""
    for char in str1:
        if char not in str2:
            req_string+=char
    return req_string
B=distchart('orange','apples')
print(B)