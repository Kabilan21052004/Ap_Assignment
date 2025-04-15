def checkunique(count):
    keys_to_remove = []
    for key in count.keys():
        if count[key] == 0:
            keys_to_remove.append(key)
    for i in keys_to_remove:
        del count[i]
    temp = set(count.values())
    if len(temp) == 1:
        return True
    else:
        return False


def create_count(str1):
    temp = {}
    for i in str1:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    return temp


def max_num(count):
    large = 0
    final = ''
    for i in count.keys():
        if count[i] >= large:
            large = count[i]
            final = i
    return final


def make_string(count):
    temp = ''
    for i, j in count.items():
        temp += i*j
    return temp


def remove_whole(count, k):
    keys_to_remove = []
    for i in count.keys():
        if k == count[i]:
            keys_to_remove.append(i)
    for key in keys_to_remove:
        temp = count
        del temp[key]
        if checkunique(temp):
            return temp
    return count

def reduce(low_str, k):
    if checkunique(create_count(low_str)):
        print(create_count(low_str))
        return low_str

    main_count = create_count(low_str)

    total_remove = remove_whole(main_count,k)
    print(total_remove)
    if checkunique(total_remove):
        return make_string(total_remove)
    

    temp = main_count
    for i in range(k):
        letter = max_num(temp)
        temp[letter] -= 1
    print(temp)
    if checkunique(temp):
        return make_string(temp)
    else:
        return 'none'
print("1")
print(reduce('aabbcc',0)) 

print("2")
print(reduce('aabbbcc',0)) 

print("3")
print(reduce('aabbbcc',1)) 

print("4")
print(reduce('aabbbcc',2)) 

print("5")
print(reduce('aabbbcc',3)) 

print("6")
print(reduce('aabbbcc',4)) 

print("7")
print(reduce('aabbbcc',5)) 

print("8")
print(reduce('aabbbcc',6)) 

print("1")
print(reduce('aabbbcc',7)) 

print("1")
print(reduce('aaaabbcc',4)) 