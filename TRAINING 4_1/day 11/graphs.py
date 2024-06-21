def fun(d,n,l=[],w = []):
    l.append(n)
    
    if n == 2:
        print("Path:",l)
        print("Cost:",sum(w))
        l.pop()
        if w:
            w.pop()
        return 
    for i,j in d[n]:
        if i not in l:
            w.append(j)
            fun(d,i,l,w)
    l.pop()
    if w:
        w.pop()
l =[]
w=[]
d = {5: [(7, 2), (3, 3)],
     7: [(5, 2), (4, 8), (3, 5)],
     4: [(7, 8), (8, 4), (2, 1)],
     8: [(3, 6), (4, 4), (2, 7)],
     3: [(5, 3), (7, 5), (8, 6)],
     2: [(4, 1), (8, 7)]}

fun(d,5,l,w)
