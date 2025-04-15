def delDup(s):
    freq_count = {}
    for terms in s:
        if terms not in freq_count:
            freq_count[terms] = 1
        else:
            freq_count[terms] += 1
    s = list(freq_count)
    return s
print(delDup([10,20,30,20,20,30,40,50,-20,60,60,-20,-20]))