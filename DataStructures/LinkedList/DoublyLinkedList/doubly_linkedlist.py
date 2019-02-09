''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of doubly linkedlist.
 *
 *  Written:       29/12/2018
 *  Last updated:  29/12/2018
 *
 *  % python doubly_linkedlist.py
 *
***************************************************************************** '''
class Node(object):
    #value
    #next
    #previous
    def __init__(self,data):
        self.data = data
        self.next = None #reference to next node
        self.previous = None #reference to previous node

class LinkedList(object):
    def __init__(self):
        self.start = None #reference to first node
        self.end = None #reference to end node
        self.size = 0  #size of the linkedlist
    
    def insertStart(self,data):
        newNode = Node(data)
        self.size += 1
        if self.start == None: #Linkedlist is empty
            self.start = newNode
            self.end = newNode # Update the end reference in case of first insertion at start
        else:
            newNode.next = self.start
            self.start.previous = newNode #reference of newly created node is stored in the previous link of the (previous)start node
            self.start = newNode

    def insertEnd(self,data):
        newNode = Node(data)
        self.size += 1
        if self.start == None:
            self.start = newNode
        else:
            self.end.next = newNode
            newNode.previous = self.end
        self.end = newNode #Update the end reference

    def insert(self,data,position):
        newNode = Node(data)
        # <=1 means start , "size" means insert at the end and "> size" means insert after end
        if position <= 1: #insert at start
            self.insertStart(data)
        elif position > self.size: #insert after the end
            self.insertEnd(data)
        else: #insert at a position other than start and end
            currentNode = self.start
            pos = 1 #we start matching from 1 because for doubly linked list we just need the node at the position that has been provided 
            while pos != position:
                currentNode = currentNode.next
                pos += 1
            currentNode.previous.next = newNode
            newNode.next = currentNode
            newNode.previous = currentNode.previous
            currentNode.previous = newNode
            self.size += 1

    def remove(self,data): #Removes first occurence of the node with the provided data
        currentNode = self.start
        while currentNode != None and currentNode.data != data:
            currentNode = currentNode.next
        if currentNode == None:
            print("Provided value doesn't exist!")
            return
        elif currentNode == self.start:  #Removing the first element
            self.start = currentNode.next
            currentNode.next.previous = None #previous node of the new start node should be None
            currentNode.next = None
        elif currentNode == self.end: #Removing end node
            self.end = currentNode.previous
            currentNode.previous.next = None
            currentNode.next = currentNode.previous = None
        else:
            currentNode.next.previous = currentNode.previous
            currentNode.previous.next = currentNode.next
            currentNode.next = currentNode.previous = None
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