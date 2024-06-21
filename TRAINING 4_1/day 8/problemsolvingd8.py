#[3,2,4,1,1,6,7,2,2,4,1,8]
#list has duplicate val,
# op : 3 2 4 1
#      1 6 7 2
#      2 4 1 8
#convert 1d list into 2d list

'''
def repeat_nl(lst):
    seen = set()
    for i in lst:
        if i in seen:
            print()
            seen.clear() 
            print(i,end=' ')
        else:
            print(i,end=' ')
        seen.add(i)

lst = [1,2,3,4,1,2,3,1,2]
list1 = [2,3,1,3,4,3,2]
list2 = [4,5,2,1]
repeat_nl(lst)
print()
repeat_nl(list1)
print()
repeat_nl(list2)

#2nd method
a = list(map(int,input().split(" ")))
m = []
c = 0
while(c!=len(a)):
    r = []
    for i in range(len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in r):
                c = c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)
'''

'''
#ip:
"the quick brown fox jumps over the lazy dog"
check whether all 26 alphabets are present in this
op: yes
'''
'''
dictionary is almost the same as set....:)
x = input()
k = set()
for i in x:
    if i.isalpha():  
        k.add(i.lower())  
if len(k) == 26:
    print("yes")
else:
    print("no")
'''

'''
a = input()
d = [0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))
'''

'''
write len of longest sub-string w/o repeating characters
'''

'''
x = input()
d = {}
maxi = 0
start = 0

for i in range(len(x)):
    if (x[i] in d and d[x[i]]>=start):
        start = d[x[i]] + 1
    d[x[i]] = i
    maxi = max(maxi,i-start + 1)
print(maxi)
'''

x = input()
d = {}
m = 0
s = ""
i = 0
while(i < len(x)):
    while(i < len(x)):
        if(x[i] not in s):
            s = s + x[i]
            d[s[i]] = i
        else:
            if(len(s) > m):
                m = len(s)
            s = ""
            break
        i = i+1
    i = d[s[i]] + 1
print(m)


    
        

        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        
        
        

