''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of prim's algorithm.
 *
 *  Written:       29/1/2018
 *  Last updated:  29/1/2018
 *  
 *  -----------------------------------------------------------------
 *
 *  % python primsAlgo.py
 *
***************************************************************************** '''

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
        if self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] != -1 \
           or self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] == -1:
            if self.directed: # if directed then remove the edge specified else remove both src->dst and dst->src
                self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = -1
            else:
                self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = -1
                self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] = -1

    def show(self):
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

    def primsMST(self,v):
        cost = 0 #Stores the total cost
        mst_vertices = [] #This set stores the vertices for spanning tree in the order in which they are visited
        remaining_vertices = {u for u in self.vertices} #This set contains vertices that have not been processed yet
        min_weights = [9999999 for w in range(self.verticesNum)] #It stores the minimum weight of the edges
        min_weights[self.getIndex(v)] = 0 #Weight corresponding the first vertex is set to 0 to make the algo pick it first
        while len(remaining_vertices) != 0: #Continue till all vertices are processed in the component
            u = self.findMin(min_weights,remaining_vertices)
            if u == -1: #No more vertices left in the component
                break   #mst has been completed
            mst_vertices.append(u) #Added the vertex to the spanning tree
            remaining_vertices.discard(u) #Removed the vertex from the remaining_vertices list
            #Update the weights for the neighbours of u
            for i in range(self.verticesNum):
                if (self.vertices[i] not in mst_vertices) \
                   and (self.adjMatrix[self.getIndex(u)][i] != -1) \
                   and (self.adjMatrix[self.getIndex(u)][i] < min_weights[i]):
                    min_weights[i] = self.adjMatrix[self.getIndex(u)][i]
        print("MST:",mst_vertices)
        for c in min_weights: #calculating total cost
            if c  != 9999999:
                cost += c
        print("Cost:",cost)

    def findMin(self,min_weights, remaining_vertices):
        min = 9999999
        index = -1
        for i in range(self.verticesNum):
            if self.vertices[i] in remaining_vertices and min > min_weights[i]:
                index = i
                min = min_weights[i]
        if index != -1:
            return self.vertices[index]
        else:
            return index



if __name__ == "__main__":
    g = Graph(6,False,True)
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addEdge('a','c',5)
    g.addEdge('b','c',2)
    g.addEdge('b','e',3)
    g.addEdge('c','d',4)
    g.addEdge('c','e',8)
    print("Vertices: "+str(g.getVertices()))
    g.show()
    g.primsMST('a')


'''
a               b
  .           . .
5   .     2 .   .
      .   .     .
        c       . 8
      .   .     .
 4  .    3  .   .
  .           . .
d               e

        f

Adjacency Matrix:
         a      b       c       d       e       f
a       -1      -1      5       -1      -1      -1
b       -1      -1      2       -1      8       -1
c       5       2       -1      4       3       -1
d       -1      -1      4       -1      -1      -1
e       -1      8       3       -1      -1      -1
f       -1      -1      -1      -1      -1      -1

After removing the edge:
Adjacency Matrix:
         a      b       c       d       e       f
a       -1      -1      5       -1      -1      -1
b       -1      -1      2       -1      -1      -1
c       5       2       -1      4       3       -1
d       -1      -1      4       -1      -1      -1
e       -1      -1      3       -1      -1      -1
f       -1      -1      -1      -1      -1      -1

'''


