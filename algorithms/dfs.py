''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of DFS traversal algorithm for graph.
 *
 *  Written:       24/1/2018
 *  Last updated:  24/1/2018
 *  
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |    bigO(-)    |  bigO(-)  |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(-)    |  bigO(-)  |    bigO(-)    |
 *  -----------------------------------------------------------------
 *
 *  MEMORY COMPLEXITY: bigO(logN) 
 *  Memory complexity depends on the number of elements stored in the 
 *  stack or the max size of stack used in the dfs algo. It can be 
 *  observed that at max we store h number of vertices in the Tree(if
 *  we assume that we are using dfs for a balanced BTree), where h is 
 *  the height of the tree. Height of a BTree is logN.
 *
 *  % python dfs.py
 *
***************************************************************************** '''
#Stack class
class Stack(object):
    def __init__(self):
        self.size = 0
        self.data = [] #data are stored in a list
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self,value):
        self.data.append(value) #Values are appended at the end of the list
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            self.size -= 1
            return self.data.pop(-1) #Removes the value from the end of the list

    def peek(self):
        return self.data[-1] #Returns the value from the end of the list

    def show(self):
        print(self.data)

#Graph class
class Graph(object):
    def __init__(self, verticesNum, directed = False, weighted = False):
        self.vertices = [] #Stores the vertices
        self.verticesNum = verticesNum #Number of vertices
        self.adjMatrix = [[-1 for i in range(verticesNum)] for j in range(verticesNum)] #vertices X vertices matrix, -1 value means no edge
        self.directed = directed
        self.weighted = weighted

    def addVertex(self, id): #Stores the vertices
        self.vertices.append(id)

    def getIndex(self, vertex): #Returns the index of the vertex
        return self.vertices.index(vertex)
    
    def addEdge(self, src, dst, weight = 0):
        if self.directed: #If directed then add the edge in the specified direction
            self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = weight
        else:#If undirected then edge should be in both direction so we need to make both the vertices as each other's neighbour
            self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = weight
            self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] = weight

    def getVertices(self):
        return self.vertices

    def removeEdge(self,src,dst):
        if self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] != -1 or self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] == -1:
            if self.directed: # if directed then remove the edge specified else remove both src->dst and dst->src
                self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = -1
            else:
                self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = -1
                self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] = -1

    def show(self): #Displays the adjacency matrix
        print("Adjacency Matrix:")
        print('  \t',end=" ")
        for v in self.vertices:
            print(v,end="\t")
        print()
        for i in range(len(self.vertices)):
            print(self.vertices[i],end="\t")
            for j in range(len(self.vertices)):
                print(self.adjMatrix[i][j],end="\t")
            print()

    #DFS by using recursion
    def dfs_util(self,v,state):
        state[self.getIndex(v)] = 0 # state=-1 means vertex is not visited and state=0 means vertex is visited
        print(v)
        for i in range(self.verticesNum): # We find the next unvisited neighbour and call dfs for that vertex
            if self.adjMatrix[self.getIndex(v)][i] != -1 and state[i] == -1: #If vertex is found to be unvisited
                self.dfs_util(self.vertices[i],state)
    
    def dfs_recursion(self,start): #Uses recursion for dfs
        state = [-1 for i in range(self.verticesNum)]
        self.dfs_util(start,state) #state is passed in parameter as a reference not value.
        for i in range(len(state)):
            if state[i] == -1:
                self.dfs_util(self.vertices[i],state) #DFS is called for the vertices that are separated from the graph

    #DFS without using recursion
    def dfs(self,start):
        s = Stack()
        s.push(start)
        state = [-1 for i in range(self.verticesNum)] # state=-1 means vertex is not visited and state=0 means vertex is visited
        state[self.getIndex(start)] = 0
        while(not s.isEmpty()):
            v = s.pop()
            print(v)
            verticesLeft = False
            for i in range(self.verticesNum):
                if self.adjMatrix[self.getIndex(v)][i] != -1 and state[i] == -1:
                    s.push(self.vertices[i])
                    state[i] = 0
                    verticesLeft = True
            if s.isEmpty() and not verticesLeft: #Check if any other vertices are left
                for i in range(len(state)):
                    if state[i] == -1: #If vertex is found to be unvisited
                        s.push(self.vertices[i])     

if __name__ == "__main__":
    g = Graph(7,False,True)
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addVertex('g')
    g.addEdge('a','c',5)
    g.addEdge('b','c',2)
    g.addEdge('b','g',2)
    g.addEdge('b','e',8)
    g.addEdge('c','d',4)
    g.addEdge('c','e',3)
    print("Vertices: "+str(g.getVertices()))
    g.show()
    print("DFS using recursion:")
    g.dfs_recursion('a')
    print("DFS without recursion:")
    g.dfs('a')


'''
a               b
  .           . . .
5   .     2 .   .   .  1
      .   .     .     .
        c       .       g
      .   .     .
 4  .    3  .   .
  .           . .
d               e
              .  
            .  8
          .
        f

Adjacency Matrix:
         a      b       c       d       e       f       g
a       -1      -1      5       -1      -1      -1      -1
b       -1      -1      2       -1      8       -1      2
c       5       2       -1      4       3       -1      -1
d       -1      -1      4       -1      -1      -1      -1
e       -1      8       3       -1      -1      -1      -1
f       -1      -1      -1      -1      -1      -1      -1
g       -1      2       -1      -1      -1      -1      -1

DFS using recursion:
a
c
b
e
g
d
f
DFS without recursion:
a
c
e
d
b
g
f

'''