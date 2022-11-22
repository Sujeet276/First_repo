class node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

class linked_list:
    def __init__(self,head=None):
        self.head=head



    def create(self,var):
        if self.head==None:
            self.head=node(var)
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=node(var)
            del p
    
    def show(self):
        p=self.head
        while p!=None:
            print(p.val,end=",")
            p=p.next
        print()
        
    def insert_at_beginning(self,var):
        if self.head==None:
            self.head=node(var)
        else:
            p=node(var)
            p.next=self.head
            self.head=p
            p=None
        
    def insert_at_end(self,var):
        if self.head==None:
            self.head=node(var)
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=node(var)
            del p

    def delete_at_begin(self):
        if self.head==None:
            pass
        elif self.head.next==None:
            head=None
        else:
            self.head=self.head.next

    def delete_at_end(self):
        if self.head==None:
            pass
        elif self.head.next==None:
            head=None
        else:
            p=self.head
            q=None
            while p.next!=None:
                q=p
                p=p.next
            q.next=None
            p=None
            q=None        
    
s=linked_list()
for i in range(int(input("create number of node : "))):
    s.create(int(input()))
s.show()
s.insert_at_beginning(22)
s.show()
s.insert_at_end(44)
s.show()
s.delete_at_begin()
s.show()
s.delete_at_end()
s.show()
