#done by:- sai manideep manga
#date   :- 11th august 2021
#stacks work on principle of LAST IN FIRST OUT
#LIFO
#operations that an be done on stacks are
#push elements at last
#pop delete element at last
#peek show the elements in stack

#lets implement stacks using lists,objects and classes

class Stack:
    def __init__(self):
        self.list=[]
        self.top=-1

    def isempty(self):
        if len(self.list)==0:
            return 1
        else:
            return 0

    def push(self,data):
        self.list.append(data)
        self.top+=1

    def pop(self):
        if self.isempty():
            print("stack underflow")
        else:
            self.list.pop()
            self.top-=1

    def peek(self):
        return self.list[-1]

stack = Stack()
#pushing elements into stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
#displaying last element of stack
print(stack.peek())
#popping out the elements
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()