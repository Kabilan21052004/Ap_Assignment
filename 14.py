def equivalent(str1, str2):
    def is_rotation(s1, s2):
        if len(s1) != len(s2):
            return False
        return s1 in (s2 + s2)

    longest_substring = ""
    for i in range(len(str1)):
        for j in range(i, len(str1)):
            sub1 = str1[i:j + 1]
            for k in range(len(str2)):
                for l in range(k, len(str2)):
                    sub2 = str2[k:l + 1]
                    if is_rotation(sub1, sub2):
                        if len(sub1) > len(longest_substring):
                            longest_substring = sub1
                        elif len(sub1) == len(longest_substring) and sub1 < longest_substring:
                            longest_substring = sub1

    return longest_substring

print(equivalent('hdjkou1', 'pokoudj'))  
print(equivalent('ghajior', 'abkoidj'))  
print(equivalent('hdjkou1', 'pikpiaa'))