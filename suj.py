class Node:
    def __init__(self,key=None):
        self.val=key
        self.left=None
        self.right=None

class bst: 
    def __init__(self,root=None):
        self.root=root
    
    def insert(self,key):
        if self.root==None:
            self.root=Node(key)
        elif self.root==key:
            pass
        else:
            prev=None
            temp=self.root
            while temp!=None:
                prev=temp
                if temp.val>key:

                    temp=temp.left
                else:
                    temp=temp.right
            if prev.val>key:
                prev.left=Node(key)
            if prev.val<key:
                prev.right=Node(key)
                
    def inorder(root):
        if root:
            bst.inorder(root.left)
            print(root.val)
            bst.inorder(root.right)
    
    def inorder(self,root):
        if self.root:




p=bst(20)


             


