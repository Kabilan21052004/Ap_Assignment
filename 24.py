def splitsum(l):
    
    return [sum(x**2 for x in l if x > 0), sum(x**3 for x in l if x < 0)]


print(splitsum([1, -2, 3, -4, 5]))  
print(splitsum([-1, -2, -3]))      
print(splitsum([1, 2, 3]))        
print(splitsum([-1, 0, 1]))         
print(splitsum([0]))                