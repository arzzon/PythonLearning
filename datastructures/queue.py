''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of queue.
 *
 *  Written:       30/12/2018
 *  Last updated:  30/12/2018
 *
 *  % python queue.py
 *
***************************************************************************** '''
class Queue(object):
    def __init__(self):
        self.size = 0
        self.data = [] #Data are stored in a list
    
    def enqueue(self,data):
        self.data.append(data) #Data is appended to the end of the list
        self.size += 1

    def dequeue(self):
        if self.size <= 0:
            print("Queue is empty!")
        else:
            self.data.pop(0) #Data is removed from the start of the list
            self.size -= 1

    def peek(self):
        return self.data[0] #Returns data from the start of the list

    def show(self):
        print(self.data)

queue = Queue()
queue.enqueue(1)
queue.show()
queue.enqueue(2)
queue.show()
queue.enqueue(3)
queue.show()
queue.enqueue(4)
queue.show()
queue.peek()
queue.dequeue()
queue.dequeue()
print(queue.peek())
queue.show()