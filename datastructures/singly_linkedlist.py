''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of singly linkedlist.
 *
 *  Written:       23/12/2018
 *  Last updated:  23/12/2018
 *
 *  % python linkedlist.py
 *
***************************************************************************** '''
class Node(object):
    #value
    #nextNode
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.start = None
        self.size = 0 
    def insertStart(self,data):
        newNode = Node(data)
        self.size += 1
        if self.start == None: #needs to improve
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode

    def insertEnd(self,data):
        newNode = Node(data)
        self.size += 1
        if self.start == None:
            self.start = newNode
        else:
            previousNode = self.start
            while previousNode.next != None:
                previousNode = previousNode.next
            previousNode.next = newNode

    def insert(self,data,position):
        newNode = Node(data)
        # 1 means start , "size" means insert at the end and "> size" means insert after end
        if position == 1: #insert at start
            self.insertStart(data)
        elif position > self.size: #insert after the end
            self.insertEnd(data)
        else: #insert at a position in between
            currentNode = self.start
            pos = 1
            while pos != position:
                previousNode = currentNode
                currentNode = previousNode.next
                pos += 1
            newNode.next = previousNode.next
            previousNode.next = newNode
            self.size += 1

    def remove(self,data):
        currentNode = self.start
        while currentNode != None and currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.next
        if currentNode == None:
            print("Provided value doesn't exist!")
            return
        elif currentNode == self.start:
            self.start = currentNode.next
            currentNode.next = None
        else:
            previousNode.next = currentNode.next
            currentNode.next = None
        self.size -= 1

    def show(self):
        tempNode = self.start
        while tempNode != None:
            print(tempNode.data)
            tempNode = tempNode.next
    

linkedlist = LinkedList()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)
linkedlist.insertEnd(32)
linkedlist.insert(9,1)
linkedlist.insert(7,linkedlist.size+1)
linkedlist.insert(5,linkedlist.size)
linkedlist.insert(50,5)
linkedlist.remove(7)
linkedlist.remove(9)
linkedlist.show()