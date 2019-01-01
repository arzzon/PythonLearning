''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of binary search tree.
 *
 *  Written:       30/12/2018
 *  Last updated:  30/12/2018
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |    bigO(n)    |  bigO(logn)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(n)    |  bigO(logn)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(n)    |    bigO(n)    |    bigO(n)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(n)    |  bigO(logn)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  
 *  % python bst.py
 *
***************************************************************************** '''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Bst(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data) #Assign the new node as the root
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data < node.data:
            if node.left:
                self.insertNode(data,node.left)
            else:
                node.left = Node(data) #Assign the new node reference as the left child of this leaf node
        else:
            if node.right:
                self.insertNode(data,node.right)
            else:
                node.right = Node(data) #Assign the new node reference as the right child of this leaf node

    def traverse(self):
        if self.root:
            self.inOrder(self.root)
    
    def inOrder(self,node): #LVR(LEFT VERTEX RIGHT)
        if node.left:
            self.inOrder(node.left)
        print(node.data, end=" ")
        if node.right:
            self.inOrder(node.right)

    def preOrder(self,node): #VLR(VERTEX LEFT RIGHT)
        print(node.data, end=" ")
        if node.left:
            self.preOrder(node.left)
        if node.right:
            self.preOrder(node.right)

    def postOrder(self,node): #VLR(LEFT RIGHT VERTEX)
        if node.left:
            self.postOrder(node.left)
        if node.right:
            self.postOrder(node.right)
        print(node.data, end=" ")

    def delete(self,data):
        if not self.root:
            print("Tree is empty")
        else:
            self.root = self.deleteNode(data,self.root)
    
    def deleteNode(self,data,node):
        #4 POSSIBLE CASES ARE POSSIBLE
        #1. LEAF NODE TO BE REMOVED
        #2. NODE HAVING A LEFT CHILD TO BE REMOVED
        #3. NODE HAVING A RIGHT CHILD TO BE REMOVED
        #4. NODE HAVING TWO CHILDREN TO BE REMOVED
        if not node: 
            return node #case where the data doesn't exist
        if data < node.data:
            node.left = self.deleteNode(data,node.left)
        elif data > node.data:
            node.right = self.deleteNode(data,node.right)
        else:
            if node.left and node.right:
                #NODE HAVING TWO CHILDREN TO BE REMOVED
                tempNode = self.getMax(node.left)
                node.data = tempNode.data
                node.left = self.deleteNode(tempNode.data,node.left)
            else:
                #1. LEAF NODE TO BE REMOVED(None is returned in this case) OR
                #2. NODE HAVING A LEFT CHILD TO BE REMOVED OR
                #3. NODE HAVING A RIGHT CHILD TO BE REMOVED
                if not node.right:
                    tempNode = node.left
                    del node
                    return tempNode
                elif not node.left:
                    tempNode = node.right
                    del node
                    return tempNode
        return node

    def getMax(self,node):
        if node.right:
            self.getMax(node.right)
        return node

    def getMin(self,node):
        if node.left:
            self.getMin(node.left)
        return node

bst = Bst()
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(1)
bst.insert(2)
bst.insert(8)
bst.insert(7)
bst.insert(7)
print("AFTER INSERTION INORDER")
bst.traverse()
print("\nPOSTORDER")
bst.postOrder(bst.root)
print("\nPREORDER")
bst.preOrder(bst.root)
bst.delete(2)
bst.delete(6)
bst.delete(5)
bst.delete(9) #if element doesn't exist then nothing is removed
print("\nINORDER")
bst.inOrder(bst.root)

'''
BST BEFORE REMOVING ELEMENTS
         5
      3     6
    1         8
      2     7
           7

BST AFTER REMOVING ELEMENTS
AFTER REMOVING 2
         5
      3     6
    1         8
            7
           7
AFTER REMOVING 6
         5
      3     8
    1      7
          7
AFTER REMOVING 5
         3
      1     8
           7
          7
AFTER REMOVING 9
         3
      1     8
           7
          7
           
'''