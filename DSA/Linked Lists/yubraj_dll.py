class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.start=None
        self.end=None

    def creation(self,val):
        newnode=Node(val)
        # newnode.next=None
        # newnode.prev=None
        self.start=newnode
        self.end=newnode
        print("DLL has been created")
    
        

    def insertion(self,value):#only from start
        newnode=Node(value)
        newnode.next=self.start
        self.start.prev=newnode#without creation self.star is null so it throw an error since None.prev is not quite right
        self.start=newnode
    def traverse(self):
        tmp=self.start
        if self.start==None:
            print("linked list is empty")
            return
        else:
            while tmp is not None: 
                print(tmp.value)
                tmp=tmp.next

    def deletion(self):#only from start
        tmp=self.start
        if self.start==None:
            print("can't delete empty linked list")
            return
        else:
            self.start=tmp.next
            print("deleted item is ",tmp.value)
            del tmp

    def search(self):
        pass    


s=DLL()
s.creation(20)
s.insertion(50)
s.insertion(60)
s.traverse()
s.deletion()
s.traverse()

#BST AVL merge sort , radix sort 

