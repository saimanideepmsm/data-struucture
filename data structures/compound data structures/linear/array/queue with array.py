#done by:- sai manideep manga
#date   :- 11th august 2021
#what is an queue
# A queues is a linear data structure which operates on principle of FIRST IN FIRST OUT
#FIFO
#in this chapter we shall complete implementation of queues using list

#OPERATIONS ON QUEUES
# 1. It has two variables or pointers which hold the front end address and rear end address
# we shall access data using indexes
# 2. push or insert :- we shall add the elements at the rear end if array or queue
# 3. pop or delete  :- we shall delete the elements only at front end of array or queue

# class to define an queue
class Queue:
    def __init__(self,maxlen):
        self.queue=[]
        self.maxlen=maxlen
        self.top=-1
        self.rear=-1

    def enqueue(self,data):
        if len(self.queue)>=self.maxlen:
            print("queue overflow")
        else:
            self.queue.append(data)

    def dequeue(self):  #poping the starting  element
        if len(self.queue)==0:
            print("queue underflow")
        else:
            del(self.queue[0])

    def display(self):
        print(self.queue)


#driver code
max=int(input("enter the max length of queue : "))
#creating an instance of class Queue
q=Queue(max)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
#displaying the elements in queue
q.display()
#deleting the elements from front end
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()