''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of priority queue.
 *
 *  Written:       30/12/2018
 *  Last updated:  30/12/2018
 *
 *  % python priority_queue.py
 *
***************************************************************************** '''
class PriorityQueue(object):
    def __init__(self):
        self.size = 0
        self.data = [] #Data are stored in a list
    
    def enqueue(self,data,priority):
        values = [data,priority] #This should be an entry for the list
        index = 0
        while index < len(self.data): # While inserting the element we ensure that the element with the highest priority is positioned infront of that with with lowest priority
            if self.data[index][1] < priority: #Checks if we have got the correct position to insert the element
                self.data.insert(index,values)
                break
            index += 1
        if index == len(self.data): #Case where the element to be inserted has the least priority, so it has to be inserted at the end
            self.data.append(values)
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
        for ele in self.data:
            print(ele[0],end=",")
        print("\n")

    def showWithPriority(self): #Displays element along with priority
        print(self.data)

pqueue = PriorityQueue()
pqueue.enqueue('a',3)
pqueue.showWithPriority()
pqueue.enqueue('h',3)
pqueue.showWithPriority()
pqueue.enqueue('b',1)
pqueue.showWithPriority()
pqueue.enqueue('c',4)
pqueue.showWithPriority()
pqueue.enqueue('c',10)
pqueue.showWithPriority()
pqueue.enqueue('c',2)
pqueue.showWithPriority()
pqueue.dequeue()
pqueue.showWithPriority()
'''
OUTPUT:
[['a', 3]]
[['a', 3], ['h', 3]]
[['a', 3], ['h', 3], ['b', 1]]
[['c', 4], ['a', 3], ['h', 3], ['b', 1]]
[['c', 10], ['c', 4], ['a', 3], ['h', 3], ['b', 1]]
[['c', 10], ['c', 4], ['a', 3], ['h', 3], ['c', 2], ['b', 1]]
[['c', 4], ['a', 3], ['h', 3], ['c', 2], ['b', 1]]
'''