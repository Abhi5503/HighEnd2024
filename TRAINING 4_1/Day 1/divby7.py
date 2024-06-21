#count of numbers divisible by 7 in an inclusive range
'''
k=[]
for i in range(300,401):
    if i%7==0:
        k.append(i)
print(k)
print(len(k))

x = (401-300)//7
y = (300/7)-(400/7)
print(x,y)
'''

#print prime...if not prime print the next nearest prime
#recursion...
'''
x = int(input())
while(1):
    c=0
    for i in range (2,(x//2)+1):
        if (x%i == 0):
            c+=1
            break # break because we need not use all the other values if the number breaks at 2/3
    if (c==0):
        print(x)
        break
    else:
        x = x+1

 '''
#no of digits in prime
'''
x = input()
c=0
while(x):
    if(x%10 in [2,3,5,7]):
        c=c+1
    x=x//10
print(c)
'''




        
    
        
        


        
        
        
        

    
