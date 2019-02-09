''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of stack.
 *
 *  Written:       30/12/2018
 *  Last updated:  30/12/2018
 *
 *  % python stack.py
 *
***************************************************************************** '''
class Stack(object):
    def __init__(self):
        self.size = 0
        self.data = [] #data are stored in a list
    
    def push(self,value):
        self.data.append(value) #Values are appended at the end of the list
        self.size += 1
    
    def pop(self):
        if self.size <= 0:
            print("Stack is empty!")
        else:
            self.data.pop(-1) #Removes the value from the end of the list
            self.size -= 1

    def peek(self):
        return self.data[-1] #Returns the value from the end of the list

    def show(self):
        print(self.data)

stack = Stack()
stack.push(1)
stack.show()
stack.push(2)
stack.show()
stack.push(3)
stack.show()
stack.push(4)
stack.show()
stack.peek()
stack.pop()
stack.pop()
print(stack.peek())
stack.show()