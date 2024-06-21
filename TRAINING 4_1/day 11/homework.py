#all the paths for same start and diff ends..
def fun(d,x,e,c,m,l1=[]):
    l.append(x)
    if(x==e):
        if(c<m):
            m = c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]: 
        if i[0] not in l:
            m,l1 = fun(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
l1=[]
l=[]
w = []
d = {5: [(7, 2), (3, 3)],
     7: [(5, 2), (4, 8), (3, 5)],
     4: [(7, 8), (8, 4), (2, 1)],
     8: [(3, 6), (4, 4), (2, 7)],
     3: [(5, 3), (7, 5), (8, 6)],
     2: [(4, 1), (8, 7)]}
for i in d:
    print(fun(d,5,i,0,9999,l1))
