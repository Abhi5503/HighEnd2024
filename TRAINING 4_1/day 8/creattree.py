class node:
    def __init__(self):
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if(root==None):
            self.root=node(x)
        elif(root.data>x):
            self.creat(root.left,x)
        else:
            self.creat(root.right,x)
t1 = tree()
t1.creat(t1.root,10)
t1.creat(t1.root,5)