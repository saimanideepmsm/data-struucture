# Implementation of singly linked list
# Done : Sai manideep manga
# Date : 15th aug 2021

#creating a class node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating a class linkedlist with inbuild methods
class Linkedlist:
    def __init__(self):
        self.head = None
#using this method we can push data at front of linked list
    def pushtop(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
#using this method we can push data at end of the linked list
    def pushend(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            flag=self.head
            while(1):
                if flag.next==None:
                    #print("break")
                    break
                else:
                    flag=flag.next
            newnode = Node(data)
            flag.next=newnode
# this method helps in pushing data in between two node
# we need to pass the pointer or node address in-order to insert the elements
    def pushmiddle(self,prev_node,data):
        newnode = Node(data)
        newnode.next=prev_node.next
        prev_node.next=newnode

##deletion of a node at a position
    def deletenode(self,indx):
        if self.head==None:
            print("empty list")
        temp=self.head

        if indx==0:
            self.head=temp.next
            temp=None
            return

        for i in range(indx-1):
            temp=temp.next
            if temp.next==None:
                print("list ended")
                return
        newtemp=temp.next.next
        temp.next=newtemp

# this method helps in printing the linked list
    def print(self):
        if self.head == None:
            print("empty linked list")
        else:
            itr = self.head
            lstring = ""
            while itr:
                lstring = lstring + str(itr.data) + "-->"
                itr = itr.next
            print(lstring)


#driver code
l=Linkedlist()
l.pushtop(1)
l.pushtop(2)
l.pushtop(3)
l.print()
l.pushend(50)
l.print()
l.pushmiddle(l.head.next,25)
l.print()
print("-------------")
l.deletenode(5)
l.print()