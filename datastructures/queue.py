''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of queue.
 *
 *  Written:       30/12/2018
 *  Last updated:  30/12/2018
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |    enqueue    |    bigO(1)    |     bigO(1)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |    dequeue    |    bigO(1)    |     bigO(1)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |     show      |    bigO(n)    |     bigO(n)   |    bigO(n)    |
 *  -----------------------------------------------------------------
 *  |     peek      |    bigO(1)    |     bigO(1)   |    bigO(1)    |
 *  -----------------------------------------------------------------
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
        if self.isEmpty():
            print("Queue is empty!")
        else:
            self.size -= 1
            return self.data.pop(0) #Data is removed from the start of the list

    def peek(self):
        return self.data[0] #Returns data from the start of the list

    def show(self):
        print(self.data)

    def isEmpty(self):
        if self.size <= 0:
            return True
        else:
            return False

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