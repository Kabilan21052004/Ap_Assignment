def extraDup(li):
    freq_count = {}
    for terms in li:
        if terms not in freq_count:
            freq_count[terms] = 1
        else:
            freq_count[terms] += 1
    ans = []
    for terms in freq_count:
        if freq_count[terms] > 1:
            ans.append(terms)
    return ans
print(extraDup([10,20,30,20,20,30,40,50,-20,60,60,-20,-20]))