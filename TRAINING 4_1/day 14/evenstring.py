'''
ip: tu5g2k1h8
    g5g8gd6h3
    
op: 865312
'''

x = 'tu5g2k1h8'
y = 'g5g8gd6h3'
s = set()
for i in x:
    for j in y:
        if i.isdigit():
            s.add(i)
        if j.isdigit():
            s.add(j)
s = list(s)
s.sort()
for i in range(len(s)):
    if int(s[i])%2==0:
        s[i],s[-1]=s[-1],s[i]
        break
print(s)
k = len(s)-1
fl = s[:k]
fl.sort()
fl = fl[::-1]
fl.append(s[-1])
print(''.join(fl))