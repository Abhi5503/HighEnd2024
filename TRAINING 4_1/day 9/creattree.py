class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root=None
        
    def creat(self,root,x):
        if(root==None):
            self.root=node(x)
        elif(root.data>x):
            if root.left is None:
                root.left = node(x)
            else:
                self.creat(root.left,x)
        else:
            if root.right is None:
                root.right = node(x)
            else:
                self.creat(root.right,x)
            
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
            
    def preorder(self,root):
        if root:
            print(root.data, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end = " ")
             
    def sumnodes(self,root):
        if (root==None):
            return 0
        else:
            return root.data + (self.sumnodes(root.left) + self.sumnodes(root.right))
            
    def sumeven(self,root):
        if root==None:
            return 0
        s = 0
        if root.data % 2 == 0:
            s += root.data
        s += self.sumeven(root.left) + self.sumeven(root.right)
        return s
    
    def sumodd(self,root):
        if root==None:
            return 0
        s = 0
        if root.data % 2 != 0:
            s += root.data
        s += self.sumodd(root.left) + self.sumodd(root.right)
        return s
    
    def diffeo(self,root):
        if root == None:
            return 0
        evensum = self.sumeven(root)
        oddsum = self.sumodd(root)
        return abs(evensum - oddsum)
    
    def height(self,root):
        if root==None:
            return -1
        ht = 0
        if root:
            l = self.height(root.left)
            r = self.height(root.right)
            ht = max(l,r)+1
        return ht
    
    def balancebt(self, root):
        if root is None:
            return "balanced" 
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left-right) <= 1:
            return "balanced"
        return "not balanced"
    
    def leafnodes(self,root):
        if (root.left==None and root.right==None):
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    
    def sumofleaf(self,root):
        if(root.left==None and root.right==None):
            return root.data
        return self.sumofleaf(root.left)+self.sumofleaf(root.right)
         
    def depth(self,root,y,c):
        if(root==None):
            return -1
        if(root.data==y):
            return c
        if(root.data>y):
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
        
    
    def search(self,root,x):
        if root is None:
            return False
        if root.data==x:
            return True
        return self.search(root.left,x) or self.search(root.right,x)
        
 
t1 = tree()
t1.creat(t1.root,10)
t1.creat(t1.root,5)
t1.creat(t1.root,15)
t1.creat(t1.root,7)
t1.creat(t1.root,3)
t1.creat(t1.root,4)
t1.creat(t1.root,1)
print("\nInorder:")
t1.inorder(t1.root)
print("\nPreorder:")
t1.preorder(t1.root)
print("\nPostorder:")
t1.postorder(t1.root)
print()
print("Sum of nodes:", t1.sumnodes(t1.root))
print("Sum of nodes in right subtree:", t1.sumnodes(t1.root.right))
print("Sum of nodes in left subtree:", t1.sumnodes(t1.root.left))
print("\nSum of even nodes:", t1.sumeven(t1.root))
print("\nSum of odd nodes:", t1.sumodd(t1.root))
print("\nDifference between sum of even and odd:", t1.diffeo(t1.root))
print("\nHeight of tree:",t1.height(t1.root))
print(t1.balancebt(t1.root))
print(t1.leafnodes(t1.root))
print(t1.sumofleaf(t1.root))
print(t1.search(t1.root,10))
print(t1.depth(t1.root,15,0))

