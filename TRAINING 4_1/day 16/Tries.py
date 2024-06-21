class Node:
    def __init__(self):
        self.d = {}  
        self.flag = 0  
        self.d1 = {}  

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root
        for i in word:
            if i not in temp.d:
                temp.d[i] = Node()
            temp = temp.d[i]
        temp.flag = 1  

    def search(self, word):
        temp = self.root
        for i in word:
            if i in temp.d:
                temp = temp.d[i]
            else:
                return False
        
        return temp.flag == 1
    
    def printprefix(self, prefix):
        temp = self.root
        for i in prefix:
            if i in temp.d:
                temp = temp.d[i]
            else:
                return False
        self.dfs(temp, prefix)

    def dfs(self,node,curr_word):
        if node.flag == 1:
            print(curr_word)
        for char, child in node.d.items():
            self.dfs(child,curr_word + char)
            
    #def lexographical():
t1 = Trie()
'''
t1.insert("hello")
t1.insert("world")
print(t1.search("world"))  
print(t1.search("hello")) 
print(t1.search("hell"))   
print(t1.search("bye"))  
'''

n = int(input())
for i in range(n):
    a,s = input().split()
    if(a=='1'):
        t1.insert(s)
    if (a=='2'):
        print(t1.search(s))
    if (a=='3'):
        print(t1.printprefix(s))