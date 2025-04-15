def subPali(strng):
    def expand_around_center(left, right):
        while left >= 0 and right < len(strng) and strng[left] == strng[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_length = 0
    for i in range(len(strng)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_length = max(max_length, len1, len2)

    return max_length


print(subPali('bbbabebabdfb'))  
print(subPali('abcdefg'))   
