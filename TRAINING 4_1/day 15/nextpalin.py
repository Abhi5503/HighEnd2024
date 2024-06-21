'''
ip: 1212
op:if palindrome...print number, else..print next palindrome
'''
def palin(x):  
    n = str(x)
    return n == n[::-1]
def next_palin(x):
    x += 1
    while not palin(x):
        x += 1
    return x
x = int(input("Enter a num:"))
if palin(x):
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")
    print(f"Next palindrome:{next_palin(x)}")