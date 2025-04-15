class InvalidInputException(Exception):
    pass

def change(s):
    red_count = 0
    green_count = 0
    for char in s:
        if char == 'R':
            red_count += 1
        elif char == 'G':
            green_count += 1
        else:
            raise InvalidInputException("Contains invalid character")
    return min(red_count, green_count)

str1 = change("RGGR")  
print(str1)
