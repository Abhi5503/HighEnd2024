x = list(map(int, input().split(" ")))
y = []

for i in x:
    if (i not in y):
        y.append(i)
for i in y:
    print(i,"-",x.count(i))

        
