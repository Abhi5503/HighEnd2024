'''
[3,5,9,6,8,10]----->[3,4,5,10,4,3]
'''
  
li = list(map(int,input().split(" ")))
count = 1
lastcount = 1
for i in range(len(li)):
    if li[i]<li[i+1]:
        count+=1
    else:
        break
for i in range(len(li)-1,-1,-1):
    if li[i]<li[i-1]:
        lastcount+=1
    else:
        break
print(count)
print(lastcount)