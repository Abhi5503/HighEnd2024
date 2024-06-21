#palindrome or not using recursion
'''
ip:
12321
op:


def is_palindrome(s):  
    if len(s)<=1:
        return True
    elif s[0]==s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
x = input()
print(is_palindrome(x))
'''
'''

def fun(x,re):
    if(x==0):
        return re
    re = re*10+(x%10)
    return fun(x//10,re)
n = int(input())

if(n==fun(n,0)):
    print("pal")
else:
    print("not pal")
'''

#max profit made from the given input..

'''
ip :
15 3 2 7 8 4

op:
6
---------
'''

'''
def maxprofit(n):
    curr = 0
    maxval = 0

    if:
        curr = pres - prev
    else:
        maxval = curr
    return maxprofit

k = list(map(int(),input().split(" ")))
x = maxprofit(n)
print(x)
'''

'''
def max_profit(prices):
  max_profit=0
  min_price=float('inf')  
  for p in prices:
    min_price=min(min_price, p)  
    max_prof=max(max_profit, p-min_price)  
  return max_profit
price = list(map(int,input().split(" ")))
prof = max_profit(price)
print(f"Maximum profit:",prof) 
'''

'''
ip: 5
op:
* * * * *
* 1 2 3 *
* 4 5 6 *
* 7 8 9 *
* * * * *

'''
'''
def cube_pattern(size):
    print("* " * size)
    for i in range(1, size - 1):
        row = "* "
        for j in range(1, size - 1):
            num = (i - 1) * (size - 2) + j
            row += str(num) + " "
        row += "*"
        print(row)
    print("* " * size)
cube_pattern(5)
'''


'''
ip:
4
op:

   _ _ _ _a_ _ _ _
   _ _ _a b a_ _ _ 
   _ _a b c b a_ _
   _a b c d c b a_

'''

'''  
def generate_pattern(size):
    if size < 3:
        return

    for i in range(size):
        row = "_"*(size-i)
        for j in range(i + 1):
            row+=chr(ord('a')+j)
        for j in range(i):
            row+=chr(ord('a')+i-j-1)
        row+= "_"*(size-i)
        print(row)

generate_pattern(4)
'''


    
    


