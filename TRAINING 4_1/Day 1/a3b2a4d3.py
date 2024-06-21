#sliding window approach (logic is good ... need to display output)
x = input()
count = 1
string=''
for i in range (len(x)-1):
    if (x[i] == x[i+1]):
        count+=1
        i+=1
    else:
        string = string + x[i] + str(count)
        count = 1
        i+=1
string = string + x[-1] + str(count)
print(string)
        
        


        


        

    
    
