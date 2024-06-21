def coin(li,n):
    l1 = [0]*(n+1)
    l1[0]=0
    for i in li:
        for j in range(1,n+1):
            if(j>=i):
                if(l1[j-i]!=1):
                    if(l1[j]!=1):
                        l1[j] = 1
                    else:
                        l1[j] = l1[j-i]+1
    return 1
                        
li = [2,3,5,6]
n = 11
print(coin(li,n))