x = input()

for i in x:
    if len(x) >= 8 and x.isalnum() and (x!= x.isdigit() and x.isalnum()):
        print("Good Password")
    else:
        for i in len(x):
            if (len(x)<8):
                print(8-len(x))
            if x.isalnum() and (not x.isalnum()) and x.isupper() and x.islower()):
                
