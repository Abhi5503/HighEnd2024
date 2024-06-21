x = 'ffA12yytEeb$@*kl'
sp = 0
lv = 0
uv = 0
lc = 0
uc = 0
d = 0
for i in x:
    if (x.islower()):
        if (x in 'aeiou'):
            lv+=1
        else:
            lc+=1
    elif (x.isupper()):
        if (x in 'AEIOU'):
            uv+=1
        else:
            uc+=1
    elif x.isdigit():
        d+=1       
    else:
        sp+=1 # use alnum if not asked the above alpha lower digit help
print("lc:",lc)
print("uc:",uc)
print("lv:",lv)
print("uv:",uv)
print("d:",d)
print("sp:",sp)

        

    
        
    
