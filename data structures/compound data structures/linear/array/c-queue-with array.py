#done by:- sai manideep manga
#date   :- 12th august 2021
class cqueue:
    def __init__(self,n):
        self.n=n
        self.q=[]
        self.top=-1
        self.rear=-1

    def enqueue(self,data):
        #starting  or empty queue
        if front==-1 and rear==-1:
            self.top=self.rear=0
            self.q[self.rear]=data

        #when queue is full
        elif (self.rear+1)%(self.n) == self.top:
            print("queue over flow")
        # when the queue is empty from either rear end or front end
        else:
            self.rear=(self.rear+1)%(self.n)
            self.q[self.rear]=data

    def dequeue(self):
        if self.top==-1 and self.rear==-1:
            print("queue underflow")#if the queue is empty
        #queue is empty
        elif self.top==self.rear:
            self.top = self.rear=-1
        #queue may have empty elements
        else:
            print("popped element is: ",self.q[self.top])
            self.top=(self.top+1)%self.n

    def display(self):
        print(self.q)

#driver code
max_len_queue=int(input("enter the max length of circular queue: "))
print("enter the operations\n 1. for enqueue\n 2. for dequeue\n 3. display the queue\n 4. to end the operations")
queue=cqueue(max_len_queue)
while(1):
    n=int(input("enter the opeartion to be done: "))
    if n==1:
        queue.enqueue(int(input()))
    if n==2:
        queue.dequeue()
    if n==3:
        queue.display()
    if n==4:
        break