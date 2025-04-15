def minIndexFirstString(str1, str2):
    max_index = -1  
    i = 0  
    for char in str1:
        for j in range(len(str2)):
            if char == str2[j]:  
                max_index = i  
                break  
        i += 1  
    return max_index

print(minIndexFirstString("tiger", "integer"))  
print(minIndexFirstString("integer", "tiger"))  
print(minIndexFirstString("abc", "xyz"))        
