'''
list1 = []
list2 = []
list1 = list(map(int,input().split(" ")))
list2 = list(map(int,input().split(" ")))

print(sorted(list1+list2))
'''

list1 = list(map(int,input().split(" ")))
list2 = list(map(int,input().split(" ")))

listconcat = []
i,j = 0,0

while(i<len(list1) and j<len(list2)):
    if (list1[i]<list2[j]):
        listconcat.append(list1[i])
        i+=1
    else:
        listconcat.append(list2[j])
        j+=1
while(j<len(list2)):
    listconcat.append(list2[j])
    j+=1
while(i<len(list1)):
    listconcat.append(list1[i])
    i+=1

print(listconcat)
        

