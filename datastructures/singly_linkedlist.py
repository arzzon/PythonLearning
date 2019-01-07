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
    #next
    def __init__(self,data):
        self.data = data
        self.next = None #reference to next node

class LinkedList(object):
    def __init__(self):
        self.start = None #reference to first node
        self.size = 0  #size of the linkedlist
    
    def insertStart(self,data):
        newNode = Node(data)
        self.size += 1
        if self.start == None: #Linkedlist is empty
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
            tempNode = self.start
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = newNode

    def insert(self,data,position):
        newNode = Node(data)
        # <=1 means start , "size" means insert at the end and "> size" means insert after end
        if position <= 1: #insert at start
            self.insertStart(data)
        elif position > self.size: #insert after the end
            self.insertEnd(data)
        else: #insert at a position other than start and end
            previousNode = self.start
            pos = 2 #we start matching from 2 because we have handled inserting at start condition and in this case we need the details
                    #of the previous node, so in case of insert at 2 for example, we would have previous node pointing to start node. 
            while pos != position:
                previousNode = previousNode.next
                pos += 1
            newNode.next = previousNode.next
            previousNode.next = newNode
            self.size += 1

    def remove(self,data): #Removes first occurence of the node with the provided data
        currentNode = self.start
        while currentNode != None and currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.next
        if currentNode == None:
            print("Provided value doesn't exist!")
            return
        elif currentNode == self.start:  #Removing the first element
            self.start = currentNode.next
            currentNode.next = None
        else:
            previousNode.next = currentNode.next
            currentNode.next = None
        self.size -= 1

    def show(self):
        tempNode = self.start
        while tempNode != None:
            print(tempNode.data, end=" ")
            tempNode = tempNode.next
    
    def reverse(self,node): #Reversing linkedlist using recursion
        if not node.next:
            self.start = node
            return
        self.reverse(node.next)
        node.next.next = node
        node.next = None #Added so that the previous start node has nextlink set to NONE

    def showReverse(self,node):
        if not node:
            return
        self.showReverse(node.next)
        print(node.data,end=" ")


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
print("Show")
linkedlist.show()
print("\nShow Reverse")
linkedlist.showReverse(linkedlist.start)
linkedlist.reverse(linkedlist.start)
print("\nAfter reversing")
linkedlist.show()