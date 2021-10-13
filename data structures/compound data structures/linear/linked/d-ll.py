class Node:
    def __init__(self,next=None,prev=None,data=None):
        self.next=next
        self.prev=prev
        self.data=data

class Doublelinkedlist:
    def __init__(self):
        self.head=Node()
    #ways to insert a node into dll
    # 1. insert the node at starting of dll
    # 2. insert the node at end of dll
    # 3. insert the node at given position
#########################################################
    # 1. insertion of node at starting of dll
    def push(self,data):
        newnode=Node(data)

        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            newnode.data=data
            self.head.prev=newnode
            self.head=newnode

#########################################################
    # 2. insertion of element at end of d-ll
    def pushend(self,data):
        if self.head==None:
            self.head=Node()
            self.head.data=data
            return
        itr = self.head
        while(itr.next!= None):
            #findig the last node
            itr=itr.next
        newnode=Node()
        newnode.data=data
        itr.next=newnode
        newnode.prev=itr

############################################################
    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            itr=self.head
            print("forward traversal")
            while(1):
                if itr.next==None:
                    return
                print(itr.data,end=" ")
                itr=itr.next
            print()
            print("backward traversal")
            while(1):
                if itr.prev==None:
                    return
                print(itr.data,end=" ")
                itr=itr.prev

#############################################################
l=Doublelinkedlist()
l.push(1)
l.push(2)
l.push(3)
l.Display()
l.pushend(1)
l.pushend(2)
l.pushend(3)
l.pushend(4)
l.Display()