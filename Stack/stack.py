class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        if self.stack==[]:
            print("Stack is empty")
        else:
            print(self.stack.pop(),"is removed from the Stack")
    def traverse(self):
        print(self.stack,"  Top of Stack:",self.stack[-1])

a=Stack() #object of Stack
a.push('First')
a.push('Second')
a.push('Third')
a.push('Fourth')
a.push('Fifth')
a.traverse()
a.pop()
a.traverse()

'''  
#This code can be used to get user input for Stack      
inp=input("Do you want to use Stack ? ('y' for YES and 'n' for NO)")
a=Stack()
while (inp=="y" or inp=="Y"):
    x=input("What you want to do? (push,pop or traverse)")
    if x=='push':
        data=input("Enter the value to be pushed to stack: ")
        a.push(data)
    elif x=='pop':
        a.pop()
    elif x=='traverse':
        a.traverse()
    else:
        print("you did not provide proper purpose value(push,pop or traverse) ")
    inp=input("Do you want to use Stack ? ('y' for YES and 'n' for NO)")
'''
