#strings..
#M==F-->0, M>F-->M, F>M--->F
x = input()
Mc = 0
Fc = 0
for i in x:
    if i == 'M':
        Mc+=1
    else:
        Fc+=1
if Mc == Fc:
    print("0")
elif Mc > Fc:
    print("M",Mc)
else:
    print("F",Fc)
    
