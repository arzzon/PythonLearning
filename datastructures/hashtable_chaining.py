''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of hash table datastructure by using chaining.
 *
 *  Written:       16/1/2018
 *  Last updated:  16/1/2018
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
 *  % python hashtable_chaining.py
 *
***************************************************************************** '''

class Node(object):
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.next = None

    def show(self):
        print("[{0},{1}]".format(self.key,self.value),end=",")

class HashTable(object):
    MAX_SIZE = 10
    def __init__(self):
        self.arr = [None] * self.MAX_SIZE
        self.size = 0

    def hash(self,key): #This hash function generates an index by adding the ASCII value of the characters of the key % MAX_SIZE
        sum = 0 
        for i in range(len(key)):
            sum += ord(key[i])
        return sum % self.MAX_SIZE

    def insert(self,key,value): #
        index = self.hash(key)
        if self.arr[index] == None:
            self.arr[index] = Node(key,value)
        else:
            node = self.arr[index]
            while node.next != None:
                if(node.key == key):
                    break
                node = node.next
            if(node.key != key):
                self.size += 1
                node.next = Node(key,value)
            else:
                node.value = value
                

    def show(self):
        print("[KEYS,VALUES]:")
        for ele in self.arr:
            if not ele: #ele == None
                print(ele)
            else:
                node = ele
                while(node != None):
                    node.show()
                    node = node.next
                print()
        


hashObj = HashTable()
hashObj.insert('a',5)
hashObj.insert('b',15)
hashObj.insert('c',52)
hashObj.insert('d',51)
hashObj.insert('e',7)
hashObj.insert('aa',1)
hashObj.insert('f',9)
hashObj.insert('a',30)
hashObj.insert('x',40)
hashObj.insert('asd',90)
hashObj.insert('abcas',303)
hashObj.insert('xguydgy',70)
hashObj.insert('ag',77)
hashObj.show()
'''
a 97=>2
b 3
c 4
d 0
e 1
aa 4

'''
