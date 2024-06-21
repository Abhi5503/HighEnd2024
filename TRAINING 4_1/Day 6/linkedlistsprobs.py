#[4,8,2,4,4,8,4]
#print the number that repeats x or more times
'''
list1=list(map(int,input().split(" ")))
print(list1)
x = len(list1)//2
print(x)
max = 0
for i in list1:
    if(list1.count(i)>max):
        max = list1.count(i)
        p = i
print(p)
'''   
