x = int(input())
y = int(input())
a=[]
for i in range(y):
    b=[]
    for j in range(x):
        b.append("_")
    a.append(b)
print(a)
#path(x,y)

def fun(i,j,c):
    if(i<0 or i>=n or j>=n or j<0 or (i==k and j==l)):
        return
    if(i==m-1 and j==n-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,c,a)
    if((i-1,j) not in vi):
        c=fun(i,j-1,c,a)
    if((i-1,j) not in vi):
        c=fun(i+1,j,c,a)
    if((i-1,j) not in vi):
        c=fun(i,j+1,c,a)
    vi.pop()
    return c
x = int(input())
y = int(input())
a=[]
for i in range(y):
    b=[]
    for j in range(x):
        b.append("_")
    a.append(b)
print(a)