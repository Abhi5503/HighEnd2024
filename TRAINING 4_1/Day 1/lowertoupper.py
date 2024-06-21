x = 'abhINANdana'
k = 'abhinandana'

#print(x.lower())
res = ''
for i in x:
    if i.islower():
        res+=i.upper()
    else:
        res+=i.lower()
print(res)

vow = ''
for i in k:
    if i in 'aeiou':
        vow+=i.upper()
    else:
        vow+=i
print(vow)
