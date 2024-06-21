#recursions..
#add even numbers in list1, and odd numbers in list2..
'''
def sumevenodd(x, seven, sodd):
    if x == len(list1):
        return seven, sodd
    if list1[x] % 2 == 0:
        seven += list1[x]
    if list2[x] % 2 != 0:
        sodd += list2[x]
    return sumevenodd(x + 1, seven, sodd)

list1 = [3,8,5,4,3]
list2 = [5,0,9,3,2]

seven, sodd = sumevenodd(0,0,0)
print("Sum of even numbers in list1:",seven)
print("Sum of odd numbers in list2:",sodd)
'''
#sum of even numbers in given input
'''
def seven(n, esum=0):
    if n < 0:
        return esum
    if n % 2 == 0:
        esum += n
    return seven(n - 1, esum)

res = seven(9)
print("Sum of even numbers under given input value:", res)
'''








    
    
