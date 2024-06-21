#convert khoor to hello...
'''
def convert_khoor_hello(x,s):
    text = ""
    for i in x:
        if i.isalpha():
            unicode = ord(i)
            value_shift = unicode - s
            if value_shift < ord('a'):
                    value_shift += 26
            text += chr(value_shift)
        else:
            text += i  
    return text

y = input()
k = int(input())
x = convert_khoor_hello(y,k)
print(x)

'''

#print the length of longest substring which has alphabets in sequence

'''
x = 'xyzabcdefklmnopqrstuvefgh'

def longest_continuous_substr(s):
    maxlen = 0
    curr_len = 1
    for i in range(1,len(s)):
        if ord(s[i]) == ord(s[i-1]) + 1:
            curr_len += 1
        else:
            if curr_len > maxlen:
                maxlen = curr_len
            curr_len = 1  
    
    if curr_len > maxlen:
        maxlen = curr_len
    
    return maxlen

print(longest_continuous_substr(x))

'''

'''

the string must consist values that are each one from given input strings
ip:3
xyz
pqr
abc
'yraxpazr'

op:
yes

ip:4
abcd
wxyz
pqrs
klmn
'armxbyqn'

op:no

'''
'''
n = int(input())
m = []
for i in range(n):
    m.append(input())

s = input()
for i in range(len(s)):
    if (s[i] not in m[i%n]):
        print("no")
        break
else:
    print("yes")
'''

"no repetititons and also follows sequence"
'''

def can_form_string_from_substrings(n, substrings, s):
    
    seen_chars = set()
    
    for i in range(len(s)):
        current_substring = substrings[i % n]
        current_char = s[i]
        
        if current_char not in current_substring:
            return "no"
    
        if current_char in seen_chars:
            return "no"
        
        seen_chars.add(current_char)
    
    return "yes"

n = int(input())
substrings = []
for _ in range(n):
    substrings.append(input())
s = input()
print(can_form_string_from_substrings(n, substrings, s))
'''
'''
#part 2
n = int(input())
m = []
for i in range(n):
    m.append(list(input()))
s = input()
f=0
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        f = 1
        break
    else:
        m[i].remove(s[i])
if (f==0):
    print("yes")

'''

