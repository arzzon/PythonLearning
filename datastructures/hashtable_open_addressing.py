''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of hash table datastructure by using open addressing.
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
 *  % python hashtable_open_addressing.py
 *
***************************************************************************** '''

class HashTable(object):
    MAX_SIZE = 10
    def __init__(self):
        self.keys = [None] * self.MAX_SIZE
        self.values = [None] * self.MAX_SIZE
        self.size = 0

    def hash(self,key): #This hash function generates an index by adding the ASCII value of the characters of the key % MAX_SIZE
        sum = 0 
        for i in range(len(key)):
            sum += ord(key[i])
        return sum % self.MAX_SIZE

    def insert(self,key,value): #
        if self.size == self.MAX_SIZE:
            print("HashTable is full!")
            return
        index = self.hash(key)
        while self.values[index] != None: #Goes on till we find an index which has not been allocated
            if self.keys[index] == key: #If key already exists, then we just need to update it's value here.
                break
            index = (index+1)%self.MAX_SIZE #next index
        if self.keys[index] != key:# This is make sure that size is not increased when we update a value that already exists
            self.size += 1
        self.keys[index]= key
        self.values[index] = value

    def show(self):
        print("KEYS:")
        for i in self.keys:
            print(i,end=",")

        print("\nVALUES:")
        for i in self.values:
            print(i,end=",")

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
hashObj.show()
'''
a 97=>7
b 8
c 9
d 0
e 1
aa 4
f 2
a 7=>2
x 3
'''

            

