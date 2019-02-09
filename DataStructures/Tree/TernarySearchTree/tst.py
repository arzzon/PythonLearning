''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of Ternary Search Tree.
 *
 *  Written:       20/1/2018
 *  Last updated:  20/1/2018
 *  
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |    bigO(n)    |  bigO(log n)  |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(n)    |  bigO(log n)  |    bigO(1)    |
 *  -----------------------------------------------------------------
 *
 *  % python tst.py
 *
***************************************************************************** '''

class Node(object):
    def __init__(self, character, value = None):
        self.leftChild = None
        self.middleChild = None
        self.rightChild = None
        self.character = character
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getCharacter(self):
        return self.character

class Tst(object):
    def __init__(self):
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    def putItem(self, node, key, value, index):
        c = key[index]
        if node == None: #If there is no element in this position then insert the new node
            node = Node(c)
        if c < node.getCharacter(): #If the char in the key is < the current node char then go to leftChild to insert
           node.leftChild = self.putItem(node.leftChild, key, value, index)
        elif c > node.getCharacter(): #If the char in the key is > the current node char then go to rightChild to insert
            node.rightChild = self.putItem(node.rightChild, key, value, index)
        elif index < len(key) - 1: #Since the above conditions didn't match, then it means that the the character in the key and the character in the current node are equal, so try to insert it in middleNode
            node.middleChild = self.putItem(node.middleChild, key, value, index+1)
        else: #Since the above condition didn't match, this means the index has reached the end and thus we need to insert the value as well
            node.setValue(value)
        
        return node 

    def get(self,key): #Returns the value associated with the key
        value = self.getValue(self.rootNode, key, 0)
        if value == None:
            print("Key doesn't exist!")
        else:
            print("Key={0} Value={1}".format(key, value))
    
    def getValue(self, node, key, index):
        if node == None: #Return None if the key doesn't exist
            return None
        c = key[index]
        if c < node.getCharacter(): #move to left subtree
            value = self.getValue(node.leftChild, key, index)
        elif c > node.getCharacter(): #move to right subtree
            value = self.getValue(node.rightChild, key, index)
        elif index < len(key) -1: #move to middle subtree
            value = self.getValue(node.middleChild, key, index+1)
        else: #Now the index has reached end of the key, so the value is stored at this node, return it
            return node.getValue()

        return value
if __name__ == "__main__":
    tst = Tst()
    tst.put("cat",10)
    tst.put("carrot",14)
    tst.put("jug",5)
    tst.put("bat",8)
    tst.get("cat")
    tst.get("carrot")
    tst.get("jug")
    tst.get("bat")
    tst.get("car")