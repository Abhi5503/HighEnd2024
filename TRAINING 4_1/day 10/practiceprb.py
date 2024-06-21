'''
x = list(map(int,input().split(" ")))
s = []
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n//2)+1):
        if n%i==0:
            return False
    return True
for i in range(len(x)-1):
    k = 0
    c = 0
    for j in range(x[i],x[i+1]):
        if prime(j):
            c = j
    k = max(c,k)
    s.append(c)
print(s)
print(sum(s))
'''
'''
ip : 4 9 8 2 14 3 5 6
iterations:
4 8 9 2 14 3 5 6
  2 8 9 14 3 5 6
    8 9 14 3 5 6
      3 9 14 5 6
        5 9 14 6
          6 9 14
op: 4 2 8 3 5 6 9 14
'''
'''
def asc(li):
    n = len(li)
    for i in range(len(li)-2):
        if li[i]>li[i+1]:
            li[i],li[i+1] = li[i+1],li[i]
        if li[i+1]>li[i+2]:
            li[i+1],li[i+2] = li[i+2],li[i+1]
        if li[i]>li[i+1]:
            li[i],li[i+1] = li[i+1],li[i]
    return li
s = list(map(int,input().split(" ")))
sort3 = asc(s)
print(sort3)
'''

'''
ip:"hello:5438,car:214,book:8799,apple:2187"
op: len:5..,len 3(not present)..2,len(4)> put X....,len(5)...2;
oaXp
'''

st=list(map(str,input().split(",")))
d={}
for i in range(len(st)):
    r=st[i].split(":")
    d[r[0]]=int(r[1])
emp=""
for k,v in d.items():
    length=len(k)
    ep=list(map(int,str(v)))
    print(ep)
    if length in ep:
        emp = emp + str(k)[length - 1]
        print(emp)
    else:
        while length != 0:
            if length in ep:
                emp = emp + str(k)[length - 1]
                print(emp)
                break
            else:
                length -= 1
        if length==0:
            emp=emp+"x"
            print(emp)
print(emp)

