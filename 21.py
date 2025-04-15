def moveZeros(li):
    count = 0
    ans = []
    for terms in li:
        if terms == 0:
            count +=1 
        else:
            ans.append(terms)
    return ans + [0]*count
print(moveZeros([1,2,0,4,0,5,0]))
        