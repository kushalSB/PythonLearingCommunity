class Node:

    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next

a=Node("1")
b=Node("2")
c=Node("3")

a.next=b
b.next=c

class SLL:
    def __init__(self):
        self.start=None



x=SLL()
x.start=a

# x.start.next=b

# B.x = x
#Create Primitive operations for DLL Insertion Deletion Traveresal FindMax SearchValue

