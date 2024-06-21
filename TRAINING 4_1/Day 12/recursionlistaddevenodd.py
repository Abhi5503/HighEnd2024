#l1,l2....(even and odd add..else increment)

def fun(l1,l2):
    l1 = [i for i in l1 if i%2 == 0]
    l2 = [j for j in l2 if j%2!=0]
    while(l1 and l2):
        return fun(l1[i],l2[j])+fun(l2[i]+l1[j])
l1 = [6,3,2,9,4,7]
l2 = [8,7,5,3,6,9]
print(fun(l1,l2))