#[(1,3)(2,5)(4,6)(6,7)(5,8)(7,9)]
#[5,6,5,4,11,2]

def fun(l1, p):
    if len(l1) != len(p):
        return 0  
    n = len(p)
    wt = p.copy()  
    l1.sort(key=lambda x: x[1])
    
    for i in range(1, n):
        for j in range(0, i):
            if l1[j][1] <= l1[i][0]:  
                wt[i] = max(wt[i], wt[j] + p[i])
    return max(wt)
l1 = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
p = [5, 6, 5, 4, 11, 2]

print(fun(l1, p))

