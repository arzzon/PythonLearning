''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of maximum heap datastructure.
 *
 *  Written:       8/1/2018
 *  Last updated:  8/1/2018
 *  
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |  bigO(-)   |  bigO(-)   |   bigO(-)  |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(-)    |  bigO(-)   |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(-)    |  bigO(-)   |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   bubbleUp    |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   bubbleDown  |    bigO(-)    |  bigO(-)   |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |    findMax    |    bigO(1)    |    bigO(1)    |    bigO(1)    |
 *  -----------------------------------------------------------------
 *
 *  % python maxheap.py
 *
***************************************************************************** '''
class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]*self.HEAP_SIZE
        self.current_position = -1

    def insert(self,item):
        if self.isFull():
            print("Heap is full!")
        else:
            self.current_position += 1
            self.heap[self.current_position] = item
            self.bubbleUp(self.current_position)

    def isFull(self):
        if self.current_position+1 == self.HEAP_SIZE:
            return True
        else:
            return False
    def isEmpty(self):
        if self.current_position == -1:
            return True
        else:
            return False

    def bubbleUp(self,pos): 
        ### Ensures that the new item inserted maintains the rule of max-heap. ###
        # pos holds the index of the item whose position has to be checked that whether it follows the rule of the max heap
        # the item in question is compared with it's parent (pos-1/2), since in max heap the parent is greater than it's children
        # the item has to be swapped with it's parent if is found to be greater than it's parent. After swapping the item moves to
        # it's parent's place, now it's position is again checked by comparing it with it's parent. For this the pos is updated as 
        # the item has moved to it's parent's place. Hence the parent index is also updated.
        if pos < 0: #Don't perform bubbleup if index becomes negative
            return
        parent_index = (pos-1)//2 #floor int value is used
        while parent_index >= 0 and self.heap[pos] >= self.heap[parent_index]:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[pos]
            self.heap[pos] = temp
            pos = parent_index
            parent_index = (pos-1)//2

    def findMax(self):
        if not self.isEmpty():
            return self.heap[0]
        else:
            print("Heap is empty!")

    def heapSort(self):
        # It works by putting the largest item in the last node in each iteration. 
        # It swaps the root node with the last node
        # 
        # 
        for i in range(self.current_position+1):
            temp = self.heap[0]
            self.heap[0] = self.heap[self.current_position-i]
            self.heap[self.current_position-i] = temp
            self.bubbleDown(self.current_position-i-1)
    
    def bubbleDown(self,pos):
        root_index = 0
        if pos<0:
            return
        while root_index < pos:
            if((2*root_index+1 <= pos) and (2*root_index+2 <= pos)): 
                if (self.heap[root_index] < self.heap[2*root_index+1]) and (self.heap[root_index] < self.heap[2*root_index+2]):
                    if self.heap[2*root_index+1] > self.heap[2*root_index+2]:
                        temp = self.heap[root_index]
                        self.heap[root_index] = self.heap[2*root_index+1]
                        self.heap[2*root_index+1] = temp
                        root_index = 2*root_index+1
                    else:
                        temp = self.heap[root_index]
                        self.heap[root_index] = self.heap[2*root_index+2]
                        self.heap[2*root_index+2] = temp
                        root_index = 2*root_index+2
                elif (self.heap[root_index] < self.heap[2*root_index+1]):
                    temp = self.heap[root_index]
                    self.heap[root_index] = self.heap[2*root_index+1]
                    self.heap[2*root_index+1] = temp
                    root_index = 2*root_index+1
                elif (self.heap[root_index] < self.heap[2*root_index+2]):
                    temp = self.heap[root_index]
                    self.heap[root_index] = self.heap[2*root_index+2]
                    self.heap[2*root_index+2] = temp
                    root_index = 2*root_index+2
                else:
                    break
            elif (2*root_index+1 <= pos):
                if self.heap[root_index] < self.heap[2*root_index+1]:
                    temp = self.heap[root_index]
                    self.heap[root_index] = self.heap[2*root_index+1]
                    self.heap[2*root_index+1] = temp
                    root_index = 2*root_index+1
                else:
                    break
            else:
                break

    def show(self):
        for i in range(self.current_position+1):
            print(self.heap[i])

heap = Heap()
heap.insert(5)
heap.insert(4)
heap.insert(10)
heap.insert(3)
heap.insert(2)
heap.insert(100)
heap.insert(12)
heap.insert(40)
heap.show()
print("Max value = ",heap.findMax())
heap.heapSort()
print("After heapsort")
heap.show()
