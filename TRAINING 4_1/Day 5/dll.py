class node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def display(self):
        t = self.head
        while(t!=None):
            print(t.data,end="->")
            t = t.next
        print()

    def rev_display(self):
        t = self.tail
        while(t!=None):
            print(t.data,end="<-")
            t = t.prev
        print()
                
    def addback(self,x):
        if(self.head==None):
            self.head = node(x)
            self.tail = self.head
        else:
            t = node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail = self.tail.next
            
    def addfront(self, x):
        n = node(x)
        if (self.head==None):
            self.head = n
            self.tail = self.head
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def linearsearch(self,x):
        t = self.head
        k = self.tail
        while(t!=None and k!=None and t!=k):
            if(t.data == x ):
                return "found"
            if (k.data == x):
                return "found"
            t = t.next
            k = k.prev
        if(t==k and t!=None and t==x): 
            return "found"
        else:
            return "not found"

    def len_dll(self):
        h = self.head
        t = self.tail
        while(h!=t and h.next!=t):
            h = h.next
            t = t.prev
        if h == t:
            return "odd"
        else:
            return "even"

    def palin_dll(self):
        h = self.head
        t = self.tail
        while (h!=None and t!=None):
            if (h.data != t.data):
                return "not palindrome"
            h = h.next
            t = t.prev
            if (h == t) or (h.prev == t):
                break
        return "palindrome"

    def halfsplit(self):
        h = self.head
        t = self.head
        while(t!=None):
            t = t.next.next
            h = h.next
        temp = h
        temp1 = h
        while(temp1!=None):
            temp.data,temp1.data = temp1.data,temp.data
            temp1 = temp1.next
            temp = temp.next
            
l1 = dll()
l1.addback(15)
l1.addfront(25)
l1.addback(17)
l1.addfront(15)
l1.addfront(17)
l1.display()
l1.rev_display()
print(l1.linearsearch(66))
print(l1.len_dll())
print(l1.palin_dll())
l1.halfsplit()