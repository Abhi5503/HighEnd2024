class Node:
    def __init__(self, u):
        self.data = u
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def addfront(self, x):
        t = Node(x)
        t.next = self.head
        self.head = t

    def addback(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = new_node

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end="->")
            t = t.next
        print("None")  # To indicate the end of the list
        print()

    def linearsearch(self,x):
        t = self.head
        while(t!=None):
            if(t.data == x):
                return "found"
            else:
                return "not found"

    def findmiddle(self): #using fast and slow pointer
        s = self.head
        f = self.head
        while(f!=None and f.next!=None):
            s = s.next
            f = f.next.next
        return s.data

    def findmiddle1(self): # O(n)
        t = self.head
        c=0
        while(t!=None):
            c+=1
            t=t.next
        c = c//2
        t = self.head
        for i in range(c):
            t = t.next
        print(t.data)

    #write a method to find len is even or odd(O(n/2))
    def lenofll(self):
        s = self.head
        f = self.head
        while(f!=None and f.next!=None):
            s = s.next
            f = f.next.next
        if (f.next==None):
            return "Odd"
        else:
            return "Even"

    #length of continuous longest substring
    def longestsub(self):
        t = self.head
        c = 1
        m = 1
        while(t.next!=None):
            if (t.data == t.next.data-1):
                c+=1
            else:
                if(c>m):
                    m=c
                c = 1
            t = t.next
        if(c>m):
            m = c
        return m

    #find the pairs
    def pairs(self):
        t = self.head
        while(t.next!=None):
            t1 = t.next
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t = t.next

    def bubblesort(self):
        t = self.head
        while(t.next!=None):
             t1 = t.next
             while(t1!=None):
                 if (t.data>t1.data):
                     t.data,t1.data = t1.data,t.data
                 t1 = t1.next
             t=t.next

    def bubble(self): #optimised
        c = 0
        t = self.head
        p = None
        while(t.next!=None):
            f = 0
            t1 = self.head
            while(t1.next!=p):
                if(t1.data>t1.next.data):
                    f = 1
                    t1.data,t1.next.data = t1.next.data,t1.data
                t1 = t1.next
                c = c + 1
            if(f == 0):
                break
            p = t1
            t = t.next
        print(c)
                
            
l1 = SLL()
l1.head = Node(22)
l1.addback(21)
l1.addback(20)
l1.addback(23)
l1.addback(50)
l1.addback(49)
l1.addback(57)
l1.addback(56)
l1.addfront(19)
print(l1.linearsearch(75))
print(l1.findmiddle())
print(l1.findmiddle1())
print(l1.lenofll())
print(l1.longestsub())
#print(l1.pairs())
#l1.bubblesort()
l1.display()
l1.bubble()
l1.display()
