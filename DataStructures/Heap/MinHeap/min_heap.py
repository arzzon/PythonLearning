'''
    This is an implementation of min heap.
'''
import copy
class minHeap(object):
    #HEAP_SIZE = 10
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.size = 0
        self.heap = [0 for i in range(self.capacity)]

    # Ensure extra capacity doubles the capacity of the heap
    def ensureExtraCapacity(self):
        if self.size == self.capacity: # If size has reached the capacity of the heap
            tempHeap = copy.deepcopy(self.heap)
            self.capacity *= 2
            self.heap = [0 for i in range(self.capacity)]
            for i in range(len(tempHeap)):
                self.heap[i] = tempHeap[i]

    # Get parent index
    def getParentIndex(self,index):
        return (index-1)//2

    # checks if parent exist
    def hasParent(self,index):
        if self.getParentIndex(index) >= 0:
            return True
        else:
            return False

    # Get the parent index
    def getParent(self,index):
        return self.heap[self.getParentIndex(index)]

    # Get left child index
    def getLeftChildIndex(self, index):
        return index * 2 + 1

    # Get right child index
    def getRightChildIndex(self,index):
        return index * 2 + 2

    # Check for left child
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size

    # Check for right child
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size

    # Get the left child
    def getLeftChild(self,index):
        return self.heap[self.getLeftChildIndex(index)]

    # Get the right child
    def getRightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]

    # Peek gets the smallest element in the heap which is always at the root in min heap
    def peek(self):
        if self.size == 0:
            raise Exception("Heap empty!")
        return self.heap[0]

    # Poll removes the smallest element from the heap and returns it
    def poll(self):
        if self.size == 0:
            raise Exception("Heap empty!")
        item = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size] # move the last element to the root
        self.heapifyDown()
        return item

    # heapifyDown helps maintain the heap property by moving the root element to it's proper location
    # It's used when we poll the minimum element from the heap, in this case we
    def heafifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            minIndex = self.getLeftChildIndex(index)
            if self.hasRightChild() and self.getRightChild(index) < self.getLeftChild(index):
                minIndex = self.getRightChildIndex(index)
            if self.heap[index] < self.heap[minIndex]:
                break
            else:
                self.swap(index,minIndex)
                index = minIndex

    # swap function swaps values present in the given indices
    def swap(self,index1,index2):
        self.heap[index1] += self.heap[index2]
        self.heap[index2] = self.heap[index1] - self.heap[index2]
        self.heap[index1] = self.heap[index1] - self.heap[index2]

    # add helps in adding new element in to the heap
    def add(self, item):
        self.ensureExtraCapacity()
        # Directly add the new element at the end of the heap then heapifyUp to put it in correct position
        self.size += 1
        self.heap[self.size] = item
        self.heapifyUp()

    # heapifyUp helps in
    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.getParent(index) > self.heap[index]:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    # displayHeap prints the heap
    def displayHeap(self):
        for i in range(self.size):
            print(self.heap[i],end=" ")
        print()

if __name__ == "__main__":
    h = minHeap()
    h.add(15)
    h.add(17)
    h.add(20)
    h.add(11)
    h.add(25)
    print(h.displayHeap())

