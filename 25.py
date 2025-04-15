def kMax(li,k):
    if len(li) < k or k<0:
        return False
    while k != 0:
        maxi = max(li)
        li.remove(maxi)
        k -= 1
        if k == 0:
            return maxi
print(kMax([10,2,4,5,7,9],1))

        
    