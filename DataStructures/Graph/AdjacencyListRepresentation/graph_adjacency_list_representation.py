''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of graph with adjacency list.
 *
 *  Written:       22/1/2018
 *  Last updated:  22/1/2018
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
 *  % python graph_adjacency_list_representation.py
 *
***************************************************************************** '''

class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.adjList = {}
    def addNeighbour(self, id, weight = 0): #Adds the vertex and weight(0 in case of unweighted) to the neighbour list 
        self.adjList[id] = weight
    def getConnections(self): #Returns the id of all the vertices those have an edge to this vertex
        return self.adjList
    def getId(self):
        return self.id
    def __str__(self):
        return self.id + ":" + str(self.getConnections())

class Graph(object):
    def __init__(self, directed = False, weighted = False):
        self.vertices = {}
        self.verticesNum = 0
        self.directed = directed
        self.weighted = weighted

    def addVertex(self, id):
        self.verticesNum += 1
        self.vertices[id] = Vertex(id)
    
    def addEdge(self, src, dst, weight = 0):
        if self.directed: #If directed then add the edge in the specified direction
            self.vertices[src].addNeighbour(dst,weight)
        else:#If undirected then edge should be in both direction so we need to make both the vertices as each other's neighbour
            self.vertices[src].addNeighbour(dst,weight)
            self.vertices[dst].addNeighbour(src,weight)

    def getVertices(self):
        return self.vertices.keys()
    
    def show(self):
        for x in self.vertices.values():
            #print(x.getId()+":"+str(x.getConnections()))
            print(x) #Used the __str__ of Vertex class to print the vertext

if __name__ == "__main__":
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addEdge('a','c')
    g.addEdge('b','c')
    g.addEdge('b','e')
    g.addEdge('c','d')
    g.addEdge('c','e')
    print("Vertices: "+str(g.getVertices()))
    g.show()


'''
a               b
  .           . .
    .       .   .
      .   .     .
        c       .
      .   .     .
    .       .   .
  .           . .
d               e

        f
'''