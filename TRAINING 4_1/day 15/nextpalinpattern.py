x = list(map(int,input().split(" ")))
k = len(x)//2
l = x[:k]
r = x[k:]
print(l)
print(r)
if (l==l[::-1]):
    print(l+l[::-1])
else:
    l[-1]+=1
    m = l+l[::-1]
    print(m)